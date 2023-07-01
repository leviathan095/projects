
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df= pd.read_csv('C:\codecademy\Exploring Mushrooms\mushroom_data.csv')
print(df.head())

#columns
for index in range(0,len(df['Bruises'])):
    df['Bruises'][index]=str(df['Bruises'][index])
columns = df.columns.tolist()
for column in columns:
    if column in ['Veil Type','Veil Color']:
        print('The data is not informative for {}'.format(column))
    elif len(df[column].unique())<4:
        plt.pie(df[column].value_counts(),labels=df[column].value_counts().index)
        plt.axis('equal')
        plt.title(column + ' Value Counts')
        plt.show()
        plt.clf()
    else:
        sns.countplot(x=column,data=df,order=df[column].value_counts().index)
        plt.xticks(rotation=30,fontsize=10)
        plt.xlabel(column,fontsize=12)
        plt.title(column + ' Value Counts')
        plt.show()
        plt.clf()
        