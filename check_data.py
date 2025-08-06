import pandas as pd

# Load data sources
print("Loading Bonibello reference data...")
bonibello_ref = pd.read_csv('Bonibello Pricing/위탁수거_프라이싱_데이터베이스_forGPT_v2.csv')
print("\nColumns:", bonibello_ref.columns.tolist())
print("\nFirst few rows:")
print(bonibello_ref.head())

print("\n" + "="*80 + "\n")

print("Loading product list data...")
product_list = pd.read_csv('Bonibello Pricing/상품 리스트_202504251310_v3.csv')
print("\nColumns:", product_list.columns.tolist())
print("\nFirst few rows:")
print(product_list.head())

print("\n" + "="*80 + "\n")

print("Loading MNKL data...")
mnkl_data = pd.read_csv('Bonibello Pricing/mnkl_products_processed_v3.csv')
print("\nColumns:", mnkl_data.columns.tolist())
print("\nFirst few rows:")
print(mnkl_data.head()) 