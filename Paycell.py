# -*- coding: utf-8 -*-
# !/usr/bin/env python3
import sys,json,time,requests,os,threading,re,datetime
from random import randint
from queue import Queue
import os

sira=Queue()
    
    
def giris_token():
    url1="https://services.paycell.com.tr/tpay/paycell/services/sessionapprs/sessionServiceApp/init/"
    headers1={"Cookie":"",
                        "version": "3.5.0",
                        "Authorization":"",
                        "Content-Type": "application/json; charset=UTF-8",
                        "Content-Length": "494",
                        "Host": "services.paycell.com.tr",
                        "Connection": "Keep-Alive",
                        "Accept-Encoding": "gzip",
                        "User-Agent": "okhttp/3.12.3"
                        }
    data1=json.dumps({"connectionType":"WIFI","globalParameterVersion":"","hashData":"1eYUfC+z6qFpi5EFeDNeX+sSprHKLLumyDPlteC/HRk=","language":"tr","requestHeader":{"deviceInfo":{"deviceId":"f894c25678684831","deviceManufacturer":"samsung","deviceModel":"SM-N950N","deviceOs":"ANDROID","deviceOsVersion":"5.1.1"},"transactionInfo":{"application":"AndroidAPP","applicationVersion":"3.5.0","authToken":"","mode":"STORE","transactionDateTime":zaman(),"transactionId":TRX(),"version":"44"}}})
    headers1["Content-Length"]=str(len(data1))
    res1=requests.post(url1,headers=headers1,data=data1)
    #print(res1.headers)
    #return res1.json()
    #print([res1.headers["Set-Cookie"],res1.json()["authToken"]])
    return [res1.headers["Set-Cookie"],res1.json()["authToken"]]

def SMS(user,cookie,token):
    url1="https://services.paycell.com.tr/tpay/paycell/services/sessionapprs/sessionServiceApp/sendOtp/"
    headers1={
                        "Cookie": cookie,
                        "version": "4.2.1",
                        "Authorization":"",
                        "Content-Type": "application/json; charset=UTF-8",
                        "Content-Length": "434",
                        "Host": "services.paycell.com.tr",
                        "Connection": "Keep-Alive",
                        "Accept-Encoding": "gzip",
                        "User-Agent": "okhttp/3.12.3",
                        }

    data1=json.dumps({"msisdn":user,"requestHeader":{"deviceInfo":{"deviceId":"f894c25678684831","deviceManufacturer":"samsung","deviceModel":"SM-N950N","deviceOs":"ANDROID","deviceOsVersion":"5.1.1"},"transactionInfo":{"application":"AndroidAPP","applicationVersion":"4.2.1","authToken":token,"mode":"STORE","transactionDateTime":zaman(),"transactionId":TRX(),"version":"44"}}})
    
    headers1["Content-Length"]=str(len(data1))
    res1=requests.post(url1,headers=headers1,data=data1)
    return res1.json()["otpValidationId"]
    
def sifre_gir(password,cookie,token):
    url1="https://services.paycell.com.tr/tpay/paycell/services/sessionapprs/sessionServiceApp/validatePin/"
    headers1={
                        "Cookie": cookie,
                        "version": "4.2.1",
                        "Authorization":"",
                        "Content-Type": "application/json; charset=UTF-8",
                        "Content-Length": "482",
                        "Host": "services.paycell.com.tr",
                        "Connection": "Keep-Alive",
                        "Accept-Encoding": "gzip",
                        "User-Agent": "okhttp/3.12.3",
                        }

    data1=json.dumps({"pin":password,"requestHeader":{"deviceInfo":{"deviceId":"f894c25678684831","deviceManufacturer":"samsung","deviceModel":"SM-N950N","deviceOs":"ANDROID","deviceOsVersion":"5.1.1"},"transactionInfo":{"application":"AndroidAPP","applicationVersion":"4.2.1","authToken":token,"mode":"STORE","transactionDateTime":zaman(),"transactionId":TRX(),"version":"44"}}})
    headers1["Content-Length"]=str(len(data1))
    res1=requests.post(url1,headers=headers1,data=data1)
    
    
def SMS_ONAY(kod,sms_id,cookie,token):
    url1="https://services.paycell.com.tr/tpay/paycell/services/sessionapprs/sessionServiceApp/validateOtp/"
    headers1={
                        "Cookie": cookie,
                        "version": "4.2.1",
                        "Authorization":"",
                        "Content-Type": "application/json; charset=UTF-8",
                        "Content-Length": "482",
                        "Host": "services.paycell.com.tr",
                        "Connection": "Keep-Alive",
                        "Accept-Encoding": "gzip",
                        "User-Agent": "okhttp/3.12.3",
                        }

    data1=json.dumps({"otp":kod,"otpValidationId":sms_id,"requestHeader":{"deviceInfo":{"deviceId":"f894c25678684831","deviceManufacturer":"samsung","deviceModel":"SM-N950N","deviceOs":"ANDROID","deviceOsVersion":"5.1.1"},"transactionInfo":{"application":"AndroidAPP","applicationVersion":"4.2.1","authToken":token,"mode":"STORE","transactionDateTime":zaman(),"transactionId":TRX(),"version":"44"}}})
   
    headers1["Content-Length"]=str(len(data1))
    res1=requests.post(url1,headers=headers1,data=data1)
   
