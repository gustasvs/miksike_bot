from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from settings import *
import time
driver = webdriver.Chrome(webdriver_pth)
driver.get("https://miksike.lv/")

driver.switch_to.frame("mytop")
driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td[3]/table/tbody/tr/td[2]/input[1]').send_keys(uname) # username
# driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td[3]/table/tbody/tr/td[2]/input[1]').send_keys('pauls123321') # username
driver.find_element_by_xpath("""/html/body/table/tbody/tr[1]/td[3]/table/tbody/tr/td[2]/input[2]""").send_keys(passw) # password
driver.find_element_by_xpath("""/html/body/table/tbody/tr[1]/td[3]/table/tbody/tr/td[2]/input[3]""").click() # login poga
driver.find_element_by_xpath("""//*[@id="prangling"]""").click() # rekini galva
time.sleep(1)
driver.switch_to.default_content()
driver.switch_to.frame("myleft")
driver.find_element_by_xpath("""//*[@id="div_Treniņa vieta"]""").click() # trenina vieta
time.sleep(1)
driver.switch_to.default_content()
driver.switch_to.frame("mycontent")
if mode == "sprint":
    driver.find_element_by_xpath("""/html/body/table/tbody/tr[2]/td[1]/table/tbody/tr[9]/td[3]/a""").click() # sprint kkas
if mode == "division":
    driver.find_element_by_xpath("""/html/body/table/tbody/tr[2]/td[1]/table/tbody/tr[7]/td[2]/a""").click() # dalisana
if mode == "addition":
    driver.find_element_by_xpath("""/html/body/table/tbody/tr[2]/td[1]/table/tbody/tr[1]/td[2]/a""").click() # saskaitisana
#driver.get("https://miksike.lv/en/mmath.html?mode=nat&ex=1&sprint=1&ekrh=1080")

driver.switch_to.window(driver.window_handles[1])

driver.find_element_by_xpath("""//*[@id="btnAlusta"]""").click()
lol = driver.find_element_by_id("txtTehtav")
nr1 = driver.find_element_by_xpath("""//*[@id="nr1"]""")
nr2 = driver.find_element_by_xpath("""//*[@id="nr2"]""")
nr3 = driver.find_element_by_xpath("""//*[@id="nr3"]""")
nr4 = driver.find_element_by_xpath("""//*[@id="nr4"]""")
nr5 = driver.find_element_by_xpath("""//*[@id="nr5"]""")
nr6 = driver.find_element_by_xpath("""//*[@id="nr6"]""")
nr7 = driver.find_element_by_xpath("""//*[@id="nr7"]""")
nr8 = driver.find_element_by_xpath("""//*[@id="nr8"]""")
nr9 = driver.find_element_by_xpath("""//*[@id="nr9"]""")
nr0 = driver.find_element_by_xpath("""//*[@id="nr0"]""")
ok = driver.find_element_by_xpath("""//*[@id="OK"]""")

maxsuma = 9999999

while True:
    cipari = []
    res = 0
    suma = maxsuma
    zime = '+'
    for e in lol.text:
        if e.isdigit():
            res = int(str(res) + str(e))
        else:
            print(e)
            if e == '+':
                zime = '+'
                suma = 0
            if e == '-':
                zime = '-'
            if e == ':':
                zime = ':'
            if e == 'x':
                zime = 'x'
            cipari.append(res)
            res = 0
    for skaitlis in cipari:
        if zime == '+':
            suma += int(skaitlis)
        if zime == '-':
            if suma == maxsuma:
                suma = int(skaitlis)
            else:
                suma -= int(skaitlis)
        if zime == ':':
            if suma == maxsuma:
                suma = int(skaitlis)
            else:
                suma //= int(skaitlis)
        if zime == 'x':
            if suma == maxsuma:
                suma = int(skaitlis)
            else:
                suma *= int(skaitlis)
    for y in str(suma):
        #print(y)
        #time.sleep(1)
        if y == "1":
            nr1.click()
        if y == "2":
            nr2.click()
        if y == "3":
            nr3.click()
        if y == "4":
            nr4.click()
        if y == "5":
            nr5.click()
        if y == "6":
            nr6.click()
        if y == "7":
            nr7.click()
        if y == "8":
            nr8.click()
        if y == "9":
            nr9.click()
        if y == "0":
            nr0.click()

    ok.click()
    time.sleep(0.4)
