import csv
from faker import Faker
import datetime
import random

fake = Faker()

start_date = datetime.date(year=2019, month=1, day=1)
end_date = datetime.date(year=2019, month=12, day=31)

def customerDataGenerate(records, customerHeaders):
  fake = Faker('ja_JP')
  gender = ["男", "女"]
  age = [20, 30, 40]
  rank = ["S", "A", "B", "C"]
  with open("customer_data.csv", 'wt') as csvFile:
    writer = csv.DictWriter(csvFile, fieldnames=customerHeaders)
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

def storeDataGenerate(records, storeHeaders):
  stores = ["a", "b", "c", "d", "e"]
  with open("store_data.csv", 'wt') as csvFile:
    writer = csv.DictWriter(csvFile, fieldnames=storeHeaders)
    writer.writeheader()
    for i in range(records):
      writer.writerow({
        "Store": random.choice(stores),
        "Date": fake.date_between(start_date=start_date, end_date=end_date),
        "Visit": random.randint(0, 100),
        })

if __name__ == '__main__':
  records = 10000
  customerHeaders = ["Name", "Buy", "Gender", "Age", "Prefecture", "City", "Rank"]
  customerDataGenerate(records, customerHeaders)

  storeHeaders = ["Store", "Date", "Visit"]
  storeDataGenerate(records, storeHeaders)
  print("CSV generation complete!")
