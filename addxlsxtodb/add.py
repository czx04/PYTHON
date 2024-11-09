import os
import pandas as pd
from pymongo import MongoClient

mongo_uri=""

def upload_folder_to_mongodb(folder_path,mongo_uri):
    client = MongoClient(mongo_uri)

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.xlsx'):
            file_path = os.path.join(folder_path, file_name)
            base_name = os.path.splitext(file_name)[0]

            # Create a database named after the base file name
            db = client[base_name]

            # Read all sheets from the .xlsx file
            all_sheets = pd.read_excel(file_path, sheet_name=None)

            for sheet_name, df in all_sheets.items():
                # Convert DataFrame to dictionary
                records = df.to_dict(orient='records')
                collection_name = sheet_name.replace(' ', '_')  # Replace spaces in sheet names

                # Insert data into collection
                if records:
                    collection = db[collection_name]
                    result = collection.insert_many(records)
                    print(
                        f"{len(result.inserted_ids)} records inserted into collection '{collection_name}' in database '{base_name}'.")
                else:
                    print(f"No records to insert for sheet '{sheet_name}' in file '{file_name}'.")

    # Close the MongoDB connection
    client.close()


# Example usage
upload_folder_to_mongodb('path/to/your/folder')
