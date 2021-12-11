#Reference: https://stackoverflow.com/questions/46263392/add-months-to-xaxis-and-legend-on-a-matplotlib-line-plot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

df = pd.read_csv('Specific_Cols.csv')
newDF = pd.DataFrame()

# Make dataframe of the number of crimes for each day
newDF['CMPLNT_FR_DT'] = df['CMPLNT_FR_DT']
newDF['CMPLNT_FR_DT'] = pd.to_datetime(newDF['CMPLNT_FR_DT'])
newDF = newDF['CMPLNT_FR_DT'].dt.date.value_counts().reset_index().rename({'CMPLNT_FR_DT':'count'})
newDF = newDF.rename({'index':'CMPLNT_FR_DT','CMPLNT_FR_DT':'count'}, axis=1)
newDF['CMPLNT_FR_DT'] = pd.to_datetime(newDF['CMPLNT_FR_DT'])

#################  Two different filters for the two line graphs ##########################
#Total number of crimes by months for 2019 to 2020
#mask = (newDF['CMPLNT_FR_DT'] >= '2019-1-1') & (newDF['CMPLNT_FR_DT'] < '2021-1-1')
#Total number of crimes by months for 2019 to 2021
mask = (newDF['CMPLNT_FR_DT'] >= '2019-1-1') 

newDF = newDF.loc[mask]
newDF['CMPLNT_FR_DT'] = pd.to_datetime(newDF['CMPLNT_FR_DT'])
newDF = newDF.set_index('CMPLNT_FR_DT')
pt = pd.pivot_table(newDF, index=newDF.index.month, columns=newDF.index.year, aggfunc='sum')
pt.columns = pt.columns.droplevel()
ax = plt.figure().add_subplot(111)
ax.plot(pt)
ticklabels = [datetime.date(1900, item, 1).strftime('%b') for item in pt.index]
ax.set_xticks(np.arange(1,13))
ax.set_xticklabels(ticklabels) #add monthlabels 
ax.legend(pt.columns.tolist(), loc='center left', bbox_to_anchor=(1, .5)) #add the column names as legend.
plt.tight_layout(rect=[0, 0, 0.85, 1])

#Change the title accordingly
#plt.title("Total Number of Crimes by months in 2019 and 2020")
plt.title("Total Number of Crimes by months in 2019, 2020, and 2021")

plt.xlabel("Months", fontsize=12, labelpad=10)
plt.ylabel('Number of Crimes',fontsize=12, labelpad=10)
plt.show()
