import pyodbc 
import pandas as pd
#connecting 
cnxn_str = ("Driver={ODBC Driver 18 for SQL Server};"
            "Server=AMINS-COMPUTER;"
            "Database=master;"
            "Trusted_Connection=yes;"
            "TrustServerCertificate=YES;")
cnxn = pyodbc.connect(cnxn_str)
data = pd.read_sql("SELECT TOP(100) * FROM mnistTableTest",cnxn)

