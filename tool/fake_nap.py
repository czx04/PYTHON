import random
from datetime import datetime, timedelta

import pymongo
from pymongo import MongoClient

# Kết nối tới MongoDB
client = pymongo.MongoClient("mongodb+srv://anhchaiuem:anhchaiuem@pep.ghbx8ax.mongodb.net/?retryWrites=true&w=majority&appName=PEP")

db = client["user"]

# Collection user và nap
user_collection = db["user"]
nap_collection = db["nap"]

# Lấy 2000 user đầu tiên từ collection user
usernames = [user["username"] for user in user_collection.find({}, {"username": 1}).limit(2000)]

# Các giá trị cho discount và money tương ứng
discount_values = [1, 5, 10, 50]
money_options = {
    1: [9, 49, 99, 149, 199, 599, 999],
    5: [5, 25, 75, 125, 175, 575, 975],
    10: [0, 40, 140, 190, 590, 990],
    50: [0, 30, 130, 180, 580, 980]
}

# Khoảng thời gian từ ngày 1/9/2024 đến 1/10/2024
start_date = datetime(2024, 9, 1)
end_date = datetime(2024, 10, 1)

# Hàm tạo random time trong ngày
def random_time():
    hour = random.randint(1, 23)
    minute = random.randint(0, 59)
    second = random.randint(1, 59)
    return f"{hour:02}:{minute:02}:{second:02}"

# Tạo dữ liệu và ghi vào MongoDB
for single_date in (start_date + timedelta(days=n) for n in range((end_date - start_date).days + 1)):
    daily_transactions = random.randint(1500, 3000)  # Số lượt nạp ngẫu nhiên mỗi ngày

    for _ in range(daily_transactions):
        username = random.choice(usernames)
        time = random_time()
        discount = random.choice(discount_values)
        money = random.choice([m for m in money_options[discount] if m >= 0])

        # Tạo một giao dịch nạp
        nap_transaction = {
            "username": username,
            "date": single_date.strftime("%d/%m/%Y"),
            "time": time,
            "money": money,
            "discount": discount
        }

        # Ghi từng giao dịch vào collection nap
        nap_collection.insert_one(nap_transaction)
        print("update successfull!      " + nap_transaction["username"] + "          " + nap_transaction["date"])

print("Dữ liệu giao dịch nạp đã được ghi vào MongoDB với số lượt nạp ngẫu nhiên mỗi ngày.")
