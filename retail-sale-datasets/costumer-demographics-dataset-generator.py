import pandas as pd
import random
from faker import Faker
import gender_guesser.detector as gender
from costumer_demographics import Locations

fake = Faker()

gender_type = gender.Detector()

locations = Locations

num_customers = 10000  # Adjust as needed

customers = []

for _ in range(num_customers):
    customer_id = f'CUST{"{:05d}".format(_)}'                           # Added leading zeros
    name = fake.unique.name()                                           # Generate a fake name
    age = random.randint(18, 70)                                        # Generate a random age
    gender = gender_type.get_gender(name.split()[0]).capitalize()       # Get the gender of first name at index 0
    if gender == 'Unknown':                                             # Leading title like Dr., Mrs, etc
        gender = gender_type.get_gender(name.split()[1]).capitalize()   # Get the gender of first name at index 1

    if gender == 'Mostly_female':                                       # If returns 'Mostly_female
        gender = 'Female'                                               # Set to 'Female'
    elif gender == 'Mostly_male':                                       # If returns 'Mostly_male
        gender = 'Male'                                                 # Set to 'Male'
    # location = fake.city()                                              # Generate a fake city
    location = fake.random_element(locations)
    membership_type = fake.random_element(['Silver', 'Gold', 'Platinum'])
    customers.append([customer_id, name, age, gender, location, membership_type])

customers_df = pd.DataFrame(customers, columns=['CustomerID', 'Name', 'Age', 'Gender', 'Location', 'MembershipType'])
customers_df.to_csv('customer_demographics.csv', index=False)
