import matplotlib.pyplot as plt
import pandas as pd

years=list(range(2010,2025))
sales = [100, 120, 115, 140, 160, 155, 180, 200, 210, 240,230, 260, 280, 300, 320]


profit=[12,15,14,18,22,20,25,28,30,35,32,40,44,48,52]

data = pd.DataFrame({"Year": years, "Sales": sales, "Profit": profit})
print(data)

#Scatter plot
plt.scatter(years,profit,color='red',label='Yearly profit')


plt.plot(years,profit,color='green',label='Profit Trend')

plt.title('Company Yearly Profit')
plt.xlabel('Years')
plt.ylabel('Profit in Thousands (USD)')
plt.legend()
plt.grid(True)
plt.show()