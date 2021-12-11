import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('Specific_Cols.csv')
print(df['BORO_NM'].value_counts())
# Making Bar Graph of the Total # of Crimes from each Borough
print(df['BORO_NM'].value_counts().plot(kind = "bar"))
plt.xticks(rotation=0, horizontalalignment="center")
plt.title("Total Number of Crimes in each Borough from 2019 to 2021")
plt.xlabel("Borough", fontsize=12, labelpad=10)
plt.ylabel('Number of Crimes',fontsize=12, labelpad=10)
# Putting values above each bar of bar graph
boroNumsY = [91122, 79229, 69912, 67724, 13801]
for i in range(5):
    plt.text(i, boroNumsY[i], boroNumsY[i], ha='center', va='bottom')
plt.show()