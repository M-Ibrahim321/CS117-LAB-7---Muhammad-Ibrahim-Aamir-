import pandas as pd

data= {
    'Product':['Laptop','Mouse', 'Keyboard','Monitor'],
    'Price':[120000,2500,4500,35000],
    'Quantity':[2,10,5,3]
}

df = pd.DataFrame(data)


#Adding Total Column
df['Total']=df['Price']*df['Quantity']
print("----------------------------------------")
print(df)
print("----------------------------------------")