from pymongo import MongoClient

client = MongoClient(
    f"mongodb+srv://anhchaiuem:anhchaiuem@pep.ghbx8ax.mongodb.net/?retryWrites=true&w=majority&appName=PEP")

db = client['overview']
collection = db['test']


datagame = [a for a in collection.find()]

months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

user_counts = 1500
total_games = 9
total_dau = 4080901
average_playtime = 42736
