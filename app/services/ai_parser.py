import httpx
import json
from app.core.config import OPENROUTER_API_KEY, OPENROUTER_URL

SYSTEM_PROMPT = """
You are a financial SMS parser.

Extract transaction data and return ONLY JSON.

Fields:
amount (number)
type (debit/credit/refund/transfer)
merchant (string)
category (food, transport, shopping, travel, bills, subscription, transfer, others)
date (YYYY-MM-DD or null)

Rules:
- debited → debit
- credited → credit
- person → transfer
- ignore ref numbers
- extract merchant after 'to' or 'at'

Return ONLY JSON.
"""

async def parse_with_ai(message: str):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            OPENROUTER_URL,
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "openai/gpt-3.5-turbo",
                "temperature": 0.1,
                "messages": [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": f"Extract from this SMS:\n{message}"}
                ]
            }
        )

        result = response.json()
        content = result["choices"][0]["message"]["content"]

        try:
            return json.loads(content)
        except:
            return {}