import csv
import config
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time 
import signal

timedelay=0.3
Ur_list = []
Fiz_list = []
Trash_list = []
Ur_dictionary = {}
Fiz_dictionary = {}
Trash_dictionary = {}


def main():
    print("Hello World!")
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options) 
    driver.set_window_size(1920, 1080)
    driver.get("https://torsed.voskhod.ru/app/#!")

    
    delay = 25 # seconds
    
    login_input = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//input')))
    print ("Page is ready!")
    login_input = driver.find_elements(By.XPATH, '//input')
    print(login_input) 
    login_input[0].send_keys(config.username)
    login_input[1].send_keys(config.password)
            
    button_login = driver.find_element(By.XPATH, '//div[@class="v-button v-widget cuba-login-submit v-button-cuba-login-submit v-has-width"]')
    button_login.click()
    
    button_spravochniki = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[text()="Справочники"]')))
    button_spravochniki = driver.find_element(By.CSS_SELECTOR, "span[class='v-menubar-menuitem']")
    
    print ("Page is ready!")

    button_spravochniki = driver.find_element(By.CSS_SELECTOR, '.cuba-main-menu.v-menubar')

    print ("tab_names " + button_spravochniki.text)
    
    button_spravochniki = driver.find_element(By.CSS_SELECTOR, "div[tabindex='0']")

    button_spravochniki = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/div[1]/div/div/div[3]/div/span[5]")
    action = ActionChains(driver)
    action.move_to_element(button_spravochniki)
    action.click(button_spravochniki)
    action.perform()

    #button_Kontragenty
    find_and_click_element_by_path(driver, delay, '/html/body/div[3]/div[2]/div/div/span[6]/span[1]')
        

    #button_Ur_litca 
    find_and_click_element_by_path(driver, delay, '/html/body/div[3]/div[3]/div/div/span[1]/span[1]')                                                                   
        

    #button_create_new
    #find_and_click_element_by_path(driver, delay, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div/div[3]/div/div[1]/div/div[1]/div/div[1]/div')
        
    #name_input = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[4]/input')))
    #name_input.send_keys('Наименование')
            
    signal.signal(signal.SIGABRT, handler)
    signal.alarm(5)
    while True:
        try:

            read_from_csv_and_write_to_database_Ur(driver, delay, 'Юридическое лицо_temp.csv')

        except Exception as e:
            print(e)
            #driver.get("https://torsed.voskhod.ru/app/#!")
            #driver.back()
            continue
        else:
            print('End of scrypt') 

def handler(signum, frame):
    print("Forever is over!")
    raise Exception("end of time")   
    
def write_name_Ur(name_Ur,driver, delay):
    input = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[4]/input')))
    input.send_keys(name_Ur)
    return

def write_fullname_Ur(fullname_Ur,driver, delay):
    input = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[6]/div/textarea')))
    input.send_keys(fullname_Ur)
    return

def write_telephone_Ur(telephone_Ur,driver, delay):
    input = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[10]/input')))
    input.send_keys(telephone_Ur)
    return

def write_fax_Ur(fax_Ur,driver, delay):
    input = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[12]/input')))
    input.send_keys(fax_Ur)
    return

def write_E_mail_Ur(E_mail_Ur,driver, delay):
    input = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[14]/input')))
    input.send_keys(E_mail_Ur)
    return

