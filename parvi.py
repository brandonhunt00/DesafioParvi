import rpa as r
import pandas as pd

df= pd.read_excel(C:\Users\Brandon Hunt\Downloads)

r.init()

r.url('http://www.rpachallenge.com/')
r.wait(10)
r.click('//button[text()="Start"]')

for index,row in df.iterrows():
    r.type('//input[@ng-reflect-name="labelFirstName"]',row['First Name'])
    r.type('//input[@ng-reflect-name="labelLastName"]',row['Last Name '])
    r.type('//input[@ng-reflect-name="labelCompanyName"]',row['Company Name'])
    r.type('//input[@ng-reflect-name="labelRole"]',row['Role in Company'])
    r.type('//input[@ng-reflect-name="labelAddress"]',row['Address'])
    r.type('//input[@ng-reflect-name="labelEmail"]',row['Email'])
    r.type('//input[@ng-reflect-name="labelPhone"]',str(row['Phone Number']))
    r.click('//input[@value="Submit"]')

r.snap('/html/body/app-root/div[2]','results.png')

r.close()
