import random
from datetime import datetime, timedelta

import pymongo

# Kết nối MongoDB
client = pymongo.MongoClient("")

db = client["user"]

# Lấy dữ liệu username từ collection "user"
user_collection = db["user"]
user_docs = user_collection.find({}, {"username": 1})  # Chỉ lấy trường "username"
usernames = [doc["username"] for doc in user_docs]

# Cấu hình tham số
start_date = datetime(2024, 9, 5)
end_date = datetime(2024, 10, 1)
days_count = (end_date - start_date).days + 1
access_collection = db["truycap"]


# Hàm tạo thời gian ngẫu nhiên trong ngày
def generate_random_start_end_times(base_date):
    start_time = base_date + timedelta(hours=random.randint(0, 23), minutes=random.randint(0, 59),
                                       seconds=random.randint(0, 59))
    end_time = start_time + timedelta(minutes=random.randint(2, 60))
    return start_time.isoformat(), end_time.isoformat()


# Tạo dữ liệu truy cập
for day in range(days_count):
    current_date = start_date + timedelta(days=day)
    daily_access_count = random.randint(6000, 10000)  # Số lượt truy cập ngẫu nhiên từ 6000 đến 10000

    for _ in range(daily_access_count):
        username = random.choice(usernames)
        start, end = generate_random_start_end_times(current_date)
        clickquangcao = random.randint(1, 8)

        record = {
            "ngay": current_date.strftime("%d/%m/%Y"),
            "username": username,
            "start": start,
            "end": end,
            "clickquangcao": clickquangcao
        }

        # Lưu từng bản ghi vào MongoDB
        access_collection.insert_one(record)
        print("update successfull!      " + record["username"] + "          " + record["ngay"])

print("Dữ liệu truy cập đã được lưu vào MongoDB")
