# Job Search AI Assistant

An AI-assisted job search tool that automatically collects job postings from Norwegian sources, matches them against a user profile, and uses a local LLM to evaluate which positions are worth reviewing.

The project is designed to reduce the amount of manual searching by filtering thousands of job advertisements down to a manageable list of relevant opportunities.

## Features

### Job Collection

Currently supports:

* NAV Job Feed API

Planned:

* FINN.no integration
* Additional Norwegian job sources

### Job Storage

Job advertisements are stored locally in SQLite.

Stored information includes:

* Job ID
* Title
* Company
* URL
* Full job description
* Last modified date
* Processing status

### Skill-Based Matching

The first filtering stage uses skill matching.

Supported skills include:

* Python
* SQL
* Machine Learning
* Data Analysis
* Statistical Modeling
* Scikit-learn
* Pandas
* PyTorch
* TensorFlow
* Feature Engineering
* Model Evaluation
* Generative AI
* RAG
* LangChain
* LlamaIndex
* Docker

The matcher supports:

* English job advertisements
* Norwegian job advertisements
* Skill aliases and alternative spellings

### AI Evaluation

Jobs that exceed a configurable matching threshold are sent to a local Large Language Model for deeper evaluation.

The LLM can:

* Assess overall relevance
* Explain why a job matches
* Identify missing qualifications
* Generate a match score
* Produce concise summaries

### Filtering

Current filtering rules include:

* Ignore inactive advertisements
* Ignore jobs containing "Senior" in the title
* Process only new or unprocessed jobs

## Project Structure

```text
job-search-ai-assistant/
│
├── data/
│   └── jobs.db
│
├── collectors/
│   ├── nav_collector.py
│   └── finn_collector.py
│
├── repositories/
│   └── job_repository.py
│
├── matching/
│   ├── matcher.py
│   ├── skills.py
│   └── aliases.py
│
├── llm/
│   └── evaluator.py
│
├── config/
│   └── settings.py
│
├── main.py
│
└── README.md
```

## Matching Pipeline

```text
NAV Feed
    ↓
Download Job
    ↓
Store in SQLite
    ↓
Skill Matching
    ↓
Threshold Check
    ↓
Local LLM Evaluation
    ↓
Relevant Job List
```

## Requirements

* Python 3.12+
* SQLite
* Requests

Recommended:

* Ollama
* RTX 4090 or similar GPU for local inference

## Installation

Clone the repository:

```bash
git clone https://github.com/henrikbreitenstein/job-search-ai-assitant.git
cd job-search-ai-assitant
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file:

```env
NAV_API_TOKEN=your_token_here
```

Never commit this file to GitHub.

## Running

Run the collection and matching pipeline:

```bash
python main.py
```

Example output:

```text
==================================================
Title: Data Scientist
Company: Statnett

Match Score: 1.00

Matched Skills:
- Python
- SQL
- Machine Learning
- Docker

LLM Assessment:
Strong match with experience in machine learning,
data analysis and software development.
==================================================
```

## Current Status

Implemented:

* NAV feed collection
* SQLite storage
* Skill matching
* English/Norwegian aliases
* Processed job tracking

In Progress:

* Local LLM integration
* Embedding-based matching
* FINN integration

Planned:

* Web interface
* Email notifications
* Daily job reports
* RAG-powered profile understanding
* Multiple user profiles

## License

MIT License
