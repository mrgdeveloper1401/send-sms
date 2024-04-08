combined_list = [('mohammad', '09391640664'), ('ali', '09930650711')]
print(len(combined_list))
while combined_list:
    full_name, mobile = combined_list.pop(0)
    print(full_name, mobile)


