from fastapi import APIRouter
from app.models.schema import SMSRequest, SMSResponse
from app.services.ai_parser import parse_with_ai
from app.services.validator import validate_response
from app.services.merchant_db import MERCHANT_DB
from app.services.normalizer import normalize_merchant
from app.services.time_utils import generate_timestamp
from app.services.utils import generate_transaction_id, generate_hash, format_merchant_name

router = APIRouter(prefix="/api")


@router.post("/parse-sms", response_model=SMSResponse)
async def parse_sms(data: SMSRequest):

    # 🔥 DEBUG LOG
    print("\n========= NEW SMS RECEIVED =========")
    print(f"USER ID: {data.user_id}")
    print(f"MESSAGE: {data.message}")
    print("====================================\n")

    # Step 1: AI parsing
    ai_result = await parse_with_ai(data.message)

    # Step 2: validate
    validated = validate_response(ai_result)

    # Step 3: normalize merchant
    merchant_raw = validated.get("merchant", "")
    normalized_merchant = normalize_merchant(merchant_raw)

    # Step 4: format merchant (for UI)
    formatted_merchant = format_merchant_name(normalized_merchant)

    # Step 5: category override
    category = MERCHANT_DB.get(
        normalized_merchant,
        validated.get("category", "others")
    )

    # 🔥 STEP 6: TIME (FIXED)
    time_data = generate_timestamp(validated.get("date"))

    return {
    "transaction_id": generate_transaction_id(),
    "user_id": data.user_id,
    "amount": validated.get("amount"),
    "currency": "INR",
    "type": validated.get("type"),
    "merchant": formatted_merchant,
    "category": category,

    # 🔥 SAFE ACCESS (NO CRASH)
    "timestamp": time_data.get("timestamp"),
    "transaction_time": time_data.get("transaction_time"),
    "transaction_month": time_data.get("transaction_month"),
    "transaction_year": time_data.get("transaction_year"),

    "raw_sms": data.message,
    "hash": generate_hash(data.message),
    "source": "ai"
}