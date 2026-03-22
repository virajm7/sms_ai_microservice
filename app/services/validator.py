def validate_response(data: dict):
    try:
        amount = float(data.get("amount")) if data.get("amount") else None
    except:
        amount = None

    txn_type = str(data.get("type", "unknown")).lower()
    if txn_type not in ["debit", "credit", "refund", "transfer"]:
        txn_type = "unknown"

    merchant = str(data.get("merchant", "unknown")).strip()
    category = str(data.get("category", "others")).lower()

    return {
        "amount": amount,
        "type": txn_type,
        "merchant": merchant,
        "category": category,
        "date": data.get("date")
    }