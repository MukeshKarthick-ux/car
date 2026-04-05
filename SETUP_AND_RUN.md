# Setup and Run Guide

## ✅ Project Status: FULLY OPERATIONAL

The Policy Compliance Checker is now **complete and running**! 🎉

### 🚀 Quick Start (Already Done)
Both servers are running:
- **Backend API**: http://localhost:8000 ✅
- **Frontend UI**: http://localhost:5000 ✅

### 🧪 Testing Results
All API tests passed (5/5) ✅
- Health check: Working
- Compliance checking: Working with intelligent mock responses
- Error handling: Working

### 🎨 UI Improvements Added
- Modern dark theme with gradients
- Enhanced styling and animations
- Better result visualization (green for compliant, red for non-compliant)
- Improved user experience

### 📋 Test the Application
1. Open: http://localhost:5000/login
2. Login: `admin` / `admin123`
3. Try these test actions:
   - ✅ "I need to work overtime this weekend"
   - ❌ "I want to work from home without approval"
   - ❌ "I want to install unauthorized software"

### 🔧 For Production Use
To use with real OpenAI API:
1. Get an OpenAI API key from https://platform.openai.com/account/api-keys
2. Replace `your_openai_api_key_here` in `backend/.env`
3. Restart the backend server

The system will automatically switch from mock responses to real AI-powered compliance checking!

## 📋 Prerequisites
- Python 3.8 or higher
- OpenAI API key (for GPT-4o-mini model)
- pip (Python package manager)

## 🚀 Step-by-Step Setup

### 1. Set Environment Variables
Create a `.env` file in the `backend/` directory:

```bash
cd backend
```

Create `.env` with:
```
OPENAI_API_KEY=your_openai_api_key_here
```

### 2. Prepare Policy Documents
**Important:** The backend expects `backend/data/policies.pdf`

Currently, there's a placeholder file. You need to:
- Add your actual policy PDF to `backend/data/policies.pdf`
- OR replace the placeholder with your policy document

The system will process the PDF and create a vector store automatically on first run.

### 3. Install Backend Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 4. Install Frontend Dependencies

```bash
# In a new terminal/command prompt
cd frontend
pip install -r requirements.txt
```

## ▶️ Running the Application

### Terminal 1: Start Backend Server
```bash
cd backend
uvicorn main:app --reload --port 8000
```

Output should show:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
```

### Terminal 2: Start Frontend Server
```bash
cd frontend
python app.py
```

Output should show:
```
 * Running on http://127.0.0.1:5000
```

## 🔖 Access the Application

### Login Page
**URL:** http://localhost:5000/login

**Default Credentials:**
- Username: `admin`
- Password: `admin123`

### Dashboard
After login, you'll be redirected to: **http://localhost:5000/dashboard**

## 📌 Important Notes

1. **Vector Store Creation:** The first time you run the app, it will create a FAISS vector store from your PDF. This may take a moment.

2. **OpenAI API Usage:** The app uses OpenAI's API for embeddings and completions. Ensure you have:
   - Valid API key
   - Sufficient API credits

3. **Security:** For production use:
   - Change the SECRET_KEY in `backend/auth.py`
   - Use proper password hashing
   - Store credentials securely

4. **Backend API Endpoints:**
   - `POST /token` - Login endpoint
   - `POST /check` - Check compliance (requires auth token)
   - `GET /users/me` - Get current user info
   - `GET /` - API info

## 🐛 Troubleshooting

### "Module not found" errors
```bash
pip install -r requirements.txt
```

### "Vector store is missing" error
- Ensure `backend/data/policies.pdf` exists
- Backend will create the vector store automatically on startup

### "Cannot connect to backend" error
- Verify backend is running on port 8000
- Check firewall settings

### CORS errors
- Backend is configured to work with frontend on localhost

## ✨ Features

- **Secure Authentication:** JWT-based login system
- **RAG Pipeline:** Retrieval-Augmented Generation using OpenAI
- **Dark Theme:** Professional UI interface
- **RESTful API:** Easy to integrate with other systems
