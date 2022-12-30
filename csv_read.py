import csv
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
#from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


Ur_list = []
Fiz_list = []
Trash_list = []
Ur_dictionary = {}
Fiz_dictionary = {}
Trash_dictionary = {}


def main():
    print("Hello World!")
    #driver = webdriver.Firefox()
    firefox_options = Options()
    #firefox_options.set_headless()
    driver = webdriver.Firefox(options=firefox_options)
    driver.get("https://torsed.voskhod.ru/app/#!")
    #login_input = driver.find_element_by_class_name("v-textfield v-widget username-field v-textfield-username-field v-has-width v-textfield-prompt")
    #login_input = driver.find_element(By.NAME, "v-verticallayout v-layout v-vertical v-widget cuba-login-bottom v-verticallayout-cuba-login-bottom v-has-width")
    #login_input = driver.find_element(By.xpath("//div/span"))
    #login_input = driver.find_elements(By.XPATH, '//input') 
    #login_input = driver.find_elements(By.XPATH, '//div')
    #login_input = driver.find_elements(By.XPATH, '//input') 
    #print(login_input)    
    #login_input.send_keys("emailid@lambdatest.com")
    
    delay = 3 # seconds
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//input')))
        print ("Page is ready!")
        login_input = driver.find_elements(By.XPATH, '//input')
        print(login_input) 
        login_input[0].send_keys("emailid@lambdatest.com")
    except TimeoutException:
        print ("Loading took too much time!")
    


def write_csv(data, name):
    with open(name, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=list(data[0].keys()), extrasaction='ignore', delimiter = ',', quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        for d in data:
            writer.writerow(d)
        return


def split_main_csv_to_3(name='Корреспонденты.csv'):

    with open('Корреспонденты.csv') as f:
        #Ur_list = []
        #Fiz_list = []
        #Trash_list = []
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
              ##if i>400:
        print('Ur_list = ')
        print(Ur_list) 
        write_csv(Ur_list, 'csv_write_Ur.csv')
        print('Fiz_list = ')
        print(Fiz_list)
        write_csv(Fiz_list, 'csv_write_Fiz.csv')
        print('Trash_list = ')
        print(Trash_list)
        write_csv(Trash_list, 'csv_write_Trash.csv')
                ##break
        return


if __name__ == "__main__":
    main()



   
    ##reader = csv.reader(f)
    ##headers = next(reader)
    ##print('Headers: ', headers)
    ##firstRow = next(reader)
    ##print('firstRow: ', firstRow)
    ##for row in reader:
        ##print(row)