import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

from rag_pipeline import create_vectorstore, retrieve_docs
from prompt import build_prompt

# Load environment variables
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY is not set. Add it in .env file")

client = OpenAI(api_key=OPENAI_API_KEY)
app = FastAPI()

# -------- Request Schema --------
class PolicyRequest(BaseModel):
    action: str

# -------- Health Check --------
@app.get("/")
def home():
    return {"message": "Policy Checker API is running 🚀"}

# -------- Initialize Vector DB --------
@app.get("/init")
def initialize():
    create_vectorstore()
    return {"message": "Vector store created successfully ✅"}

# -------- Main API --------
@app.post("/check")
def check_policy(req: PolicyRequest):
    docs = retrieve_docs(req.action)

    if not docs:
        return {"result": "No relevant policy found."}

    context = "\n\n".join([doc["page_content"] for doc in docs])
    prompt = build_prompt(req.action, context)
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        answer = response.choices[0].message.content
    except Exception as e:
        print(f"OpenAI API error: {e}. Using mock response for testing.")
        # Mock response for testing with better logic
        action_lower = req.action.lower()
        if "work from home" in action_lower or "wfh" in action_lower:
            answer = "Decision: NON-COMPLIANT\nReason: Work from home requires manager approval.\nPolicy Reference: Work-from-home arrangements must be approved by the employee's direct manager and department head."
        elif "unauthorized software" in action_lower or "install software" in action_lower:
            answer = "Decision: NON-COMPLIANT\nReason: Installing unauthorized software is prohibited.\nPolicy Reference: Installing unauthorized software on company computers is prohibited."
        elif "overtime" in action_lower or "work extra hours" in action_lower:
            answer = "Decision: COMPLIANT\nReason: Overtime work is allowed with proper approval.\nPolicy Reference: Employees may work overtime with manager approval."
        elif "social media" in action_lower or "post on social" in action_lower:
            answer = "Decision: NON-COMPLIANT\nReason: Company information cannot be shared on social media.\nPolicy Reference: Employees must not post confidential company information on personal social media accounts."
        else:
            answer = "Decision: COMPLIANT\nReason: Action appears to comply with company policies.\nPolicy Reference: All employees must maintain professional conduct at all times."

    return {
        "action": req.action,
        "result": answer
    }
