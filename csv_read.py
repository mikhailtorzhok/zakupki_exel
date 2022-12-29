import csv
#Ur_list = []
#Fiz_list = []
#Trash_list = []
Ur_dictionary = {}
Fiz_dictionary = {}
Trash_dictionary = {}


with open('Корреспонденты.csv') as f:
    Ur_list = []
    Fiz_list = []
    Trash_list = []
    reader = csv.DictReader(f)
    i=0
    for row in reader:
        print(row)
        i+=1
        print(row['ВидКорреспондента'])
        if row['ВидКорреспондента'] == 'Юридическое лицо':
            print('add to Ur.csv')
            Ur_dictionary = row
            Ur_list.append(Ur_dictionary)
        elif row['ВидКорреспондента'] == 'Физическое лицо':
            print('add to Fiz.csv')
            Fiz_dictionary = row
            Fiz_list.append(Fiz_dictionary)
            #i+=1
            #if i>2:
            #    break
        else:
            print('add to NotValid.csv')
            Trash_dictionary = row
            Trash_list.append(Trash_dictionary)
            #i+=1
            #if i>2:
            #    break
        if i>400:
            print('Ur_list = ')
            print(Ur_list) 
            print('Fiz_list = ')
            print(Fiz_list)
            print('Trash_list = ')
            print(Trash_list)
            break
   




def write_Ur(data):
    with open('csv_write_Ur.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=list(data[0].keys()), quoting=csv.QUOTE_NONNUMERIC)
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