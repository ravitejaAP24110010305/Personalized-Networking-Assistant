# Personalized Networking Assistant

## Overview
An AI-powered web application that generates personalized networking conversation starters using FastAPI, Streamlit, Hugging Face Transformers, GPT-2, and the Wikipedia API.

## Features
- Event theme extraction
- AI-generated conversation starters
- Wikipedia fact checking
- Conversation history
- Feedback logging

## Tech Stack
- Python
- FastAPI
- Streamlit
- Hugging Face Transformers
- GPT-2
- Wikipedia API
- Pytest

## Run the Backend

```bash
uvicorn app.main:app --reload
```

## Run the Frontend

```bash
streamlit run frontend/app.py
```