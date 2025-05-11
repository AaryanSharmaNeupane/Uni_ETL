import requests
import pandas as pd

Base_Url="http://universities.hipolabs.com/search?country=Canada"
def extract()->dict:
    result=requests.get(Base_Url).json()
    return result

def transform(data:dict)->pd.DataFrame:
    df=pd.DataFrame(data)
    df=df[df["state-province"].str.contains('Ontario',na=False)]
    df['domains']=[",".join(map(str,d)) for d in df["domains"]]
    df['web_pages']=[",".join(map(str,d)) for d in df["web_pages"]]
    df=df.reset_index(drop=True)
    return df[["name","domains","web_pages"]]
       
       
    


data=extract()
transformed_data=transform(data)
print(transformed_data)

