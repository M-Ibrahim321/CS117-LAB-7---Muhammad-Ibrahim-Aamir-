import matplotlib.pyplot as plt

days=[1,2,3,4,5]
temp_cityA=[22,24,21,25,23]
temp_cityB=[30,32,29,31,33]

plt.plot(days,temp_cityA,color='blue',marker='o',label='city1')
plt.plot(days,temp_cityB,color='orange',marker='s',label='city2')

plt.title('Daily Temperature Data')
plt.xlabel('Days')
plt.ylabel('Temperature (Celsius)')
plt.legend()
plt.grid(True)
plt.show()