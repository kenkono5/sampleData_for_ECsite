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

def categoryDataGenerate(records, categoryHeaders):
  categorys = ["日用品", "医薬品", "食品", "衛生用品", "化粧品"]
  with open("category_data.csv", 'wt', encoding='utf_8_sig') as csvFile:
    writer = csv.DictWriter(csvFile, fieldnames=categoryHeaders)
    writer.writeheader()
    id = 1
    for i in categorys:
      writer.writerow({
        "CategoryID": id,
        "Category": i,
        })
      id+=1

if __name__ == '__main__':
  category_records = 1000
  categoryHeaders = ["CategoryID", "Category"]
  categoryDataGenerate(category_records, categoryHeaders)

  print("CSV generation complete!")
