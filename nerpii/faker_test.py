import csv
from faker import Faker

fake = Faker('en_US')  # English locale for more relevant data

output_file = 'random_data.csv'

fields = [
    "First Name", "Last Name", 
    "Postal Code", "Phone Number", 
    "Social Security Number", "Email"
]

num_records = 100

with open(output_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(fields)  
    
    for _ in range(num_records):
        writer.writerow([
            fake.first_name(),
            fake.last_name(),
            fake.postcode(),
            fake.phone_number(),
            fake.ssn(),  
            fake.email()
        ])

print(f"CSV file '{output_file}' with {num_records} random records created successfully.")
