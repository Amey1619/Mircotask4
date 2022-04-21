import re
import requests
article = input("Enter your URL: ")

def validations(article):
  valid3=requests.get(article) # valid3 will send a get request and validates the URL
  if(valid3.status_code==200): # If status_code returns 200 it will a valid URL otherwise it not.
    print(" Valid URL ")
  else:
    print(" Invalid URL ")

valid1=re.match('http:|https://[a-zA-Z0-9.]+/.+',article)   # Matches is URL matches the format of URL
valid2=re.search('https://www.google.com/search/|https://www.facebook.com/|HTTPS://WWW.GOOGLE.COM/SEARCH|HTTPS://WWW.FACEBOOK.COM',article) # Avoiding google and facebook unreliable URL

if(valid1!=None): # If valid1 does not match then format is incorrect 
  if(valid2!=None): # If valid2 does not find any google search results it is correct
    print(" Invalid URL ")
  else:
    validations(article) # If valid1 & valid2 fields are cleared then only validations function will run !
else:
  print("Invalid URL")
 
#This is my python code for validation of URL

