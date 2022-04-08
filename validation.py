import re
article = input("Enter your URL: ")

valid1=re.match('http:|https://[a-zA-Z0-9.]+/.+',article)
valid2=re.search('https://www.google.com/search/|https://www.facebook.com/|HTTPS://WWW.GOOGLE.COM/SEARCH|HTTPS://WWW.FACEBOOK.COM',article)

if(valid1!=None):
  if(valid2!=None):
    print(" Invalid URL ")
  else:
    print(" valid URL ")
else:
  print("Invalid URL")
 
#This is my python code for validation of URL

