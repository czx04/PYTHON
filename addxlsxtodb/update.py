import os
import pandas as pd
from pymongo import MongoClient


def update_mongodb_from_xlsx(folder_path, mongo_uri="mongodb://localhost:27017/"):
    # Connect to MongoDB
    client = MongoClient(mongo_uri)

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.xlsx'):
            file_path = os.path.join(folder_path, file_name)
            base_name = os.path.splitext(file_name)[0]

            db = client[base_name]
            all_sheets = pd.read_excel(file_path, sheet_name=None)

            for sheet_name, df in all_sheets.items():
                records = df.to_dict(orient='records')
                collection_name = sheet_name.replace(' ', '_')

                collection = db[collection_name]

                for record in records:
                    query = {'id': record['id']} if 'id' in record else None

                    if query:
                        existing_record = collection.find_one(query)

                        if existing_record:
                            collection.update_one(query, {'$set': record})
                            print(
                                f"Updated record with id {record['id']} in collection '{collection_name}' from file '{file_name}'.")
                        else:
                            # Insert the record if it does not exist
                            collection.insert_one(record)
                            print(
                                f"Inserted new record with id {record['id']} into collection '{collection_name}' from file '{file_name}'.")
                    else:
                        print(
                            f"No unique identifier found for record in collection '{collection_name}' from file '{file_name}'. Consider adding a unique field for proper updates.")
    client.close()

update_mongodb_from_xlsx('path/to/your/folder')
