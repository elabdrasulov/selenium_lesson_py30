import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
# service = Service(executable_path='/home/user/chromedriver/')

options = Options()
# options.page_load_strategy = 'eager' 'normal' 'none'
# options.add_argument('user-agent=MakersBootcamp')
options.add_argument('user-data-dir=/home/ljazz/SeleniumProfile')

driver = webdriver.Chrome(service=service, options=options)

try:
    # for i in range(1,6):
    #     driver.get(f'https://www.kinopoisk.ru/lists/movies/top250/?page={i}')
    #     with open(f'films250_{i}', 'w') as f:
    #         f.write(driver.page_source)
    #         time.sleep(2)
    driver.get('https://google.com')
    # driver.get('https://www.whatismybrowser.com/detect/what-is-my-user-agent/')
    # driver.get_screenshot_as_file('1.png')
    google_form = driver.find_element(By.ID, 'APjFqb')
    google_form.send_keys('Makers')
    time.sleep(2)
    google_form.send_keys(Keys.ENTER)
    
    elem = driver.find_element(By.XPATH, '//*[@id="pnnext"]/span[2]')
    
    # print(elem.get_attribute('style'))
    time.sleep(2)
    
    driver.execute_script("arguments[0].scrollIntoView(true);", elem)
    # driver.execute_script("window.scrollBy(0,1000);")
    
    
    time.sleep(3)
    
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()