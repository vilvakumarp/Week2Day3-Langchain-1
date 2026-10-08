# LangChain + OpenAI + LangSmith Tracing

A simple LangChain application that sends multiple prompts to OpenAI using `ChatOpenAI` and demonstrates LangSmith tracing through environment variables.

The application also displays **latency and token usage directly in the terminal** for each run.

## Features

- Uses LangChain `ChatOpenAI`
- Sends 3 different prompts in a single execution
- Displays each model response
- Measures response latency
- Displays input, output, and total token usage
- Enables LangSmith tracing without adding tracing code to the application
- Uses a `.env` file for API keys and configuration
- Groups runs under a named LangSmith project

## Technologies

- Python
- LangChain
- OpenAI
- LangSmith
- python-dotenv

## Project Structure

```text
traced-app/
│
├── traced_app.py
├── .env
├── .gitignore
└── README.md
```

## Installation

Create and activate a virtual environment:

```bash
python -m venv venv
```

### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

Install the required packages:

```bash
pip install langchain langchain-openai python-dotenv
```

## Environment Variables

Create a `.env` file in the project directory:

```env
OPENAI_API_KEY=your-openai-api-key

LANGSMITH_TRACING=true
LANGSMITH_API_KEY=your-langsmith-api-key
LANGSMITH_PROJECT=simple-rag-app
```

Do **not** commit the `.env` file to GitHub.

## Run the Application

```bash
python traced_app.py
```

The application will execute three prompts and display information similar to:

```text
======================================================================
RUN 1
======================================================================

PROMPT:
Explain Newton's first law in simple terms for a 12-year-old.

ANSWER:
...

----------------------------------------------------------------------
RUN INFORMATION
----------------------------------------------------------------------
Latency       : 1.24 seconds
Input tokens  : 18
Output tokens : 96
Total tokens  : 114
----------------------------------------------------------------------
```

The same information is displayed for all three runs.

## LangSmith Tracing

LangSmith tracing is enabled entirely through environment variables:

```env
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=your-langsmith-api-key
LANGSMITH_PROJECT=simple-rag-app
```

There is intentionally **no LangSmith tracing code** inside `traced_app.py`.

After running the application, open LangSmith and navigate to the:

```text
simple-rag-app
```

project to inspect the individual runs.

For each run, LangSmith can be used to inspect:

- Exact prompt sent to the model
- Model response
- Execution latency
- Input tokens
- Output tokens
- Total tokens
- Model/run details

## What This Demonstrates

This project demonstrates how LangSmith can provide observability for a LangChain application without modifying the application with explicit tracing callbacks or tracing logic.

It also highlights the relationship between:

```text
Prompt
   ↓
LangChain ChatOpenAI
   ↓
OpenAI
   ↓
Response
   ↓
Latency + Token Usage
   ↓
LangSmith Trace
```

## Security

API keys should never be committed to GitHub.

Add the following to `.gitignore`:

```gitignore
.env
venv/
__pycache__/
*.pyc
```

If an API key is accidentally committed, revoke it immediately and generate a new one.

## Assignment Objective

The project fulfills the following objectives:

- Build a small LangChain application
- Use `ChatOpenAI`
- Send multiple prompts
- Print each response
- Enable LangSmith tracing using environment variables
- Use a named LangSmith project
- Inspect runs in LangSmith
- Compare latency and token usage across prompts
- Identify which prompt is more expensive and consider whether the additional cost is justified
