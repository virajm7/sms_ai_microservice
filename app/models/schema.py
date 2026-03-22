from pydantic import BaseModel
from typing import Optional

class SMSRequest(BaseModel):
    message: str
    user_id: Optional[str] = "test_user"

class SMSResponse(BaseModel):
    transaction_id: str
    user_id: str
    amount: Optional[float]
    currency: str
    type: str
    merchant: str
    category: str
    timestamp: str
    raw_sms: str
    hash: str
    source: str