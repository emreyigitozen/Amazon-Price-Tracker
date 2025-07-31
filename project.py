from bs4 import BeautifulSoup
import requests
import smtplib
import time           #Kütüphaneler
import datetime
import csv


#Websitesini bağlama
URL='https://www.amazon.com.tr/Under-Armour-Charged-Pursuit-Ayakkab%C4%B1s%C4%B1/dp/B0969278HK/?_encoding=UTF8&pd_rd_w=xiL4E&content-id=amzn1.sym.8366b9e9-4852-434b-af36-c553f69a685e%3Aamzn1.symc.fc11ad14-99c1-406b-aa77-051d0ba1aade&pf_rd_p=8366b9e9-4852-434b-af36-c553f69a685e&pf_rd_r=5P06C660FXN0AEJ1FFW0&pd_rd_wg=BbWof&pd_rd_r=d439f0fd-21ae-4a23-ae33-6cf67d8dd96a&ref_=pd_hp_d_atf_ci_mcx_mr_ca_hp_atf_d&th=1&psc=1'
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"}

page=requests.get(URL,headers=headers)

soup1=BeautifulSoup(page.content,'html.parser')  #URL'nin html kodunu çektik.
soup2=BeautifulSoup(soup1.prettify(),'html.parser') #URL'nin html kodunu daha düzenli hale getirir.
title=soup2.find(id='productTitle').get_text() #Ürünün ismini çektik.
price=soup2.find(class_='a-price-whole').get_text() #Ürünün fiyatını çektik.
title=title.strip() #Gereksiz boşlukları temizledik.
price=price.strip()
bugun=datetime.date.today() #Bugünün tarihi
header=['Title','Price','Date'] #Başlıklar
data=[title,price,bugun] #Veriler


#with open('AmazonWebScraping.csv','w',newline='',encoding='UTF8') as f: #Yeni csv dosyası oluşturduk.
  # writer=csv.writer(f)
  # writer.writerow(header) #Başlıkları csv'ye yazdık.
  # writer.writerow(data) #Verileri csv'ye yazdık.

with open('AmazonWebScraping.csv','a+',newline='',encoding='UTF8') as f: #Csv dosyasına yeni verileri ekliyoruz.
   writer=csv.writer(f)
   writer.writerow(data) #Yeni verileri csv'ye ekliyoruz.

def check_price():
   URL='https://www.amazon.com.tr/Under-Armour-Charged-Pursuit-Ayakkab%C4%B1s%C4%B1/dp/B0969278HK/?_encoding=UTF8&pd_rd_w=xiL4E&content-id=amzn1.sym.8366b9e9-4852-434b-af36-c553f69a685e%3Aamzn1.symc.fc11ad14-99c1-406b-aa77-051d0ba1aade&pf_rd_p=8366b9e9-4852-434b-af36-c553f69a685e&pf_rd_r=5P06C660FXN0AEJ1FFW0&pd_rd_wg=BbWof&pd_rd_r=d439f0fd-21ae-4a23-ae33-6cf67d8dd96a&ref_=pd_hp_d_atf_ci_mcx_mr_ca_hp_atf_d&th=1&psc=1'
   headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"}

   page=requests.get(URL,headers=headers)

   soup1=BeautifulSoup(page.content,'html.parser') 
   soup2=BeautifulSoup(soup1.prettify(),'html.parser') 
   title=soup2.find(id='productTitle').get_text() 
   price=soup2.find(class_='a-price-whole').get_text()
   bugun=datetime.date.today()
   header=['Title','Price','Date'] 
   data=[title,price,bugun] 
   with open('AmazonWebScraping.csv','a+',newline='',encoding='UTF8') as f: 
    writer=csv.writer(f)
    writer.writerow(data)

while(True):
  check_price()
  time.sleep(86400) ##Her 24 saate bir fiyatı güncelleyecek.