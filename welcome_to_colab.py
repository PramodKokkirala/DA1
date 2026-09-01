
import pandas as pd
df = pd.read_csv('/content/employee_dataset_1000_records.csv')
print(df)

import pandas as pd
db= pd.read_excel("/content/employee_dataset_1000_records.xlsx")
print(db)

import pandas as pd
da = pd.read_json("/content/employees.json")
print(da)

import pandas as pd
df = pd.read_csv('/content/employee_dataset_1000_records.csv')
print(df.head(2))
print(df.tail(3))
print(df.isna().sum())

import pandas as pd
db= pd.read_excel("/content/Sample - Superstore (1).xls")
print(db.info)
print(db.describe())
print(db.head(10))
print(db.tail(10))
print(db[["Category", "Sales"]])
print(db.loc[db["Sales"]>500],"Sales")
print(db[db["Profit"]>100])
print(db[db["Region"]=="West"])
print(db[(db["Quantity"]>5) & (db["Sales"]>500)])

print(db[(db["Region"]=="West") | (db["Region"]=="East")])
print(db.loc[10:19])
print(db.iloc[10:20])
print(db[["Customer Name", "Category", "Sales", "Profit"]].head(10))
print(db.iloc[[0, 5, 10, 15, 20]])
print(db.iloc[20:31])
print(db.rename(columns={'Sales':'Sales_Amount','Profit':'Profit_Amount','Quantity':'Quantity_sold','Category':'Product_Category'},inplace=True))
