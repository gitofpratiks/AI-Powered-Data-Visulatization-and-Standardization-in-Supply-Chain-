import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Simulated dataset for an Indian Retail Store
np.random.seed(42)
num_records = 500

data = {
    'Store_ID': np.random.randint(100, 200, num_records),
    'Store_Location': np.random.choice(['Mumbai', 'Delhi', 'Bangalore', 'Kolkata', 'Chennai'], num_records),
    'Product_Category': np.random.choice(['Fruits', 'Dairy', 'FMCG', 'Electronics', 'Clothing'], num_records),
    'Selling_Price': np.random.randint(50, 5000, num_records),
    'Units_Sold': np.random.randint(10, 200, num_records),
    'Stock_Level': np.random.randint(0, 500, num_records),
    'Supplier_ID': np.random.randint(1000, 1100, num_records),
    'Delivery_Time_Days': np.random.randint(1, 10, num_records),
    'Customer_Reviews': np.random.uniform(1, 5, num_records).round(1),
    'Discount_Applied': np.random.choice([0, 5, 10, 15, 20], num_records)
}

df = pd.DataFrame(data)

# Correctly calculating Cost_Price and Profit_Per_Unit
df['Cost_Price'] = df['Selling_Price'] * np.random.uniform(0.6, 0.9, num_records)
df['Profit_Per_Unit'] = df['Selling_Price'] - df['Cost_Price']

df['Cost_Price'] = df['Cost_Price'].round(2)
df['Profit_Per_Unit'] = df['Profit_Per_Unit'].round(2)

# Data Cleaning
print("Missing Values:")
print(df.isnull().sum())

df.dropna(inplace=True)  # Drop rows with missing values (if any)

# Save dataset for later use
df.to_csv("retail_store_data.csv", index=False)

# Exploratory Data Analysis (EDA)
plt.figure(figsize=(10,5))
sns.boxplot(x='Product_Category', y='Selling_Price', data=df)
plt.title('Price Distribution by Product Category')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10,5))
sns.barplot(x='Store_Location', y='Units_Sold', data=df, estimator=np.sum)
plt.title('Total Units Sold by City')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10,5))
sns.scatterplot(x='Stock_Level', y='Units_Sold', data=df)
plt.title('Stock Levels vs. Units Sold')
plt.show()

plt.figure(figsize=(10,5))
sns.histplot(df['Customer_Reviews'], bins=10, kde=True)
plt.title('Customer Review Ratings Distribution')
plt.show()

# Insights & Business Recommendations
insights = """
Business Insights:
1. High-profit categories should be prioritized for inventory.
2. Optimize stock levels based on demand in different locations.
3. Improve delivery times to reduce delays in the supply chain.
4. Increase stock for products with high customer ratings.
5. Analyze the impact of discounts on sales and profits.
"""

print(insights)

# Save insights to a text file
with open("business_insights.txt", "w") as f:
    f.write(insights)