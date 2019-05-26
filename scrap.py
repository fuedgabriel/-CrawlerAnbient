from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time


def click(xp):
    driver.find_element(By.XPATH, xp).click()      


options = Options()
options.headless = False
driver = webdriver.Firefox(options=options)
driver.get('https://www.anbient.com/anime/lista')
time.sleep(5)



x = 1
for ranger in range(1, 27):
    print("Range is:" + str(ranger))
    click('/html/body/main/main/div[2]/div/div/ul/li['+str(ranger)+']') 
    while(True):    
        name = "//*[@id=\"lista-de-animes\"]/table/tbody/tr["+str(x)+"]/td[2]/a"
        ep = "//*[@id=\"lista-de-animes\"]/table/tbody/tr["+str(x)+"]/td[3]"
        try:
            nome = driver.find_element(By.XPATH, name).text
        except:
            break
        link = driver.find_element(By.XPATH, name).get_attribute('href')
        epi = driver.find_element(By.XPATH, ep).text
        print("link: "+link)
        print("Nome: "+nome)
        print("Episodeos: "+epi)
        print("____________________________________")
        print("")
        print("")
        x+=1

driver.quit()


