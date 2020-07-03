from faker import Faker
import csv
import datetime
import random

fake = Faker()

start_date = datetime.date(year=2019, month=6, day=1)
end_date = datetime.date(year=2019, month=6, day=30)

def customerDataGenerate(records, customerHeaders):
  fake = Faker('ja_JP')
  gender = ["男", "女"]
  age = [20, 30, 40]
  prefecture = ["東京", "埼玉", "神奈川", "千葉"]
  rank = ["S", "A", "B", "C"]
  with open("customer_data.csv", 'wt', encoding='utf_8_sig') as csvFile:
    writer = csv.DictWriter(csvFile, fieldnames=customerHeaders)
    writer.writeheader()
    for _ in range(records):
      writer.writerow({
        "Name": fake.name(),
        "Gender": random.choice(gender),
        "Buy": random.randint(100, 5000),
        "Age": random.choice(age),
        "Prefecture" : random.choice(prefecture),
        "Rank": random.choice(rank),
        })

def storeDataGenerate(records, storeHeaders):
  stores = ["オンラインストア", "トモズ 秋葉原店", "トモズ 大手町 カンファレンスセンター店", "トモズ 大手町プレイス店", "トモズ KITTE店", "トモズ 東京ミッドタウン日比谷店", "トモズ 神田和泉町店"]
  w = [2, 1, 1, 1, 1, 1, 1]
  stores_weight = random.choices(stores, k = records, weights = w)
  with open("store_data.csv", 'wt', encoding='utf_8_sig') as csvFile:
    writer = csv.DictWriter(csvFile, fieldnames=storeHeaders)
    writer.writeheader()
    for i in range(records):
      writer.writerow({
        "Store": stores_weight[i],
        "Date": fake.date_between(start_date=start_date, end_date=end_date),
        "Visit": random.randint(0, 100),
        })

if __name__ == '__main__':
  customer_records = 100000
  customerHeaders = ["Name", "Buy", "Gender", "Age", "Prefecture", "Rank"]
  customerDataGenerate(customer_records, customerHeaders)

  store_records = 1000
  storeHeaders = ["Store", "Date", "Visit"]
  storeDataGenerate(store_records, storeHeaders)
  print("CSV generation complete!")
