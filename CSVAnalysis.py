import pandas as pd
import matplotlib.pyplot as plt

# load CSV file
file_path = "/Users/akshayramen/PythonCSVProject/ReadingCSV/sample_sales_data_updated.csv"
sales_data = pd.read_csv(file_path)

# check for missing values
print("Missing values in each column:")
print(sales_data.isnull().sum())

# Check data types
print("\n Data types of each column:")
print(sales_data.dtypes)

# converting 'date' column to datetime if it's not already
sales_data['Date']= pd.to_datetime(sales_data['Date'])

# basic statistics
print("\nDescriptive statistics of dataset:")
print(sales_data.describe())

#display first few rows to verify
print("\nFirst few rows of the cleaned dataset:")
print(sales_data.head())


# Group data by date and sume the quantitive and revenue
daily_sales =  sales_data.groupby('Date').sum(numeric_only=True)

# #Plot sales trends over time
# plt.figure(figsize=(12, 6)) 
# plt.plot(daily_sales.index, daily_sales['Quantity Sold'], label='Quantity Sold')
# plt.plot(daily_sales.index, daily_sales['Revenue'], label='Revenue')
# plt.title('Sales Trends Over Time')
# plt.xlabel('Date')
# plt.ylabel('Total')
# plt.legend()
# plt.grid(True)
# plt.show()


#EDA Best-selling products
product_sales = sales_data.groupby('Product').sum(numeric_only=True)
sorted_by_quantity = product_sales.sort_values(by='Quantity Sold', ascending=False)
sorted_by_revenue = product_sales.sort_values(by='Revenue', ascending=False)

print("\nBest-selling products by quantity:")
print(sorted_by_quantity)

print("\nBest-selling products by revenue:")
print(sorted_by_revenue)

# EDA - Revenue per month
sales_data['Month'] = sales_data['Date'].dt.to_period('M')
monthly_revenue = sales_data.groupby('Month').sum (numeric_only=True)['Revenue']

# Print monthly revenue
print("\nMonthly revenue:")
print(monthly_revenue)



