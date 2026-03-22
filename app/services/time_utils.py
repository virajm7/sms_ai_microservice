from datetime import datetime

def generate_timestamp(date_str: str):
    try:
        # input like 2026-03-11
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")

        # add current time
        now = datetime.now()

        final = datetime(
            year=date_obj.year,
            month=date_obj.month,
            day=date_obj.day,
            hour=now.hour,
            minute=now.minute,
            second=now.second
        )

        return final.isoformat()

    except:
        return datetime.now().isoformat()