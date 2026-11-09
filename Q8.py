import pandas as pd


#Students Data

data={
    'Name':['Ali', 'Usman', 'Umer','Sara','Zain'],
    'Age':[17,16,18,19,20],
    'Math':[85,90,88,92,65],
    'Physics':[88,76,82,34,67],
    'ICT':[32,67,89,90,99]
}



df=pd.DataFrame(data)

#Total marks for each Students

df['Total Marks']=df['Math']+df['Physics']+df['ICT']

print("\nStudent data with total marks :")
print(df[['Name','Age','Math','Physics','ICT','Total Marks ']])


#Average marks for each Subject
AverageMarks=df[['Math','Physics','ICT']].mean()
print("\nAverage Marks :")
print(AverageMarks)