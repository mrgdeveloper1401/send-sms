import datetime
import os.path
import pandas as pd
import numpy as np

# import excel file
f = os.path.join('/home/mohammadgoodarzi/Desktop/project-django/send_sms/sms/dataset_excel_ppNZaC6.xlsx')
excel_file = pd.read_excel(f)


# define list
# r = []
# full_name = []
# mobile_phone = []
# birthday = []
# contract = []
# third_party_insurance = []
# rental_insurance = []
# technical_diagnoses = []
#
# for i in excel_file['row']:
#     r.append(i)
#
# for a in excel_file['full_name']:
#     full_name.append(a)
#
# for b in excel_file['mobile_phone']:
#     mobile_phone.append(b)
#
# for c in excel_file['birthday']:
#     birthday.append(c)
#
# for d in excel_file['contract']:
#     contract.append(d)
#
# for e in excel_file['third_party_insurance']:
#     third_party_insurance.append(e)
#
# for f in excel_file['rental_insurance']:
#     rental_insurance.append(f)
#
# for j in excel_file['technical_diagnoses']:
#     technical_diagnoses.append(j)

# define dictionary
# data = {
#     'row': r,
#     'full_name': full_name,
#     'contract': contract,
#     'birthday': birthday,
#     'third_party_insurance': third_party_insurance,
#     'rental_insurance': rental_insurance,
#     'technical_diagnoses': technical_diagnoses
# }

mohammad_birthday = datetime.date(year=2001, month=1, day=1)
# counter = 0
#


# birthday = excel_file['birthday'].loc[0]
# print(birthday)
# print(birthday == mohammad_birthday)
# print(birthday.month, birthday.day)
# print(mohammad_birthday.month, mohammad_birthday.day)
# if mohammad_birthday.month == birthday.month and mohammad_birthday.day == birthday.day:
#     print('happy birthday')
# else:
#     print('not happy birthday')

birthday = excel_file['birthday']
counter = 0
for b in birthday:
    if mohammad_birthday.month == b.month and mohammad_birthday.day == b.day:
        print(f'today is {b} and happy birthday')
        counter += 1
    else:
        print(f'today is {b} is not happy birthday')


print(excel_file.loc[counter - 1])
