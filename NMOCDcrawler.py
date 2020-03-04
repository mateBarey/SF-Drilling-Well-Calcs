from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
from bs4 import BeautifulSoup
import requests
import time
import numpy as np 
import os
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

class Scraper():
    def __init__(self,wellfile,driver_file,chrome_file,path):
        self.wellfile = wellfile
        self.driver_file = driver_file
        self.chrome_file = chrome_file
        self.path = path


    def api_arr_generator(self):
        df = pd.read_excel(self.wellfile)
        df = df['API #'].dropna()
        arr_new = df.to_numpy()
        arr_new2 = [str(int(el)) + '0000' for el in arr_new]
        return arr_new2

    def crawler(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-impl-side-painting")
        chrome_options.add_argument("--disable-no-sandbox")
        chrome_options.add_argument("--disable-seccomp-filter-sandbox")
        chrome_options.add_argument("--disable-breakpad")
        chrome_options.add_argument("--disable-client-side-phishing-detection")
        chrome_options.add_argument("--disable-cast")
        chrome_options.add_argument("--disable-cast-streaming-hw-encoding")
        chrome_options.add_argument("--disable-cloud-import")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--disable-session-crashed-bubble")
        chrome_options.add_argument("--disable-ipv6")
        chrome_options.add_argument("--allow-http-screen-capture")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument('window-size=1200x600')
        #chrome_options.add_argument('--disable-dev-shm-usage')        
        chrome_options.binary_location = self.chrome_file
        chromedriver = self.driver_file
        driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chromedriver)
        i = 0
        link_hash = {}
        api_arr_names_for_pdf_download = self.api_arr_generator()
        for api_name in api_arr_names_for_pdf_download:
            address = 'http://ocdimage.emnrd.state.nm.us/imaging/WellFileView.aspx?RefType=WF&RefID=' + str(api_name)
            driver.get(address)
            #time.sleep(2)
            '''
            need to fix this part only downloading first file for some stuff

            try to see first if its getting more then 1 element for pdf links
            '''
            #driver.find_elements_by_xpath('//*[@id="dlFiles"]/tbody/tr[1]')
            imageLinks = driver.find_elements_by_css_selector('a')
            imageNames = []
            for el in imageLinks:
                imageNames.append(el.get_attribute("href"))
            str1 = '.pdf'
            link_arr = []
            for el2 in imageNames:
                if str1 in el2:
                    link_arr.append(el2)
            link_hash[api_name] = link_arr

        for k,v in link_hash.items():
            os.chdir(self.path)
            if os.path.exists(k):
                os.chdir(k)
            os.makedirs(k)
            os.chdir(k)
            url_arr_length = len(v)
            i = 0
            for url in link_hash[k]:
                try:
                    r = requests.get(url, timeout=30, verify = False)
                    r.raise_for_status()
                    name = url.split('/')[-1].replace('0000','')
                    with open(str(name),"wb") as pdf:
                        pdf.write(r.content)
                    pdf.close()      
                    if i == (url_arr_length - 1): 
                        pdf_names = os.listdir(os.path.realpath('.'))
                        merger = PdfFileMerger()
                        for pdf_file in pdf_names:
                            with open(pdf_file, 'rb') as pdf:
                                merger.append(PdfFileReader(pdf))
                            if os.path.exists(pdf_file): os.remove(pdf_file)
                        merg_str = ((os.getcwd().split('\\')[-1]) + 'merged '+'.pdf')
                        merger.write(merg_str)
                        merger.close()
                    break
                except:
                    print("Connection refused by the server..")
                    print("Let me sleep for 5 seconds")
                    print("ZZzzzz...")
                    time.sleep(5)
                    print("Was a nice sleep, now let me continue...")
                    continue                  
                i += 1
        print('Finished downloading Well Pdfs')


if __name__ =="__main__":
    # change this to a default blank well inventory with random api's using qgis etc..
    file_1 = r"C:\Users\pinochhio\Documents\Well INV Template.xlsx"
    file_2 = r'C:\Users\pinochhio\Desktop\work\Main Project\chromedriver.exe'
    file_3 = r"C:\Users\pinochhio\Desktop\work\Main Project\chrome-win\chrome.exe"
    file_4 = r'C:\Users\pinochhio\Documents\test3'
    arr_scraper_obj = Scraper(file_1, file_2, file_3,file_4)
    scraper = arr_scraper_obj.crawler()
    print(scraper)