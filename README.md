# Policy Compliance Checker

A comprehensive web application that uses Retrieval-Augmented Generation (RAG) to check if user-described actions comply with company policy documents.

## Features

- **RAG Pipeline**: AI-powered compliance checking using LangChain and OpenAI
- **Simple API**: Easy-to-run backend with a single `/check` endpoint
- **Frontend UI**: Flask-based dashboard that posts user actions to the backend
- **Vector DB**: FAISS store generated from the policy PDF

## Project Structure

```
policy-compliance-checker/
├── backend/
│   ├── main.py              # FastAPI server with authentication and compliance API
│   ├── rag_pipeline.py      # RAG pipeline implementation
│   ├── prompt.py            # AI prompts for compliance checking
│   ├── auth.py              # JWT authentication utilities
│   ├── requirements.txt     # Backend dependencies
│   ├── data/
│   │   └── policies.pdf     # Company policy documents (replace placeholder)
│   └── vectorstore/         # FAISS vector database
└── frontend/
    ├── app.py               # Flask web application
    ├── requirements.txt     # Frontend dependencies
    ├── templates/
    │   ├── login.html       # Login page
    │   └── dashboard.html   # Main dashboard with compliance checker
    └── static/
        └── css/
            └── style.css    # Dark theme styles
```

## Setup Instructions

### Prerequisites
- Python 3.8+
- OpenAI API key

### Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd policy-compliance-checker/backend
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set environment variables:
   ```bash
   export OPENAI_API_KEY="your-openai-api-key"
   ```

4. Place your company policy document as `data/policies.pdf`

5. Run the backend server:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd policy-compliance-checker/frontend
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the frontend server:
   ```bash
   python app.py
   ```

## Usage

1. Open your browser and go to `http://localhost:5000`
2. Login with username: `admin`, password: `admin123`
3. Enter a description of an action you want to check for compliance
4. Click "Check Compliance" to get an AI-powered analysis

## Testing Examples

Try these sample actions to test the compliance checker:

### ✅ Compliant Actions:
- "I need to work overtime this weekend to finish an important project"
- "I want to request vacation time for next month"
- "I need to attend a professional development conference"

### ❌ Non-Compliant Actions:
- "I want to work from home tomorrow without asking my manager"
- "I want to install unauthorized software on my work computer"
- "I want to post company information on my personal social media"

### 🤔 Edge Cases:
- "I need to share a client contact with a colleague"
- "I want to use company email for personal matters"
- "I need to handle confidential documents"

## API Documentation

The backend provides a REST API. Key endpoints:

- `POST /check`: Check action compliance
- `GET /init`: Build the vector store from `backend/data/policies.pdf`

## Security Notes

- Change the default admin credentials in production
- Use environment variables for secrets
- Implement proper user management for multiple users
- Add HTTPS in production

## Technologies Used

- **Backend**: FastAPI, LangChain, OpenAI GPT, FAISS, JWT
- **Frontend**: Flask, HTML5, CSS3
- **AI/ML**: Retrieval-Augmented Generation, Vector Embeddings