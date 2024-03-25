import pandas as pd

read_excel_file = pd.read_excel('./file.xlsx')
mobile_phone_en = read_excel_file['mobile phone']
mobile_phone_per = read_excel_file['تلفن همراه']
print(mobile_phone_en)
print(mobile_phone_per)

