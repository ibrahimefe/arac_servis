# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 13:51:24 2020

@author: ibrah
"""
import os
import random
import time
#import pandas as pd
import datetime
#import string



print(os.getcwd())

dummy_name = "dummyDataset"+time.strftime("%Y%m%d_%H%M%S")+".csv"
print(dummy_name)
#strftime.Org
header = "tarih,plaka,marka,model,uretim_tarihi,km,parca_fiyat,iscilik_fiyat"

markalar = ["FİAT","MERCEDES","BMW","AUDİ","TOFAS","FORD","TESLA","SAAB", \
            "VOLVO","WOLKSWAGEN"]
modeller = {"FİAT":["EGEA","500L","500","DOBLO"],
         "MERCEDES":["E200","S600","S350","A180"],
         "TOFAS":["DOGAN","SAHIN","KARTAL"],
         "BMW":["E200","S600","S350","A180"],
         "AUDİ":["E200","S600","S350","A180"],
         "FORD":["E200","S600","S350","A180"],
         "TESLA":["E200","S600","S350","A180"],
         "SAAB":["E200","S600","S350","A180"],
         "VOLVO":["E200","S600","S350","A180"],
         "WOLKSWAGEN":["E200","S600","S350","A180"]}
dosya = open(dummy_name,"w", encoding ='UTF-8')
dosya.write(header + "\n")

def randomDate ():
    start = datetime.datetime.now().replace(day=1, month=1, year=2018).toordinal()
    end = datetime.datetime.now().replace(day=1, month=1, year=2020).toordinal()
    pred = (datetime.date.fromordinal((random.randint(start,end))))
    return pred

def randomLicensePlate ():
    licensePlate = random.randint(1, 81)
    return licensePlate
    

for x in range(24000):
    #rplaka = ''.join.random.choice(string.ascii_uppercase + string.digits,k=7)
    plaka = randomLicensePlate()
    tarih = randomDate()
    marka = random.choice(markalar)
    model = random.choice(modeller[marka])
    
    üretim_tarihi = random.randint(2000, 2017)
    km = random.randint(1000, 200000)
    parça_fiyat= random.randint(50, 10000)
    işçilik_fiyat= random.randint(250, 2000)
    dosya.write(str(tarih)+","+str(plaka)+","+marka+","+model+","+str(üretim_tarihi)+","+str(km)+
                ","+str(parça_fiyat)+","+str(işçilik_fiyat)+"\n")
dosya.close()



