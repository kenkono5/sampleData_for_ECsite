import csv
from faker import Faker
import datetime
import random

def customerDataGenerate(records, headers):
    fake = Faker('ja_JP')
    gender = ["男", "女"]
    age = [20, 30, 40]
    rank = ["S", "A", "B", "C"]
    with open("customer_data.csv", 'wt') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        for i in range(records):
            writer.writerow({
                    "Name": fake.name(),
                    "Gender": random.choice(gender),
                    "Buy": random.randint(100, 5000),
                    "Age": random.choice(age),
                    "Prefecture" : fake.prefecture(),
                    "City" : fake.city(),
                    "Rank": random.choice(rank),
                    })
    
if __name__ == '__main__':
    records = 10
    headers = ["Name", "Buy", "Gender", "Age", "Prefecture", "City", "Rank",]
    customerDataGenerate(records, headers)
    print("CSV generation complete!")
