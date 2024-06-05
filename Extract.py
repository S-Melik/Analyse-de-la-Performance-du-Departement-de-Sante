import pymysql
import pandas as pd

# MySQL database connection details
host = 'localhost'  # or '127.0.0.1'
user = 'root'
password = '1381'  # Replace with your actual password
database = 'health_insurance'
query = 'SELECT * FROM data_table2024'  # Adjust your query as needed

# Connect to the database
connection = pymysql.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Execute the query and fetch the data into a DataFrame
df = pd.read_sql(query, connection)

# Save the DataFrame to a CSV file
csv_file_path = 'extracted_data2024.csv'
df.to_csv(csv_file_path, index=False)

# Close the database connection
connection.close()

print(f"Data extracted and saved to {csv_file_path}")

# ----------------------------------------------------------------------------------------------------------------------------------------

# Load data from the extracted CSV file
df = pd.read_csv('extracted_data2024.csv')

# Step 1: Remove Blank Rows
df = df[~((df['Declaration'] == '') & (df['Date reception'] == '') & 
          (df['Frais engages'] == '') & (df['Police'] == '') & 
          (df['Adherent CIN'] == '') & (df['Adherent ville'] == '') & 
          (df['Code maladie'] == ''))]

# Step 2: Remove Duplicates
# Identify duplicates by creating a 'row_num' column
df['row_num'] = df.groupby(['Declaration', 'Date reception', 'Frais engages', 
                            'Police', 'Adherent CIN', 'Adherent ville', 
                            'Code maladie']).cumcount() + 1

# Remove duplicates
df = df[df['row_num'] == 1].copy()
df.drop(columns=['row_num'], inplace=True)

# Step 4: Standardize the Data
df['Declaration'] = pd.to_numeric(df['Declaration'], errors='coerce').fillna(0).astype(int)
df['Date reception'] = pd.to_datetime(df['Date reception'], errors='coerce')
df['Frais engages'] = pd.to_numeric(df['Frais engages'], errors='coerce').fillna(0.0).astype(float)
df['Code maladie'] = pd.to_numeric(df['Code maladie'], errors='coerce').fillna(0).astype(int)

# Save the cleaned data to a new CSV file
df.to_csv('extracted_data2024_cleaned.csv', index=False)

print("Data cleaning and standardization complete. Cleaned data saved to 'extracted_data2024_cleaned.csv'")
