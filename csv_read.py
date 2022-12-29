import csv
Ur_dictionary = {}
Fiz_dictionary = {}
Trash_dictionary = {}


with open('Корреспонденты.csv') as f:
    reader = csv.DictReader(f)
    i=0
    for row in reader:
        print(row)
        print(row['ВидКорреспондента'])
        if row['ВидКорреспондента'] == 'Юридическое лицо':
            print('add to Ur.csv')
        elif row['ВидКорреспондента'] == 'Физическое лицо':
            print('add to Fiz.csv')
            #i+=1
            #if i>2:
            #    break
        else:
            print('add to NotValid.csv')
            #i+=1
            #if i>2:
            #    break
   




def write_Ur(data):
    with open('csv_write_Ur.csv', 'w') as f:
    writer = csv.DictWriter(
        f, fieldnames=list(data[0].keys()), quoting=csv.QUOTE_NONNUMERIC)
    writer.writeheader()
    for d in data:
        writer.writerow(d)
    return

   
    ##reader = csv.reader(f)
    ##headers = next(reader)
    ##print('Headers: ', headers)
    ##firstRow = next(reader)
    ##print('firstRow: ', firstRow)
    ##for row in reader:
        ##print(row)