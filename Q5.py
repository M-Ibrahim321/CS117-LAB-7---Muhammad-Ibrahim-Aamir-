import pandas as pd

#6 Cities data
data={
    'City':['Islamabad','Rawalpindi','Lahore','Karachi','Peshawar','Quetta'],
    'Population':[1200000,2098000,13000000,16000000,1970000,1000000],
    'Area (Km²)':[906,259,1772,3780,1257,2656]
}

df=pd.DataFrame(data)

#adding the desity column

df['Density']=df['Population']/df['Area']

print("Full DataFrame")
print(df)

print("First 3 rows")
print(df.head(3))