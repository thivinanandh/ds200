import pandas as pd
data = pd.read_csv('data.csv')
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
import matplotlib.pyplot as plt3


plt.bar(data.iloc[-15:,0], data.iloc[-15:,5])
plt.xlabel('Year')
plt.title('Average RainFall in Southern Penninsula During Month of June-Sep' )
plt.ylabel('RainFall in mm')
plt.grid('on', linestyle='--')



plt2.scatter(data.iloc[-10:,0],data.iloc[-10:,4])
plt.xlabel('Year')
plt.ylabel('RainFall in mm')
plt.title('Average RainFall in Southern Penninsula During Month of June-Sep' )
plt.grid('on', linestyle='--')


boxplot = data.boxplot(column = ['Actual Rainfall: JUN', 'Actual Rainfall: JUL','Actual Rainfall: AUG','Actual Rainfall: SEPT'])
