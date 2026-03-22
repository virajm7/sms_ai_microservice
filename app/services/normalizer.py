def normalize_merchant(name: str):
    if not name:
        return "unknown"

    name = name.lower().strip()

    # remove common noise words
    noise_words = ["pvt", "ltd", "limited", "india", "services", "trf", "txn"]

    for word in noise_words:
        name = name.replace(word, "")

    name = name.strip()

    # match known merchants
    for key in [
        "zepto", "swiggy", "zomato", "uber", "ola", "rapido",
        "irctc", "amazon", "flipkart", "myntra", "ajio",
        "google", "netflix", "spotify", "youtube",
        "jio", "airtel", "paytm", "phonepe", "gpay",
        "bigbasket", "blinkit", "dunzo"
    ]:
        if key in name:
            return key

    return name