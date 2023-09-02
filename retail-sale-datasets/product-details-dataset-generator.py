import pandas as pd
from faker import Faker
from faker.providers import DynamicProvider

from product_details import Product_Details

product_details_list = Product_Details

product_details_provider = DynamicProvider(
    provider_name = "product_detail",
    elements = product_details_list,
)

fake = Faker()

fake.add_provider(product_details_provider)

num_products = 500  # Adjust as needed

products = []

for _ in range(num_products):
    product_id = f'PROD{"{:05d}".format(_)}'            # Added leading zeros
    product_detail = fake.product_detail()              # Store the random product detail
    product_name = product_detail['product name']       # Get the product name
    category = product_detail['category']               # Get the category
    subcategory = product_detail['subcategory']         # Get the subcategory
    manufacturer = fake.company()                       # Generate fake company name
    unit_cost = product_detail['unit price']            # Get the unit price
    products.append([product_id, product_name, category, subcategory, manufacturer, unit_cost])

products_df = pd.DataFrame(products, columns=['Product ID', 'Product Name', 'Category', 'Subcategory', 'Manufacturer', 'Unit Cost'])
products_df.to_csv('product_details.csv', index=False)
