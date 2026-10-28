#importing my toolkits
import sqlite3
import pandas as pd

#loading the raw CSV file
print("loading kaggle Synthetic Healthcare Claims dataset...")
import os

# Get the absolute path to the data folder safely
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, '../data/healthcare_data.csv')

print(f"Attempting to load from: {csv_path}")
df = pd.read_csv(csv_path)

#inspecting the structure.
#the first code extracts every column header from the dataset
#the second code prints out the list of column headers to verify berfore wrting SQL queries
print("\nDetected Columns in your Dataset:")
print(df.columns.tolist())

# creating and connecting the database
# the sqlite.connect creates a new local database file named claims.db
db_path = os.path.join(current_dir, '../data/claims.db')
conn = sqlite3.connect(db_path)

# pushing data into SQL table
df.to_sql('raw_claims', conn, if_exists='replace', index=False)

# running a Test Query to verify
test_query = "SELECT * FROM raw_claims LIMIT 3;"
result = pd.read_sql(test_query, conn)
print("\nTest SQL Query Output:")
print(result)

# closing the database connection
conn.close()