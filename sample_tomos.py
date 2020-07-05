from faker import Faker
import csv
import datetime
import random

fake = Faker()

start_date = datetime.date(year=2019, month=6, day=1)
end_date = datetime.date(year=2019, month=6, day=30)

start = str(20190601)
end = str(20190630)
start_dt = datetime.datetime.strptime(start, "%Y%m%d")
end_dt = datetime.datetime.strptime(end, "%Y%m%d")
lst = []
t = start_dt
while t <= end_dt:
    lst.append(t)
    t += datetime.timedelta(days=1)
month_array = [x.strftime("%Y-%m-%d") for x in lst]

def customerDataGenerate(records, customerHeaders):
  fake = Faker('ja_JP')
  gender = ["男", "女"]
  age = [20, 30, 40, 50, "60以上"]
  w_age_number = [1, 3, 1, 2, 1]
  w_age = random.choices(age, k = records - 1, weights = w_age_number)
  prefecture = ["東京都", "埼玉県", "神奈川県", "千葉県"]
  w_prefecture_number = [3, 2, 1, 1]
  w_prefecture = random.choices(prefecture, k = records - 1, weights = w_prefecture_number)
  rank = ["S", "A", "B", "C"]
  w_rank_number = [1, 1, 2, 3]
  w_rank = random.choices(rank, k = records - 1, weights = w_rank_number)
  id = 1

  with open("customer_data.csv", 'wt', encoding='utf_8_sig') as csvFile:
    writer = csv.DictWriter(csvFile, fieldnames=customerHeaders)
    writer.writeheader()
    for _ in range(records):
      writer.writerow({
        "ID": id,
        "Name": fake.name(),
        "Gender": random.choice(gender),
        "Buy": random.randint(100, 5000),
        "Age": w_age[id - 2],
        "Prefecture" : w_prefecture[id - 2],
        "Rank": w_rank[id - 2],
        })
      id+=1

def storeDataGenerate(records, storeHeaders):
  stores = ["オンラインストア", "トモズ 秋葉原店", "トモズ 大手町 カンファレンスセンター店", "トモズ 大手町プレイス店", "トモズ KITTE店", "トモズ 東京ミッドタウン日比谷店", "トモズ 神田和泉町店"]
  with open("store_data.csv", 'wt', encoding='utf_8_sig') as csvFile:
    writer = csv.DictWriter(csvFile, fieldnames=storeHeaders)
    writer.writeheader()
    for i in stores:
      for j in month_array:
        if i == "オンラインストア":
          writer.writerow({
          "Store": i,
          "Date": j,
          "Visit": random.randint(0, 200)
          })
        else:
          writer.writerow({
          "Store": i,
          "Date": j,
          "Visit": random.randint(0, 100)
          })

if __name__ == '__main__':
  customer_records = 118455
  customerHeaders = ["ID", "Name", "Buy", "Gender", "Age", "Prefecture", "Rank"]
  customerDataGenerate(customer_records, customerHeaders)

  store_records = 1000
  storeHeaders = ["Store", "Date", "Visit"]
  storeDataGenerate(store_records, storeHeaders)
  print("CSV generation complete!")