def kontrol(cookie,token):
    url1="https://services.paycell.com.tr/tpay/paycell/services/customerapprs/customerServiceApp/getBenefit"
    headers1={
                        "Cookie":cookie,
                        "version": "4.2.1",
                        "Authorization":"",
                        "Content-Type": "application/json; charset=UTF-8",
                        "Content-Length": "432",
                        "Host": "services.paycell.com.tr",
                        "Connection": "Keep-Alive",
                        "Accept-Encoding": "gzip",
                        "User-Agent": "okhttp/3.12.3",
                        }
                        
                        
    data1=json.dumps({"benefitType":"BOX","requestHeader":{"deviceInfo":{"deviceId":"f894c25678684831","deviceManufacturer":"samsung","deviceModel":"SM-N950N","deviceOs":"ANDROID","deviceOsVersion":"5.1.1"},"transactionInfo":{"application":"AndroidAPP","applicationVersion":"4.2.1","authToken":token,"mode":"STORE","transactionDateTime":zaman(),"transactionId":TRX(),"version":"44"}}})
    
    headers1["Content-Length"]=str(len(data1))
    res1=requests.post(url1,headers=headers1,data=data1)
    
    if res1.json()["benefitCode"]=="SALLA_TOPLA1":
        print("Sallama Hakkı var")
        return True
    else:
        print("Sallama Hakkı Yok!")
        return False
   
def puan(cookie,token,son=500):
    url1="https://services.paycell.com.tr/tpay/paycell/services/customerapprs/customerServiceApp/getBonusHistory"
    headers1={"Cookie": cookie,
                    "version":"4.2.1",
                    "Authorization":"",
                    "Content-Type": "application/json; charset=UTF-8",
                    "Content-Length": "565",
                    "Host": "services.paycell.com.tr",
                    "Connection": "Keep-Alive",
                    "Accept-Encoding": "gzip",
                    "User-Agent": "okhttp/3.12.3"
                    }
    data1={"currency":"MB","endDate":zaman()[0:8],"startDate":"20200101","requestHeader":{"deviceInfo":{"deviceId":"0faf1a78bf78b0a0","deviceManufacturer":"samsung","deviceModel":"SM-G955N","deviceOs":"ANDROID","deviceOsVersion":"5.1.1"},"merchant":{"imageName":0,"merchantCode":"-9999","terminalCode":"-9999","timeoutDuration":0},"transactionInfo":{"application":"AndroidAPP","applicationVersion":"4.2.1","authToken":token,"mode":"STORE","transactionDateTime":zaman(),"transactionId":TRX(),"version":"44"}}}
    res1=requests.post(url1,headers=headers1,json=data1)
    gecmis=res1.json()["bonus"]
    print("Tarih        Hediye\n"+("_"*60))
    for i in gecmis[0:son]:
        
        if i["references"][0]["referenceType"]=="ACTIVATE_BENEFIT":
            print("%s         %s"%(i["createDate"],i["campaignName"]))



   
def get_account(cookie,token):
    url1="https://services.paycell.com.tr/tpay/paycell/services/customerapprs/customerServiceApp/getAccount/"
    headers1={
                        "Cookie": cookie,
                        "version": "4.2.1",
                        "Authorization":"",
                        "Content-Type": "application/json; charset=UTF-8",
                        "Content-Length": "412",
                        "Host": "services.paycell.com.tr",
                        "Connection": "Keep-Alive",
                        "Accept-Encoding": "gzip",
                        "User-Agent": "okhttp/3.12.3",
                        }

    data1=json.dumps({"requestHeader":{"deviceInfo":{"deviceId":"f894c25678684831","deviceManufacturer":"samsung","deviceModel":"SM-N950N","deviceOs":"ANDROID","deviceOsVersion":"5.1.1"},"transactionInfo":{"application":"AndroidAPP","applicationVersion":"4.2.1","authToken":token,"mode":"STORE","transactionDateTime":zaman(),"transactionId":TRX(),"version":"44"}}})
    
    headers1["Content-Length"]=str(len(data1))
    res1=requests.post(url1,headers=headers1,data=data1)

   
   
