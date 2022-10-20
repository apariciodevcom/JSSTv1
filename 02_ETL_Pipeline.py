import pandas as pd
import numpy as np
import re

df=[]
files=np.arange(1,60)

for file in files:
    data=pd.read_csv('data_analyst_'+str(file)+'.csv')
    #Store DataFrame in list
    df.append(data)
df=pd.concat(df)

df.shape
#Name of columns
df.columns
pd.set_option('display.max_rows', None)
pd.set_option("expand_frame_repr", True)

# Split text and eliminate special characters
df['jp']=df['Job Position'].apply(lambda x: " ".join(x.lower() for x in x.split()))
df['jp']=df['jp'].map(lambda x: re.sub(r'\W+',' ',x))
df['loc']=df['Location'].apply(lambda x: " ".join(x.lower() for x in x.split()))
df['loc']=df['Location'].map(lambda x: re.sub(r'\W+',' ',x))
df['company']=df['Company Name'].apply(lambda x: " ".join(x.lower() for x in x.split()))
df['company']=df['company'].map(lambda x: re.sub(r'\W+',' ',x))

df

#Rewiew word frequency
freq = pd.Series(' '.join(df['loc']).split()).value_counts()[:50]
print(freq)

#Flags for filtering

df['analyst'] = df['jp'].apply(lambda x: 1 if 'analyst' in x else 0)
df['software']= df['jp'].apply(lambda x: 1 if 'software' in x else 0)
df['developer']= df['jp'].apply(lambda x: 1 if 'developer' in x else 0)
df['engineer']= df['jp'].apply(lambda x: 1 if 'engineer' in x else 0)
df['freelance']= df['jp'].apply(lambda x: 1 if 'freelance' in x else 0)
df['remote']= df['jp'].apply(lambda x: 1 if 'remote' in x else 0)
df['DA']= df['jp'].apply(lambda x: 1 if 'data analyst' in x else 0)    
df['DS']= df['jp'].apply(lambda x: 1 if 'data scientist' in x else 0)
df['ML']= df['jp'].apply(lambda x: 1 if 'machine learning' in x else 0)
df['BI']= df['jp'].apply(lambda x: 1 if 'business intelligence' in x else 0)
df['DE']= df['jp'].apply(lambda x: 1 if 'data engineer' in x else 0)
df['senior']= df['jp'].apply(lambda x: 1 if 'senior' in x else 0)
df['junior']= df['jp'].apply(lambda x: 1 if 'junior' in x else 0)
df['bigdata']= df['jp'].apply(lambda x: 1 if 'big data' in x else 0)
df['powerbi']= df['jp'].apply(lambda x: 1 if 'power bi' in x else 0)
df['tableau']= df['jp'].apply(lambda x: 1 if 'tableau' in x else 0)
df['qlik']= df['jp'].apply(lambda x: 1 if 'qlik' in x else 0)
df['sql']= df['jp'].apply(lambda x: 1 if 'sql' in x else 0)
df['python']= df['jp'].apply(lambda x: 1 if 'python' in x else 0)
df['consultant']= df['jp'].apply(lambda x: 1 if 'consultant' in x else 0)
df['statistical']= df['jp'].apply(lambda x: 1 if 'statistical' in x else 0)
# id_job to identify job offer
df['id_job'] = df['Link'].str[34:60]
df['id_job'] = df['id_job'].str[1:11]
df['id_job']
# Location
df['CH']= df['loc'].apply(lambda x: 1 if 'Switzerland' in x else 0)
df['zurich']= df['loc'].apply(lambda x: 1 if 'Zurich' in x else 0)
df['germany']= df['loc'].apply(lambda x: 1 if 'Germany' in x else 0)
df['UK']= df['loc'].apply(lambda x: 1 if 'Kingdom' in x else 0)
df['loc_remote']= df['loc'].apply(lambda x: 1 if 'remote' in x else 0)
df.shape

# Drop duplicates
df = df.drop_duplicates(subset = ['id_job'])
df.shape

data=df[{'id_job', 'company','jp','loc','analyst', 'software', 'developer', 'engineer','freelance', 'remote', 'DA', 'DS', 'ML', 'BI', 'DE', 'senior', 'junior','bigdata', 'powerbi', 'tableau', 'qlik', 'sql', 'python', 'consultant','statistical','CH','UK', 'zurich', 'germany', 'loc_remote'}]

data.columns

data.to_csv("1457_job_offers.csv")

#from sqlalchemy import create_engine

#Genera conexion a la base de datos
#engine = create_engine('postgresql://postgres:password@localhost:puerto/dbname')
#df.to_sql('tablename', engine)

#filter
dfilter=df['DA']==1
dfilter.shape
