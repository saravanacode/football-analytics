import pandas as pd
from pymongo import MongoClient

# MongoDB connection string
mongo_uri = "mongodb://ls_mongodb:mar21%40live@3.6.82.52:27017/ls-retail"
client = MongoClient(mongo_uri)

# Access the database and collection
db = client['ls-retail']
invoices_collection = db['transactions']

# Fetch all entries from the invoices collection
transactions = list(invoices_collection.find())

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(transactions)

# Optionally, drop the MongoDB ObjectId if it's not needed
if '_id' in df.columns:
    df.drop(columns=['_id'], inplace=True)

# Save the DataFrame to a CSV file
csv_file_path = 'invoices1.csv'
df.to_csv(csv_file_path, index=False)

print(f"All entries have been exported to {csv_file_path}")
