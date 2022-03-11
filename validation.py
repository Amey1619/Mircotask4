import re
article = input("Enter your URL: ")
valid=re.search('https://www.google.com/search/|https://www.facebook.com/',article)
if(valid!=None):
  print("It is not valid url")
else:
    print("It is valid url")
#This is my python code for validation of URL



