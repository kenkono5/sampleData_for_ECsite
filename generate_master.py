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

def categoryDataGenerate(categoryHeaders):
  categorys = ["日用品", "医薬品", "食品", "衛生用品", "化粧品"]
  with open("csv/category_data.csv", 'wt', encoding='utf_8_sig') as csvFile:
    writer = csv.DictWriter(csvFile, fieldnames=categoryHeaders)
    writer.writeheader()
    id = 1
    for i in categorys:
      writer.writerow({
        "CategoryID": id,
        "Category": i,
        })
      id+=1

def prefectureDataGenerate(prefectureHeaders):
  prefectures = ['北海道', '青森県', '岩手県', '宮城県', '秋田県', '山形県', '福島県', '茨城県', '栃木県', '群馬県', '埼玉県', '千葉県', '東京都', '神奈川県', '新潟県', '富山県', '石川県', '福井県', '山梨県', '長野県', '岐阜県', '静岡県', '愛知県', '三重県', '滋賀県', '京都府', '大阪府', '兵庫県', '奈良県', '和歌山県', '鳥取県', '島根県', '岡山県', '広島県', '山口県', '徳島県', '香川県', '愛媛県', '高知県', '福岡県', '佐賀県', '長崎県', '熊本県', '大分県', '宮崎県', '鹿児島県', '沖縄県']
  with open("csv/prefecture_data.csv", 'wt', encoding='utf_8_sig') as csvFile:
    writer = csv.DictWriter(csvFile, fieldnames=prefectureHeaders)
    writer.writeheader()
    id = 1
    for i in prefectures:
      writer.writerow({
        "PrefectureID": id,
        "Prefecture": i,
        })
      id+=1
def rankDataGenerate(rankHeaders):
  ranks = ["S", "A", "B", "C"]
  with open("csv/rank_data.csv", 'wt', encoding='utf_8_sig') as csvFile:
    writer = csv.DictWriter(csvFile, fieldnames=rankHeaders)
    writer.writeheader()
    id = 1
    for i in ranks:
      writer.writerow({
        "RankID": id,
        "Rank": i,
        })
      id+=1

def customerDataGenerate(records, customerHeaders):
  fake = Faker('ja_JP')
  with open("csv/customer_data.csv", 'wt', encoding='utf_8_sig') as csvFile:
    writer = csv.DictWriter(csvFile, fieldnames=customerHeaders)
    writer.writeheader()
    id = 1
    for _ in range(records):
      writer.writerow({
        "CustomerID": id,
        "Name": fake.name(),
        "Address": fake.address(),
        })
      id+=1

if __name__ == '__main__':
  categoryHeaders = ["CategoryID", "Category"]
  categoryDataGenerate(categoryHeaders)

  prefectureHeaders = ["PrefectureID", "Prefecture"]
  prefectureDataGenerate(prefectureHeaders)

  rankHeaders = ["RankID", "Rank"]
  rankDataGenerate(rankHeaders)

  customer_records = 1000
  customerHeaders = ["CustomerID", "Name", "Address"]
  customerDataGenerate(customer_records, customerHeaders)

  print("CSV generation complete!")