def write_site_Ur(site_Ur,driver, delay):
    find_and_click_element_by_path(driver, delay, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[16]/div/div/div[3]/div')
    time.sleep(timedelay)
    input = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[16]/div/div/div[1]/div/a')))
    #/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[16]/div/div/div[1]/div/a
    #/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[16]/div/div/div[1]/div/a/span
    #/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[16]/div/div
    #/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[16]/div/div/div[1]/div/a/span
    #/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[16]/div/div
    #/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[16]/div/div/div[1]/div/a
    #/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[15]
    time.sleep(timedelay)
    input.send_keys(Keys.RETURN)
    input.send_keys(site_Ur)
    input.send_keys(Keys.RETURN)

    return

def write_INN_Ur(INN_Ur,driver, delay):
    input = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[18]/input')))
    input.send_keys(INN_Ur)
    return

def write_KPP_Ur(KPP_Ur,driver, delay):
    input = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[23]/input')))
    input.send_keys(KPP_Ur)
    return

def write_OGRN_Ur(OGRN_Ur,driver, delay):
    input = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[27]/input')))
    input.send_keys(OGRN_Ur)
    return

def write_OKOPF_Ur(OKOPF_Ur,driver, delay):
    try:
        wait = WebDriverWait(driver, 2)
        input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[29]/div/input')))
        input.send_keys(OKOPF_Ur)
        input.send_keys(Keys.RETURN)
        span = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/table/tbody/tr/td/span')))
                                                                                        #/html/body/div[3]/div[2]/div/div[2]/table/tbody/tr/td/span
                                                                                        #/html/body/div[3]/div[2]/div/div[2]/table/tbody/tr[2]/td
        span.click()
    except:
        pass    
    return

def write_Type_Ur(Type_Ur, driver, delay):
    input = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[41]/div[2]/input')))
    input.send_keys('Общественные организации')
    input.send_keys(Keys.RETURN)

    time.sleep(timedelay)
    drop_down_list=WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[41]/div[2]/div')))
    drop_down_list.click()
    #/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[41]/div[2]/div
    time.sleep(timedelay)

    span = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/table/tbody/tr[6]/td/span')))
    
    #/html/body/div[3]/div[2]/div/div[2]/table/tbody/tr[6]/td/span
    #/html/body/div[3]/div[2]/div/div[2]/table/tbody/tr/td/span
    #/html/body/div[3]/div[2]/div/div[2]/table/tbody/tr[2]/td
    #/html/body/div[3]/div[2]/div/div[2]/table/tbody/tr[10]/td
    #/html/body/div[3]/div[2]/div/div[2]/table/tbody/tr[10]/td/span
    #/html/body/div[3]/div[2]/div/div[2]/table/tbody/tr/td/span
    span.click()
    return

def write_place_of_creating(place_of_creating, driver, delay):
    input = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[8]/div[2]/div/div[1]/input')))
    input.send_keys(place_of_creating)
    input.send_keys(Keys.RETURN)
    time.sleep(timedelay)

    find_element = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[8]/div[2]/div/div[3]')))
    #/html/body/div[3]/div[2]/div/div[2]/table/tbody/tr/td/span
    #/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[8]/div[2]/div/div[3]
    find_element.click()
    time.sleep(timedelay)
    button_element_new_page = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div[1]/div')))
    button_element_new_page.click()


    #span = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/table/tbody/tr[1]/td/span')))
    #span = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/table/tbody/tr[1]/td/span')))
    
    #span.click()
    return

def write_Nerezident(nerezident, driver, delay):
    if nerezident == 'Да':
        #print('inside nerezident if')
        find_and_click_element_by_path(driver, delay, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[33]/span/input') 
        #/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[33]/span/input
        #chechbox = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[33]/span/label')))
    elif nerezident == 'Нет':
        pass
    else:
        pass
    return

def write_Postavchick(postavchick, driver, delay):
    if postavchick == 'Да':
        #print('inside postavchick if')
        find_and_click_element_by_path(driver, delay, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[35]/span/input') 
    elif postavchick == 'Нет':
        pass
    else:
        pass
    return

def write_Pokupatel(pokupatel, driver, delay):
    if pokupatel == 'Да':
        #print('inside postavchick if')
        find_and_click_element_by_path(driver, delay, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[37]/span/input') 
    elif pokupatel == 'Нет':
        pass
    else:
        pass
    return

def press_button_OK(driver, delay):
    find_and_click_element_by_path(driver, delay, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/div[1]/div/span/span')
    return

def write_Post_address(address, full_address, driver, delay):
    print('full_address is  ' + full_address)
    #input_address = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div[19]/div/textarea')))
    #input_address = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div[19]/div/textarea')))
    #input_address.send_keys(full_address)
    #input_address.send_keys(Keys.RETURN)

    address_list=address.split()
    for item in address_list:
        try:
            if item.find('Индекс') != -1 :
                #print(item)
                print("INSIDE INDEX")
                index = item.partition('=')[2]
                #print(index)
                input_index = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div[3]/input')))
                input_index.send_keys(index)
                input_index.send_keys(Keys.RETURN)
                time.sleep(timedelay)
                #/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div[3]/input
                #find_and_click_element_by_path(driver, delay, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[37]/span/input') 
            elif item.find('Регион') != -1 :
                #pass
                print("INSIDE REGION")
                region = item.partition('=')[2]
                #print(region)
                region_button_input = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div[5]/div/div/div[2]')))
                region_button_input.click()
                time.sleep(timedelay)
                region_input = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div/div/div/div/div[1]/div/div[3]/input'))) 
                region_input.send_keys(region)
                region_input.send_keys(Keys.RETURN)
                time.sleep(timedelay)            
                region_input_button_inside = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div/div/div/div/div[3]/div/div/div[2]/div[1]'))) 
                #/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div/div/div/div/div[3]/div/div/div[2]/div[1]
                #old_span/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/div/span/span
                #Actions action = new Actions(driver).contextClick(region_input_button_inside).sendKeys(Keys.ARROW_UP).sendKeys(Keys.ENTER)
                #action.build().perform()
                
                action = ActionChains(driver)
                action.move_to_element(region_input_button_inside)
                #action.context_click(on_element = region_input_button_inside)
                action.double_click(on_element = region_input_button_inside)
                action.perform()

                #time.sleep(0.01) 
                #region_select = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div/div/div/div/span/span')))
                #region_select.click()


                
                #region_input_button_inside.click()
                #time.sleep(0.01) 
                #region_input_button_inside.click() 
            #elif item.find('Регион') == -1 :
                #print("Else inside ELIF")
            elif item.find('Город') != -1 :
                #pass
                print("INSIDE GOROD")
                #if item.find('Регион') == -1 :
                    #pass ## ERROR HERE
                    #print("ERROR HERE")
                    #region_button_input = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div[5]/div/div/div[2]')))
                    #/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div[5]/div/div/div[2]
                    #region_button_input.click()
                    #time.sleep(timedelay)
                    #driver.back()
                    #time.sleep(timedelay)
                gorod = item.partition('=')[2]
                gorod_button_input = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div[10]/div/div/div[2]')))
                #/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div[10]/div/div/div[2]
                #/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div[9]/div/div/div[2]
                #/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div[10]/div/div/div[2]
                gorod_button_input.click()

                time.sleep(timedelay)
                gorod_input = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div/div/div/div/div[1]/div/div[3]/input'))) 
                gorod_input.send_keys(gorod)
                gorod_input.send_keys(Keys.RETURN)
                time.sleep(timedelay)            
                gorod_input_button_inside = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div/div/div/div/div[3]/div/div/div[2]/div[1]/div[1]'))) 
            
                action = ActionChains(driver)
                action.move_to_element(gorod_input_button_inside)
                action.double_click(on_element = gorod_input_button_inside)
                action.perform()
            elif item.find('Улица') != -1 :
                #pass
                print("INSIDE Ulitca")
                ulitca = item.partition('=')[2]
                ulitca_button_input = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div[13]/div/div/div[2]')))

                ulitca_button_input.click()

                time.sleep(timedelay)
                ulitca_input = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div/div/div/div/div[1]/div/div[3]/input'))) 

                ulitca_input.send_keys(ulitca)
                ulitca_input.send_keys(Keys.RETURN)
                time.sleep(timedelay)            
                ulitca_input_button_inside = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div/div/div/div/div[3]/div/div/div[2]/div[1]/div[1]'))) 
                #/html/body/div[3]/div[1]/div/div/div[1]/div
                action = ActionChains(driver)
                action.move_to_element(ulitca_input_button_inside)
                action.double_click(on_element = ulitca_input_button_inside)
                action.perform()
            else:
                pass
        except Exception:
            #pass  # or you could use 'continue'
            print('before continue')
            continue
            print('after continue')

    return


def read_from_csv_and_write_to_database_Ur(driver, delay, filename='Юридическое лицо.csv'):
    with open(filename, encoding='utf-8') as f:
        #Ur_list = []
        #Fiz_list = []
        #Trash_list = []
        reader = csv.DictReader(f)
        i=0
        for row in reader:
            print(row)
            #button_create_new
            find_and_click_element_by_path(driver, delay, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div/div[3]/div/div[1]/div/div[1]/div/div[1]/div')
            time.sleep(timedelay)
            i+=1
            #if i == 1:
                #continue
            #print(row['Ссылка'])
            
            
            write_name_Ur(row['Ссылка'],driver, delay)
            time.sleep(timedelay)
            write_fullname_Ur(row['ПолноеНаименование'],driver, delay)
            time.sleep(timedelay)
            write_place_of_creating('Тверская область',driver, delay)
            time.sleep(timedelay)
            write_telephone_Ur(row['ЭлементНомерТелефонаБезКодов'],driver, delay)
            time.sleep(timedelay)
            write_fax_Ur(row['ЭлементНомерТелефона'],driver, delay)
            time.sleep(timedelay)
            write_E_mail_Ur(row['ЭлементДоменноеИмяСервера'],driver, delay)
            time.sleep(timedelay)
            #write_site_Ur(row['Сайт'],driver, delay)
            #time.sleep(timedelay)
            write_INN_Ur(row['ИНН'],driver, delay)
            time.sleep(timedelay)
            write_KPP_Ur(row['КПП'],driver, delay)
            time.sleep(timedelay)
            #write_OGRN_Ur(row['ОГРН'],driver, delay)
            #time.sleep(timedelay)
            #write_OKOPF_Ur(row['КодПоОКПО'],driver, delay)
            #time.sleep(timedelay)

            try:
                write_Post_address(row['ЭлементЗначенияПолей'],row['ЭлементПредставление'],driver, delay)
                time.sleep(timedelay)
            except TimeoutException as e:
                print(e)
                driver.back()
                continue
            
            driver.execute_script("window.scrollTo(0, 1080)")
            time.sleep(timedelay)
         

            write_Type_Ur(row['ВидКорреспондента'],driver, delay) 
            time.sleep(timedelay)
            #write_Nerezident(row['Нерезидент'],driver, delay)
            #time.sleep(timedelay)
            #write_Postavchick(row['Поставщик'],driver, delay)
            #time.sleep(timedelay)
            #write_Pokupatel(row['Покупатель'],driver, delay)
            #time.sleep(timedelay)
            press_button_OK(driver, delay)
            time.sleep(timedelay)
    return


def find_and_click_element_by_path(driver, delay, path):
    button = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, path)))
    action = ActionChains(driver)
    action.move_to_element(button)
    action.click(button)
    action.perform()
    return


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

