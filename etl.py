import requests
import pandas as pd
import sqlalchemy


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
       
def load(df:pd.DataFrame):
    
    try:
        engine = sqlalchemy.create_engine(
            "postgresql+psycopg2://Aaryan:ads@localhost:5432/university"
        )
        print("Rows in transformed_data:", len(transformed_data))
        print(transformed_data.head())

        df.to_sql('ontario',engine,if_exists='replace',index=False)
        with engine.connect() as conn:
            result = conn.execute(sqlalchemy.text("SELECT COUNT(*) FROM Ontario"))
            count = result.scalar_one()   # scalar_one() returns the single value
            print(f"Rows now in database: {count}")
    except Exception as e:
        print(e)

    


data=extract()
transformed_data=transform(data)
load(transformed_data)

