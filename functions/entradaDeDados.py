# -*- coding: utf-8 -*-
"""
Created on Tue May 25 16:21:27 2021

@author: Carlos Alberto
"""

from bs4 import BeautifulSoup
from selenium import webdriver
import time
import json
    
def minerarOsDadosDoBotao(url):
     
    options = webdriver.ChromeOptions()
    #options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path='C:\\Users\\Carlinhos\\Downloads\\chromedriver.exe', chrome_options=options)
    #driver = webdriver.Chrome(chrome_options=options)
    #driver = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.CHROME)

    driver.get(url)
    time.sleep(5)
    
    
    tagLastPage = driver.find_element_by_xpath('//a[@ng-switch-when="last"]')
    html_LastPage = tagLastPage.get_attribute('outerHTML')
    soup_LastPage = BeautifulSoup(html_LastPage, 'html.parser')
    numberLastPage = int(soup_LastPage.find(name = 'span').text)
    
    listDocuments = []
     
    for page in range(numberLastPage):
        buttons_Detalhes = driver.find_elements_by_xpath('//button[@ng-click="buscarEstabalecimento(estab.id)"]')      
        
        for open_Detalhes in buttons_Detalhes:
            open_Detalhes.click()
            
            time.sleep(2)
            
            form = driver.find_element_by_xpath('//*[@id="dadosBasicosModal"]//*[@class = "ng-pristine ng-valid"]')
            html_form = form.get_attribute('outerHTML')
            soup_form = BeautifulSoup(html_form, 'html.parser')
            documentFinal = {}
            
            for children in soup_form.select('div[class*=col-md-]'):
                 
                fieldName = children.find(name='label').text
                if fieldName != 'Dia semana':
                    content = children.find('input').get('value')
                    document = {fieldName:content}
                    documentFinal.update(document)
                
            listDocuments.append(documentFinal)
            close_Detalhes = driver.find_element_by_xpath('//*[@id="dadosBasicosModal"]//div[@class="modal-content"]//button[@class="btn btn-primary"]')
            close_Detalhes.click()
            time.sleep(1)
            
        button_NextPage = driver.find_element_by_xpath('//a[@ng-switch-when="next"]')
        button_NextPage.click()
        print(page + 1, 'paginas lidas')
        
    driver.quit()
    
    return listDocuments



