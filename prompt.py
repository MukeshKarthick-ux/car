def build_prompt(action, context):
    return f"""
You are a strict compliance officer.

Policy Context:
{context}

User Action:
{action}

Evaluate carefully and respond in this format:

Decision: COMPLIANT or NON-COMPLIANT
Reason: Clear explanation
Policy Reference: Exact quoted line from policy
"""
