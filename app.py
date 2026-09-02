from flask import Flask, request, jsonify
from shapely.geometry import Point, shape
from shapely.ops import unary_union
from datetime import datetime, date
import json
import os

app = Flask(__name__)

zones = []


def load_geojson(filepath, zone_type, severity):
    if not os.path.exists(filepath):
        return
    with open(filepath, "r") as f:
        data = json.load(f)
    for feature in data["features"]:
        props = feature.get("properties", {})
        zones.append({
            "geometry":    shape(feature["geometry"]),
            "zone_id":     props.get("MRGID", props.get("zone_id", "N/A")),
            "name":        props.get("GEONAME", props.get("name", zone_type)),
            "zone_type":   zone_type,
            "severity":    severity,
            "restricted":  True,
            "description": props.get("description", "")
        })
    print(f"Loaded {filepath} — {len(data['features'])} zones")


def generate_5nm_zone():
    nm12_geometries = [z["geometry"] for z in zones if z["zone_type"] == "TERRITORIAL_12NM"]
    if not nm12_geometries:
        return
    merged = unary_union(nm12_geometries)
    buffer_5nm = merged.buffer(-0.0834)
    zones.append({
        "geometry":    buffer_5nm,
        "zone_id":     "5NM_NOTRAWL",
        "name":        "5NM Coastal No-Trawling Zone",
        "zone_type":   "NO_TRAWLING_5NM",
        "severity":    "CRITICAL",
        "restricted":  True,
        "description": "5NM coastal no-trawling zone — trawling prohibited"
    })
    print("Generated 5NM No-Trawling Zone")


def check_monsoon_ban(lat, lon):
    today = date.today()

    if lon > 90:
        start  = date(today.year, 5, 15)
        end    = date(today.year, 7, 31)
        coast  = "Andaman & Nicobar"
        period = "May 15 - July 31"
    elif lon < 80:
        start  = date(today.year, 6, 1)
        end    = date(today.year, 7, 31)
        coast  = "West Coast"
        period = "June 1 - July 31"
    else:
        start  = date(today.year, 4, 15)
        end    = date(today.year, 6, 14)
        coast  = "East Coast"
        period = "April 15 - June 14"

    return {
        "ban_active":   start <= today <= end,
        "coast":        coast,
        "ban_period":   period,
        "checked_date": today.isoformat()
    }


def validate_india_bounds(lat, lon):
    if not (6 <= lat <= 38):
        return {
            "error":       "Latitude out of India range",
            "valid_range": "6 to 38 (Kanyakumari to Kashmir)",
            "received":    lat
        }
    if not (68 <= lon <= 98):
        return {
            "error":       "Longitude out of India range",
            "valid_range": "68 to 98 (Gujarat to Andaman)",
            "received":    lon
        }
    return None


load_geojson("india_eez.geojson",  "EEZ_200NM",        "LOW")
load_geojson("india_12nm.geojson", "TERRITORIAL_12NM", "HIGH")
generate_5nm_zone()
print(f"Total zones loaded: {len(zones)}")


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message":      "India Restricted Fishing Zone API",
        "zones_loaded": len(zones),
        "endpoints": {
            "check_zone_GET":  "GET  /check-zone?latitude=15.0&longitude=80.5",
            "check_zone_POST": "POST /check-zone  — body: {latitude, longitude}",
            "list_zones":      "GET  /zones",
            "health":          "GET  /health"
        },
        "india_bounds": {
            "latitude":  "6 to 38 (Kanyakumari to Kashmir)",
            "longitude": "68 to 98 (Gujarat to Andaman)"
        }
    })


@app.route("/check-zone", methods=["GET", "POST"])
def check_zone():
    if request.method == "GET":
        lat = request.args.get("latitude")
        lon = request.args.get("longitude")
        if lat is None or lon is None:
            return jsonify({
                "error":   "Pass latitude and longitude as query params",
                "example": "http://127.0.0.1:5000/check-zone?latitude=15.0&longitude=80.5"
            }), 400
        lat = float(lat)
        lon = float(lon)
    else:
        data = request.get_json()
        if not data:
            return jsonify({"error": "JSON body required"}), 400
        lat = float(data["latitude"])
        lon = float(data["longitude"])

    bound_error = validate_india_bounds(lat, lon)
    if bound_error:
        return jsonify(bound_error), 400

    point = Point(lon, lat)
    matched_zones = []

    for zone in zones:
        if zone["geometry"].contains(point):
            matched_zones.append({
                "zone_id":     zone["zone_id"],
                "name":        zone["name"],
                "zone_type":   zone["zone_type"],
                "severity":    zone["severity"],
                "restricted":  True,
                "description": zone["description"]
            })

    monsoon = check_monsoon_ban(lat, lon)

    return jsonify({
        "latitude":            lat,
        "longitude":           lon,
        "in_restricted_zone":  len(matched_zones) > 0 or monsoon["ban_active"],
        "zones_found":         matched_zones,
        "total_zones_matched": len(matched_zones),
        "monsoon_ban":         monsoon,
        "checked_at":          datetime.utcnow().isoformat() + "Z"
    })


@app.route("/zones", methods=["GET"])
def list_zones():
    return jsonify({
        "total_zones": len(zones),
        "zones": [
            {
                "zone_id":   z["zone_id"],
                "name":      z["name"],
                "zone_type": z["zone_type"],
                "severity":  z["severity"]
            }
            for z in zones
        ]
    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status":       "ok",
        "zones_loaded": len(zones)
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)