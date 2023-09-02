import pandas as pd
import random
from faker import Faker
from faker.providers import DynamicProvider

from product_details import Product_Details, Company_List_Per_Product

product_details_list = Product_Details

product_details_provider = DynamicProvider(
    provider_name = "product_detail",
    elements = product_details_list,
)

company_list_per_product = Company_List_Per_Product

fake = Faker()

fake.add_provider(product_details_provider)

num_products = 10000  # Adjust as needed

products = []

for _ in range(num_products):
    product_id = f'PROD{"{:05d}".format(_)}'                                    # Added leading zeros
    product_detail = fake.product_detail()                                      # Store the random product detail
    product_name = product_detail['product name']                               # Get the product name
    category = product_detail['category']                                       # Get the category
    subcategory = product_detail['subcategory']                                 # Get the subcategory
    manufacturer = fake.random_element(company_list_per_product[product_name])  # Get the company name based on product name
    unit_cost = float(product_detail['unit price']) + random.randint(0, 20)     # Get random unit price
    products.append([product_id, product_name, category, subcategory, manufacturer, unit_cost])

products_df = pd.DataFrame(products, columns=['ProductID', 'ProductName', 'Category', 'Subcategory', 'Manufacturer', 'UnitCost'])
products_df.to_csv('product_details.csv', index=False)
