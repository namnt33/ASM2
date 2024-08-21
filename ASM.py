import pandas as pd

# Load the CSV files
website_df = pd.read_csv('Website.csv')
sale_df = pd.read_csv('Sale.csv')
product_group_df = pd.read_csv('Product_Group.csv')
product_df = pd.read_csv('Product.csv')
market_df = pd.read_csv('Market.csv')
customer_df = pd.read_csv('Customer.csv')

# Handle empty data and error data
website_df.fillna('', inplace=True)
sale_df.fillna(0, inplace=True)
product_group_df.fillna('', inplace=True)
product_df.fillna('', inplace=True)
market_df.fillna(0, inplace=True)
customer_df.fillna('', inplace=True)

# Check for duplicate rows
print('Duplicate rows in each dataset:')
print('Website:', website_df.duplicated().sum())
print('Sale:', sale_df.duplicated().sum())
print('Product Group:', product_group_df.duplicated().sum())
print('Product:', product_df.duplicated().sum())
print('Market:', market_df.duplicated().sum())
print('Customer:', customer_df.duplicated().sum())

# Analyze the data
print('\nProduct Information:')
print(product_df.head())

print('\nCustomer Information:')
print(customer_df.head())

print('\nMarket Trend Information:')
print(market_df.head())

# Check for missing values
print('\nMissing values in each dataset:')
print('Website:', website_df.isnull().sum())
print('Sale:', sale_df.isnull().sum())
print('Product Group:', product_group_df.isnull().sum())
print('Product:', product_df.isnull().sum())
print('Market:', market_df.isnull().sum())
print('Customer:', customer_df.isnull().sum())

# Perform basic analysis
print('\nProduct Categories:')
print(product_df['Product_Category'].unique())

print('\nCustomer Segments:')
print(customer_df['Customer_Segment'].unique())

print('\nMarket Trend Forecast:')
print(market_df.groupby('Product_Group_ID')['Market_Trend_Forecast'].mean())