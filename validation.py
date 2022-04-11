import re
import requests
article = input("Enter your URL: ")

def validations(article):
  valid3=requests.get(article)
  if(valid3.status_code==200):
    print(" Valid URL ")
  else:
    print(" Invalid URL ")

valid1=re.match('http:|https://[a-zA-Z0-9.]+/.+',article)
valid2=re.search('https://www.google.com/search/|https://www.facebook.com/|HTTPS://WWW.GOOGLE.COM/SEARCH|HTTPS://WWW.FACEBOOK.COM',article)

if(valid1!=None):
  if(valid2!=None):
    print(" Invalid URL ")
  else:
    validations(article)
else:
  print("Invalid URL")
 
#This is my python code for validation of URL