def logout(cookie,token):
    url1="https://services.paycell.com.tr/tpay/paycell/services/sessionapprs/sessionServiceApp/logout/"
    headers1={
                        "Cookie": cookie,
                        "version": "4.2.1",
                        "Authorization":"",
                        "Content-Type": "application/json; charset=UTF-8",
                        "Content-Length": "412",
                        "Host": "services.paycell.com.tr",
                        "Connection": "Keep-Alive",
                        "Accept-Encoding": "gzip",
                        "User-Agent": "okhttp/3.12.3",
                        }

    data1=json.dumps({"requestHeader":{"deviceInfo":{"deviceId":"f894c25678684831","deviceManufacturer":"samsung","deviceModel":"SM-N950N","deviceOs":"ANDROID","deviceOsVersion":"5.1.1"},"transactionInfo":{"application":"AndroidAPP","applicationVersion":"4.2.1","authToken":token,"mode":"STORE","transactionDateTime":zaman(),"transactionId":TRX(),"version":"44"}}})
    headers1["Content-Length"]=str(len(data1))
    res1=requests.post(url1,headers=headers1,data=data1)
    if res1.json()["responseHeader"]["responseDescription"]=="Success":
        print("Başarılı Bir şekilde Çıkış Yapıldı")
        return True
    else:
        print("Hata")
        return False
   

def salla(cookie,token,zam,trans):
    url1="https://services.paycell.com.tr/tpay/paycell/services/customerapprs/customerServiceApp/activateBenefit"
    headers1={
                        "Cookie": cookie,
                        "version": "4.2.1",
                        "Authorization":"",
                        "Content-Type": "application/json; charset=UTF-8",
                        "Content-Length": "412",
                        "Host": "services.paycell.com.tr",
                        "Connection": "Keep-Alive",
                        "Accept-Encoding": "gzip",
                        "User-Agent": "okhttp/3.12.3",
                        }
    #data1=json.dumps({"benefitCode":"SALLA_TOPLA1","requestHeader":{"deviceInfo":{"deviceId":"f894c25678684831","deviceManufacturer":"samsung","deviceModel":"SM-N950N","deviceOs":"ANDROID","deviceOsVersion":"5.1.1"},"transactionInfo":{"application":"AndroidAPP","applicationVersion":"4.2.1","authToken":token,"mode":"STORE","transactionDateTime":zaman(),"transactionId":trans,"version":"44"}}})
    data1=json.dumps({"benefitCode":"SALLA_TOPLA1","requestHeader":{"deviceInfo":{"deviceId":"f894c25678684831","deviceManufacturer":"samsung","deviceModel":"SM-N950N","deviceOs":"ANDROID","deviceOsVersion":"5.1.1"},"transactionInfo":{"application":"AndroidAPP","applicationVersion":"4.2.1","authToken":token,"mode":"STORE","transactionDateTime":zaman(),"transactionId":TRX(),"version":"44"}}})
    
    headers1["Content-Length"]=str(len(data1))
    res1=requests.post(url1,headers=headers1,data=data1)
    if res1.json()["responseHeader"]["responseDescription"]=="Success":
        Hediyeler.append(str(res1.json()["activationAmount"]))
        return True
    else:
        Hediyeler.append("Bos")
    

def basla(sira):
    dene=0
    while dene<10:
        cookie,token,zam,trans=sira.get()
        try:
            salla(cookie,token,zam,trans)
        except Exception as error:
            #print(str(error))
            pass
        dene+=1
    sira.task_done()
        



print ("Sistem baslatiliyor...")
TRX=lambda : "".join([str(randint(0, 9)) for p in range(0, 19)])
zaman=lambda : str(re.sub('[^0-9]', '',str(datetime.datetime.now()))[:17])

username="".join(str(input("Telefon no;\n>>+90 ")).split(" "))
count=input("Kac defa salla topla:\n>>")

cookie,token=giris_token()
time.sleep(1)
sms_id=SMS(username,cookie,token)
kod=input("Telefona gelen sms kodu\n>")
SMS_ONAY(kod,sms_id,cookie,token)
password=input("Paycell Sifresi:\n>>")
time.sleep(1)
sifre_gir(password,cookie,token)
time.sleep(1)
get_account(cookie,token)
kontrol(cookie,token)
time.sleep(1)

Hediyeler=[]

zam=zaman()
trans=TRX()

for i in range(int(count)):
    p=threading.Thread(target=basla,args=(sira,))
    p.daemon=True
    p.start()
    sira.put([cookie,token,zam,trans])
    #print (i," Sallandi")
print("ahmetesmer ile Gelen hediyeler:")
print(dict((x,Hediyeler.count(x)) for x in set(Hediyeler)))    
time.sleep(5)
print("ahmet ile gösterilen hediyeler.")
puan(cookie,token)
logout(cookie,token)
print("ahmetesmer e yanliş yapilmaz...")
