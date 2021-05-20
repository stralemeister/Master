from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import argparse
from netaddr import IPNetwork
import csv

ip_list = []
rep_list = []
def check_ips(ips):
    x = ips
    x = list(dict.fromkeys(x))
    driver = webdriver.Chrome(executable_path=r"C:\Users\strahinja.soskic\Desktop\BackUP\Programiranje\Python\chromedriver.exe")
    for i in range(len(x)):
        url = 'https://mxtoolbox.com/SuperTool.aspx?action=blacklist%3a' + str(ip[i]) + '&run=toolpage'
        driver.get(url)
        time.sleep(10)
    
        element = driver.find_elements_by_xpath('/html/body/form/div[3]/div[2]/div[2]/div/div[2]/div[2]/span/div[1]/div[3]/strong[3]')                                       
        element_text = element[0].text
        
        ip_list.append(ip[i])
        rep_list.appemd(element_text)

        #doradi ovo, neka se provere sve IP adrese i neka se i one vrate f-iji
        #
        #
        #
        #


#print(niz1)
#print(niz2)


