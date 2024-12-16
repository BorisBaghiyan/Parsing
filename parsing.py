# import undetected_chromedriver as uc
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver.chrome.options import Options
# from fake_useragent import UserAgent
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys


# user_agent = UserAgent()

# options = uc.ChromeOptions()
# options.add_argument(f'user-agent={user_agent.random}')

# driver = uc.Chrome(options=options)

# try:
#     driver.get(url='https://www.list.am/')
#     time.sleep(3)
#     driver.find_element(By.CSS_SELECTOR, '#dlgLangSel > div.bar > a:nth-child(1)').click()
#     time.sleep(3)
#     driver.find_element(By.CSS_SELECTOR, '#hcontent > div.stripc > div:nth-child(2) > a').click()
#     time.sleep(3)
#     driver.find_element(By.CSS_SELECTOR, '#main > div.catms > div > div:nth-child(2) > a').click()
#     time.sleep(3)
#     driver.find_element(By.CSS_SELECTOR, '#ff > div:nth-child(4) > div > div.co4 > div.me').click()
#     time.sleep(3)
#     driver.find_element(By.CSS_SELECTOR, '#ff > div:nth-child(4) > div > div.co4 > div.l > div:nth-child(12)').click()
#     time.sleep(3)
#     driver.find_element(By.CSS_SELECTOR, '#idprice1').click()
#     time.sleep(3)
#     driver.find_element(By.CSS_SELECTOR, '#idprice1').send_keys("10000")
#     time.sleep(3)
#     driver.find_element(By.CSS_SELECTOR, '#idprice2').click()
#     time.sleep(3)
#     driver.find_element(By.CSS_SELECTOR, '#idprice2').send_keys("20000",Keys.ENTER)
#     time.sleep(3)
#     driver.find_element(By.CSS_SELECTOR, '#pagecol > div.content-container > div.dlbar > div > div').click()
#     time.sleep(3)
#     driver.find_element(By.CSS_SELECTOR, '#pagecol > div.content-container > div.dlbar > div > div > select > option:nth-child(2)').click()
#     time.sleep(3)
#     driver.find_element(By.CSS_SELECTOR, '#tp > div.dl > div > a:nth-child(6)').click()
#     time.sleep(3)
#     driver.find_element(By.CSS_SELECTOR, '#abar > div > span.price.x').click()
#     time.sleep(3)

#     price_list = []
#     index = 1

#     while True:
#         try:
#             price = driver.find_element(By.CSS_SELECTOR, f'#abar{index}').text
#             time.sleep(1)
#             price_list.append(price)
#             index += 1
#         except:
#             break
    
#     print(price_list)

# except Exception as ex:
#     print(ex.__class__.__name__)
# finally:
#     driver.close()
#     driver.quit()