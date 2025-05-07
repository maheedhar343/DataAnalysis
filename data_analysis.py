import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

try:
    # Step 4: Data Analysis
    print("\nStep 4: Data Analysis")
    
    # Load wrangled data
    if not os.path.exists('sales_data_wrangled.csv'):
        raise FileNotFoundError("sales_data_wrangled.csv not found. Ensure data_preprocessing.py ran successfully.")
    
    data_analysis = pd.read_csv('sales_data_wrangled.csv')

    # Summary statistics
    print("Summary Statistics:\n", data_analysis.describe())

    # Correlation matrix (select numeric columns only)
    numeric_cols = data_analysis.select_dtypes(include=['int64', 'float64', 'bool']).columns
    plt.figure(figsize=(10, 6))
    sns.heatmap(data_analysis[numeric_cols].corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.savefig('correlation_matrix.png')
    plt.close()

    # Total Sales by Product
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Product', y='TotalSales', data=data_analysis)
    plt.title('Total Sales by Product')
    plt.savefig('sales_by_product.png')
    plt.close()

    # Total Sales over Time
    plt.figure(figsize=(10, 6))
    data_analysis['Date'] = pd.to_datetime(data_analysis['Date'])
    sns.lineplot(x='Date', y='TotalSales', data=data_analysis)
    plt.title('Total Sales Over Time')
    plt.savefig('sales_over_time.png')
    plt.close()

    print("Visualizations saved as PNG files.")

except Exception as e:
    print(f"Error in data_analysis.py: {str(e)}")
    raise