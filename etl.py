import requests

Base_Url="http://universities.hipolabs.com/search?country=Canada"
def extract()->dict:
    result=requests.get(Base_Url).json()
    return result

data=extract()
print(data)