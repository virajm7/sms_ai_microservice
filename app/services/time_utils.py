from datetime import datetime

def generate_timestamp(date_str=None):
    if date_str:
        try:
            dt = datetime.strptime(date_str, "%Y-%m-%d")
        except:
            dt = datetime.now()
    else:
        dt = datetime.now()

    return {
        "timestamp": dt.isoformat(),
        "transaction_time": dt.strftime("%H:%M:%S"),
        "transaction_month": dt.month,
        "transaction_year": dt.year
    }