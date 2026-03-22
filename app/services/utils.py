import uuid
import hashlib

def generate_transaction_id():
    return str(uuid.uuid4())

def generate_hash(message: str):
    return hashlib.md5(message.encode()).hexdigest()

def format_merchant_name(name: str):
    return name.title() if name else "Unknown"