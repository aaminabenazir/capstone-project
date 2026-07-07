import pandas as pd
import os
print("Files in this folder:")
print(os.listdir())
import matplotlib.pyplot as plt
import seaborn as sns
import os
# This finds the folder where the script is currently located
folder_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(folder_path, "california_housing_train.csv..csv")

df = pd.read_csv(file_path, encoding='utf-8-sig')
'''file_path="/Users/aaminabenazir/Desktop/california_housing_train.csv"
df=pd.read_csv(file_path)'''
print (df)
'''from google.colab import drive
drive.mount('/content/drive')'''
print("first 5 rows of the data:")
print (df.head())
print("data info:")
print(df.info())
df=df.dropna()
df.isnull().sum()
from numpy import shape
(df.isnull().sum()/df.shape[0]*100)
df.duplicated().sum()
df.drop_duplicates(inplace=True)
print (df)
pd.to_numeric(df['total_rooms'],errors='coerce')
pd.to_numeric(df['total_bedrooms'],errors='coerce')
df.memory_usage(deep=True).sum()
plt.figure(figsize=(12,6))
top_ages=df['housing_median_age'].value_counts().head(10)
sns.barplot(x=top_ages.index,y=top_ages.values,hue=top_ages.index,palette='viridis',legend=False)
plt.xlabel('Median Housing Age')
plt.ylabel('Count')
plt.title('Top 10 Median Housing Ages')
plt.savefig('top_10_median_housing_ages_barplot.png')
plt.show()
import matplotlib.pyplot as plt
sns.lineplot(x=df['population'],y=df['median_house_value'],color='red')
plt.xlabel('Population')
plt.ylabel('Median House Value')
plt.title('Population vs. Median House Value')
plt.savefig('population_vs_median_house_value_lineplot.png')
plt.show()
plt.close()
import matplotlib.pyplot as plt
plt.figure(figsize=(10,5))
df['housing_median_age'].value_counts().sort_index().plot(kind='bar')
plt.xlabel('Housing Median Age')
plt.ylabel('Count')
plt.title('Housing Count by Median Age')
plt.savefig('housing_count_by_median_age_barplot.png')
plt.show()
plt.close()
import matplotlib.pyplot as plt
import seaborn as sns
sns.scatterplot(x='median_income',y='median_house_value',data=df,color='purple')
plt.xlabel('Median Income')
plt.ylabel('Median House Value')
plt.title('Median Income vs. Median House Value')
plt.savefig('median_income_vs_median_house_value_scatterplot.png')
plt.show()
import matplotlib.pyplot as plt
sns.histplot(df['median_house_value'],bins=30,kde=True,color='green')
plt.xlabel('Median House Value')
plt.ylabel('Frequency')
plt.title('Distribution of Median House Value')
plt.savefig('distribution_of_median_house_value_histplot.png')
plt.show()
plt.close()
import matplotlib.pyplot as plt
plt.figure(figsize=(10,8))
corr_matrix=df.corr()
sns.heatmap(corr_matrix,annot=True,cmap='coolwarm',fmt='.2f')
plt.title('Correlation Matrix')
plt.savefig('correlation_matrix_heatmap.png')
plt.show()
plt.close()
import matplotlib.pyplot as plt
sns.pairplot(df[['median_house_value','median_income','total_rooms','housing_median_age']])
plt.savefig('pairplot.png')
plt.show()
plt.close()
df.to_csv('cleaned_data.csv',index=False)
