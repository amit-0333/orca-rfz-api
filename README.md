<!-- Header Wave Banner -->
<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=200&section=header&text=Amit%20Kumar&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=36&desc=Data%20Science%20%7C%20Machine%20Learning%20%7C%20AI%20Engineering&descAlignY=58&descAlign=50" />

<!-- Typing Animation -->
<div align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&duration=3000&pause=1000&color=6AD3F7&center=true&vCenter=true&width=700&lines=Learn+it+%E2%86%92+Build+it+%E2%86%92+Push+it+%E2%86%92+Repeat;Data+Science+%7C+Machine+Learning+%7C+AI+Engineering;Tested%2C+evaluated+and+documented" alt="Typing SVG" />
</div>

<br/>

<!-- Social Links -->
<div align="center">

  <a href="https://www.linkedin.com/in/amit-kumar-a62a3640a/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>
  &nbsp;
  <a href="https://www.kaggle.com/amitkumar038975" target="_blank">
    <img src="https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white" />
  </a>
  &nbsp;
  <a href="mailto:amitkumar03pqr@gmail.com?subject=Hi%20Amit%20-%20Found%20you%20on%20GitHub">
    <img src="https://img.shields.io/badge/Gmail-EA4335?style=for-the-badge&logo=gmail&logoColor=white" />
  </a>
  &nbsp;
  <a href="https://github.com/amit-0333" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" />
  </a>

<br/><br/>

  <img src="https://komarev.com/ghpvc/?username=amit-0333&label=Profile%20Views&color=0e75b6&style=flat" alt="profile views" />

<br/><br/>

**Open to entry-level roles in AI engineering, ML engineering, data science and data analysis.**

</div>

---

## About

I'm a data science and machine learning practitioner with a data analysis foundation, now moving into AI engineering. I build systems that take a model or an LLM from a notebook to something that runs, is tested, and can be trusted.

My path so far: Python, data structures and SQL, then exploratory analysis and visualization, then statistics, forecasting and machine learning, and most recently APIs, data pipelines, LLM applications and MLOps. Everything I learn goes into a public repository. The projects that matter most come with a written account of what went wrong along the way, not only what worked.

### What I bring

