
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

mushroom_data= pd.read_csv('C:\codecademy\Exploring Mushrooms\mushroom_data.csv')
print(mushroom_data.head())

#columns
for index in range(0,len(mushroom_data['Bruises'])):
    mushroom_data['Bruises'][index]=str(mushroom_data['Bruises'][index])
columns = mushroom_data.columns.tolist()
for column in columns:
    sns.countplot(x=column,data=mushroom_data,order=mushroom_data[column].value_counts().index)
    #print(column)
    plt.xticks(rotation=30,fontsize=10)
    plt.xlabel(column,fontsize=12)
    plt.title(column + ' Value Counts')
    plt.show()
    plt.clf()