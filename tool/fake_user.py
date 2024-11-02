import random
import string
import pymongo
from datetime import datetime, timedelta

# MongoDB configuration
client = pymongo.MongoClient("mongodb+srv://anhchaiuem:anhchaiuem@pep.ghbx8ax.mongodb.net/?retryWrites=true&w=majority&appName=PEP")
db = client["user"]
collection = db["user"]

# Helper functions
def random_username():
    length = random.randint(6, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def random_registration_time():
    start_date = datetime(2023, 9, 1, 0, 0)
    end_date = datetime(2023, 10, 1, 23, 59)
    delta = end_date - start_date
    random_seconds = random.randint(0, int(delta.total_seconds()))
    return start_date + timedelta(seconds=random_seconds)

def random_age():
    return random.randint(12, 39)

def random_server():
    return random.choice(["VN", "CN", "JP", "TW", "CAM", "KOR"])

def random_platform():
    return random.choice(["ios", "android", "macos", "windows"])

def random_status():
    return random.choice(["on", "off"])

def random_reviews_star():
    return random.randint(1, 5)

# Generate and insert user data
user_data = []
for _ in range(10000):
    user = {
        "username": random_username(),
        "registration_time": random_registration_time(),
        "age": random_age(),
        "server": random_server(),
        "platform": random_platform(),
        "status": random_status(),
        "reviews_star": random_reviews_star()
    }
    user_data.append(user)

# Insert data in batches to avoid memory issues
batch_size = 1000
for i in range(0, len(user_data), batch_size):
    batch = user_data[i:i + batch_size]
    collection.insert_many(batch)

print("Data insertion completed.")
