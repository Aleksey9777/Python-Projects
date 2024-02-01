import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('online_retail.csv')

print(df.head())
print(df.describe())
print(df.isnull().sum())

plt.figure(figsize=(10,6))
sns.boxplot(x=df['Quantity'])
plt.title('Distribution of Quantity')
plt.xlabel('Quantity')
plt.show()

customer_data = df.groupby('CustomerId').agg({'Quantity': 'sum', 'InvoiceDate': 'nunique'}).reset_index()
customer_data.columns = ['CustomerId', 'TotalQuantity', 'UniqueInvoices']

plt.scatter(customer_data['UniqueInvoices'], customer_data['TotalQuantity'])
plt.title('Customer Segmentation based on Purchase Behavior')
plt.xlabel('Number of Unique Invoices')
plt.ylabel('Total Quantity Purchased')
plt.show()