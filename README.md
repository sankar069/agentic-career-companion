# Agentic Career Counseling Companion

This is an AI-powered career guidance tool that provides personalized career suggestions using IBM's Granite large language model (LLM).

## Features
- FastAPI backend for AI communication
- Streamlit frontend for user interface
- Realtime suggestions using IBM Watsonx.ai Granite Model

## Run Locally

1. Clone the repo  
2. Create `.env` with your IBM API Key  
3. Run the backend:
   ```
   uvicorn main:app --reload
   ```
4. Run the frontend:
   ```
   streamlit run app.py
   ```

## Dependencies
See `requirements.txt`