| Area | What I've done | Where to see it |
|---|---|---|
| **Machine learning** | Forecasting with ARIMA and Prophet, online learning with River, NLP with TF-IDF and spaCy, evaluation on true holdout data | [UPI Forecast](https://github.com/amit-0333/upi-forecast-uncertainty), [CareerPulse](https://github.com/amit-0333/careerpulse) |
| **LLM applications** | An LLM grounded in computed scores, natural language to SQL, and an annotation platform built around an LLM | [CareerPulse](https://github.com/amit-0333/careerpulse), [Flights NL Query](https://github.com/amit-0333/flights-nl-query-dashboard), [LabelFlow](https://github.com/amit-0333/labelflow) |
| **MLOps and engineering** | FastAPI services, Docker, MLflow experiment tracking, scheduled pipelines, drift detection, automated tests | [CareerPulse](https://github.com/amit-0333/careerpulse), [Flights NL Query](https://github.com/amit-0333/flights-nl-query-dashboard) |
| **Statistics and experimentation** | Hypothesis testing, A/B analysis, difference-in-differences, robust standard errors | [Causal Inference](https://github.com/amit-0333/causal-inference-ab-test-diff-in-diff) |
| **Data analysis and visualization** | SQL, pandas, and interactive dashboards in Streamlit, Dash and Plotly | [Dashboards](#more-projects) |

### How I work

- **Evaluate on data the model has never seen.** In my UPI forecasting project I caught data leakage in my own tuning process and rebuilt the evaluation. I also showed that a trend term improved in-sample fit while holdout error rose from 11.44% to 86.24%.
- **Ground LLMs in computed facts.** CareerPulse calculates match scores with a deterministic algorithm and gives those numbers to the LLM, so its advice rests on real data instead of estimates.
- **Test and document.** The flights dashboard has 25 automated tests, and my major projects include a `PROJECT_JOURNEY.md` covering decisions, mistakes and limitations.

---

## Selected Projects

### CareerPulse: AI Career Assistant
*Live job data, real skill-match scoring, LLM guidance and an MLOps pipeline.*

Most job tools list openings without telling you how well you fit. CareerPulse fetches jobs daily from 4 APIs, calculates a real skill-match percentage with a set-intersection algorithm, and passes those scores to an LLM so its career advice is based on actual numbers.

- Parses PDF resumes to extract skills, then reports match scores and skill gaps against live jobs
- Generates a 90-day learning roadmap, tailored cover letters and interview questions
- Online learning model (River) that updates as new jobs arrive, with drift detection that triggers retraining
- MLflow experiment tracking and a scheduled daily pipeline

**Stack:** Python, FastAPI, Streamlit, River, spaCy, MLflow, Groq, SQLite, Docker  
**Status:** live deployment coming soon  
**[View repository](https://github.com/amit-0333/careerpulse)**

---

### LabelFlow: LLM-Powered Data Annotation Platform
*A labeling workspace with an LLM in the loop.*

A platform for creating annotation projects, managing tasks and exporting labeled data, built around an LLM to speed up the labeling workflow. It includes user authentication, project and task management, templates and export.

**Stack:** Python, LLM  
**Status:** in active development  
**[View repository](https://github.com/amit-0333/labelflow)**

---

### Flights NL Query Dashboard
*Ask questions about Indian flight data in plain English and get answers from SQL.*

A Streamlit dashboard where an LLM (Gemini) translates natural language into SQL. It adds cross-sectional anomaly detection and a governed metrics layer so numbers stay consistent across queries, and it is backed by 25 automated tests.

**Stack:** Python, Streamlit, Gemini API, MySQL  
**[View repository](https://github.com/amit-0333/flights-nl-query-dashboard)**

---

### UPI Forecast with Honest Uncertainty
*Forecasting India's monthly UPI transaction volume, then testing the forecast on data the models never saw.*

ARIMA and Prophet with 95% confidence intervals, evaluated on a real 12-month holdout.

| Model | MAE (Mn) | RMSE (Mn) | MAPE |
|---|---|---|---|
| ARIMA(1,1,1) | 2,105 | 2,536 | 11.44% |
| Prophet (tuned) | 2,012 | 2,423 | 11.25% |

- Found and fixed data leakage in my own hyperparameter tuning
- Showed that "100% interval coverage" was a symptom of poorly calibrated long-horizon intervals, not a success

**Stack:** Python, statsmodels, Prophet, pandas, scikit-learn  
**[View repository](https://github.com/amit-0333/upi-forecast-uncertainty)**

---

### Causal Inference: A/B Testing and Difference-in-Differences
*Establishing whether a change caused an outcome, not just whether the two moved together.*

- **Cookie Cats A/B test (90,189 users):** moving the paywall gate from level 30 to 40 lowered 7-day retention from 19.02% to 18.20% (p = 0.0016), with no significant change in 1-day retention. An extreme outlier was identified and removed.
- **Card and Krueger (1994) replication (410 restaurants):** difference-in-differences with robust standard errors found no evidence that New Jersey's minimum wage increase reduced employment (+2.75 FTE per restaurant).

**Stack:** Python, SciPy, statsmodels, pandas, Matplotlib  
**[View repository](https://github.com/amit-0333/causal-inference-ab-test-diff-in-diff)**

---

## Tech Stack

<div align="center">

### Languages and Version Control

<table>
  <tr>
    <td align="center" width="110">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="60" height="60" alt="Python" />
      <br><b>Python</b>
    </td>
    <td align="center" width="110">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg" width="60" height="60" alt="Java" />
      <br><b>Java</b>
    </td>
  </tr>
  <tr>
    <td align="center" width="110">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original-wordmark.svg" width="60" height="60" alt="SQL" />
      <br><b>SQL</b>
    </td>
    <td align="center" width="110">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" width="60" height="60" alt="Git" />
      <br><b>Git</b>
    </td>
  </tr>
</table>

<br/>

### Data Science and ML Libraries

<table>
  <tr>
    <td align="center" width="110">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg" width="60" height="60" alt="NumPy" />
      <br><b>NumPy</b>
    </td>
    <td align="center" width="110">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" width="60" height="60" alt="Pandas" />
      <br><b>Pandas</b>
    </td>
    <td align="center" width="110">
      <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" width="60" height="60" alt="Scikit-learn" />
      <br><b>Scikit-learn</b>
    </td>
  </tr>
  <tr>
    <td align="center" width="110">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/scipy/scipy-original.svg" width="60" height="60" alt="SciPy" />
      <br><b>SciPy</b>
    </td>
    <td align="center" width="110">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/matplotlib/matplotlib-original.svg" width="60" height="60" alt="Matplotlib" />
      <br><b>Matplotlib</b>
    </td>
  </tr>
  <tr>
    <td align="center" width="110">
      <img src="https://seaborn.pydata.org/_images/logo-tall-lightbg.svg" width="50" height="60" alt="Seaborn" />
      <br><b>Seaborn</b>
    </td>
    <td align="center" width="110">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/plotly/plotly-original.svg" width="60" height="60" alt="Plotly" />
      <br><b>Plotly</b>
    </td>
  </tr>
</table>

<br/>

<img src="https://img.shields.io/badge/MLflow-0194E2?style=for-the-badge&logo=mlflow&logoColor=white" alt="MLflow" />
<img src="https://img.shields.io/badge/MLxtend-3776AB?style=for-the-badge" alt="MLxtend" />
<img src="https://img.shields.io/badge/statsmodels-4C72B0?style=for-the-badge" alt="statsmodels" />
<img src="https://img.shields.io/badge/Prophet-0078D4?style=for-the-badge" alt="Prophet" />
<img src="https://img.shields.io/badge/spaCy-09A3D5?style=for-the-badge&logo=spacy&logoColor=white" alt="spaCy" />
<img src="https://img.shields.io/badge/NLTK-154F5B?style=for-the-badge" alt="NLTK" />

<br/><br/>

### Frameworks, APIs and Deployment

<table>
  <tr>
    <td align="center" width="110">
      <img src="https://cdn.simpleicons.org/flask/808080" width="60" height="60" alt="Flask" />
      <br><b>Flask</b>
    </td>
    <td align="center" width="110">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg" width="60" height="60" alt="FastAPI" />
      <br><b>FastAPI</b>
    </td>
    <td align="center" width="110">
      <img src="https://streamlit.io/images/brand/streamlit-mark-color.svg" width="60" height="60" alt="Streamlit" />
      <br><b>Streamlit</b>
    </td>
  </tr>
  <tr>
    <td align="center" width="110">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="60" height="60" alt="Tkinter" />
      <br><b>Tkinter</b>
    </td>
    <td align="center" width="110">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" width="60" height="60" alt="Docker" />
      <br><b>Docker</b>
    </td>
  </tr>
</table>

<br/>

<img src="https://img.shields.io/badge/Plotly_Dash-119DFF?style=for-the-badge&logo=plotly&logoColor=white" alt="Dash" />
<img src="https://img.shields.io/badge/Gemini_API-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white" alt="Gemini API" />
<img src="https://img.shields.io/badge/Groq_API-F55036?style=for-the-badge" alt="Groq API" />

<br/><br/>

### Tools and Environments

<table>
  <tr>
    <td align="center" width="110">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" width="60" height="60" alt="VS Code" />
      <br><b>VS Code</b>
    </td>
    <td align="center" width="110">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pycharm/pycharm-original.svg" width="60" height="60" alt="PyCharm" />
      <br><b>PyCharm</b>
    </td>
    <td align="center" width="110">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/anaconda/anaconda-original.svg" width="60" height="60" alt="Anaconda" />
      <br><b>Anaconda</b>
    </td>
  </tr>
  <tr>
    <td align="center" width="110">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jupyter/jupyter-original-wordmark.svg" width="60" height="60" alt="Jupyter" />
      <br><b>Jupyter</b>
    </td>
    <td align="center" width="110">
      <img src="https://upload.wikimedia.org/wikipedia/commons/d/d0/Google_Colaboratory_SVG_Logo.svg" width="60" height="60" alt="Google Colab" />
      <br><b>Colab</b>
    </td>
  </tr>
  <tr>
    <td align="center" width="110">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/kaggle/kaggle-original.svg" width="60" height="60" alt="Kaggle" />
      <br><b>Kaggle</b>
    </td>
    <td align="center" width="110">
      <img src="https://cdn.simpleicons.org/github/808080" width="60" height="60" alt="GitHub" />
      <br><b>GitHub</b>
    </td>
  </tr>
</table>

</div>

---

## More Projects

<details>
<summary><b>Learning notes: ML and data science</b></summary>

<br/>

- [Machine Learning](https://github.com/amit-0333/machine-learning): notes and implementations
- [Math for Data Science](https://github.com/amit-0333/math-for-data-science)
- [SQL Learning](https://github.com/amit-0333/sql-learning)
- [EDA and Analysis Walkthrough](https://github.com/amit-0333/eda-and-analysis-walkthrough): end-to-end exploratory data analysis

</details>

<details>
<summary><b>Dashboards and analytics</b></summary>

<br/>

- [Global EV Market Dashboard](https://github.com/amit-0333/global-ev-market-dashboard)
- [India Census Dashboard](https://github.com/amit-0333/india-census-dashboard)
- [Indian Startup Funding Dashboard](https://github.com/amit-0333/indian-startup-funding)
- [COVID-19 India Dashboard](https://github.com/amit-0333/covid19-india-dashboard): built with Dash and Plotly

</details>

<details>
<summary><b>Backend and web apps</b></summary>

<br/>

- [IPL Stats API](https://github.com/amit-0333/flask-api/tree/main/ipl-stats-api): Flask REST API
- [Spotify Stats API](https://github.com/amit-0333/flask-api/tree/main/spotify-stats-api): Flask REST API
- [NLP Web App](https://github.com/amit-0333/nlp-web-app-flask): sentiment and text analysis
- [NLP GUI App](https://github.com/amit-0333/NLP-GUI-APP): Tkinter desktop app
- [Expense Tracker](https://github.com/amit-0333/flask-expense-tracker): Flask and SQLite
- [The Journal](https://github.com/amit-0333/the-journal): journaling web app

</details>

<details>
<summary><b>Foundations and reference guides</b></summary>

<br/>

- [Python Fundamentals](https://github.com/amit-0333/PYTHON-FUNDAMENTALS)
- [NumPy](https://github.com/amit-0333/python-numpy) and [Pandas](https://github.com/amit-0333/Pandas-Complete-Guide)
- [Matplotlib](https://github.com/amit-0333/matplotlib-complete-guide), [Seaborn](https://github.com/amit-0333/seaborn-complete-guide) and [Plotly](https://github.com/amit-0333/plotly-go-and-express)
- [DSA with Python](https://github.com/amit-0333/DSA-WITH-PYTHON) and [DSA Practice Questions](https://github.com/amit-0333/DSA-PRACTICE-QUESTION)
- [ER Diagram Schema](https://github.com/amit-0333/er-diagram-schema)

</details>

---

## GitHub Activity

<div align="center">
  <img src="https://streak-stats.demolab.com?user=amit-0333&theme=tokyonight&hide_border=true&hide_current_streak=true" alt="GitHub contribution stats" />
</div>

---

## Currently

- **Building:** LabelFlow, an LLM-powered annotation platform
- **Studying:** deep learning
- **Next:** RAG, LLM evaluation, agent workflows, and a live deployment of CareerPulse

---

<div align="center">

**The best way to reach me is LinkedIn or email, both linked at the top.**

</div>

<!-- Footer Wave -->
<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=120&section=footer" />
