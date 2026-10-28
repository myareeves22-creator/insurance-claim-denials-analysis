import os
import sqlite3
import pandas as pd

# 1. Safely connect to our SQLite database using absolute pathing
current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, '../data/claims.db')
conn = sqlite3.connect(db_path)

#2. Write the SQL query to answer the stakeholder's question:
# "Which insurance carriers/types are causing the highest financial loss due to denials?"
query = """
SELECT 
    "Insurance Type",
    COUNT("Claim ID") AS total_denied_claims,
    SUM("Billed Amount") AS total_loss_revenue
FROM raw_claims
WHERE "Claim Status" = 'Denied'
GROUP BY "Insurance Type"
ORDER BY total_loss_revenue DESC; 
"""

#3. Execute the query and load the results into a pandas DataFrame
print("Running RCM Denial Rvenue Recovery Analysis...\n")
df_results = pd.read_sql(query, conn)

#4. Print the formatted business report to the terminal
print("--- STAKEHOLDER REPORT: Top Denied Insurance Types by Lost Revenue---")
print(df_results.to_string(index=False))

# Close connection
conn.close()