# capstone-project part 1 (coding-explanation)
pipeline:
1.loading the datset(pd.rtead_csv)
2.inspecting the structures(.head(),.info())
3.checking and cleaning missing values(.isnull().sum(),.drpna())
4.remioving rows(drop_duplicates(inplace=True)
5.fixing datatype anomalies(pd.to_numeric)
6.visualizing single distribution and multi variable correlation(sns.histplot,sns.hestmap,sns.pairplot)
7.exporting clean dataset for future use(.to_csv)

I.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
file_path='/content/sample_data/california_housing_train.csv'
df=pd.read_csv(file_path)
print (df)
*import the pandas library and nicknames it pd. imports matplotlib.pyplot as plt:imports the foundational plotting engine in python, nicnaming it . use this to cuswtoimize title and display graphs. import seaborn as sns:imports sesborn,a libtaty built on top of matplotlib that make drawing beautiful,complex ststidtical graphics much easier.
*longitude and latitude : the geographic coordinates of the neighborhood. housing meadian age:median age of the houses in that block. total_rooms and total_bedroom:total counts for that neighborhood population and households:the number of peoples and families living there. median incme:median income for house holds in the area(scaled) median home value:the target variable ehat the home are generally worth.


II.
print("first 5 rows of the data:")
print (df.head())
print("data info:")
print(df.info())
*df.head()grabs the first 5 rows. it tells: total entries:total number of rows column names: a list of all columns in the dataset.] non null count:how many values in each column are not empty. datatype(dtypes):tells you if the data is a float (decimal number).integer(whole. number) or object (text/string)


III
df=df.dropna()
df.isnull().sum()
(df.isnull().sum()/df.shape[0]*100)
df.duplicated().sum()
pd.to_numeric(df['total_rooms'],errors='coerce')
pd.to_numeric(df['total_bedrooms'],errors='coerce')
*the line of code is used to clean your dataset by remaing missing data.
*this line code is check for missing values in a data set using panas
*this code calculate the percentage of missing for each column in your dataset
*by default doesnt change hte original variable. inplace = true -->modify the original df variable directly in place.
*this code converts the column totakl_rows and total bedrooms into numeric data types like integer and float. *when numbers in our datasets are accidenlly being read as text ,symbol or formatting errors in those columns. Eg.three instead of 3 *panda will force the conversion any way and replace any convertible with a missing value(NaN)


IV
df.memory_usage(deep=True).sum()
*this line calculates the total memory(ram)used by your entire dsatframe,measured in bytes. *df.memory_usage() our dataframe column by column and return how many bytes of memory each individual column is consuming.


V
plt.figure(figsize=(12,6))
top_ages=df['housing_median_age'].value_counts().head(10)
sns.barplot(x=top_ages.index,y=top_ages.values,palette='viridis')
plt.xlabel('Median Housing Age')
plt.ylabel('Count')
plt.title('Top 10 Median Housing Ages')
plt.savefig('top_10_median_housing_ages_barplot.png')
plt.show()
*create a bar plot
*it transitions your workflow from data cleaning into data visualization. *fig size=(12,6)-->see the dimention of 12 inches wide by 6 inches tall. *value count()-->counts how many times each specific age appears in the dataset.it automaticallyt sorts them from the most frequent age to the least frequent. *head(10)-->grab only the first 10 most frequent ages. *platte='viridis'--> applies a beautiful,modern color that shifts smoothly from dark purple to bright yellow across the bars *plt.xlabel/ylabel/title-->for adding the heading *plt.save fig()-->savesimages as a .png file in your current work space directly|(you can download)


VI
import matplotlib.pyplot as plt
sns.lineplot(x=df['population'],y=df['median_house_value'],color='red')
plt.xlabel('Population')
plt.ylabel('Median House Value')
plt.title('Population vs. Median House Value')
plt.savefig('population_vs_median_house_value_lineplot.png')
plt.show()
*line plot *using seaborn to visualize how median house value changes in relation to the population column,displaying the result as a prominent red line. *plt.show()-->display the finished chart clearly our screen.


VII
import matplotlib.pyplot as plt
plt.figure(figsize=(10,5))
df['housing_median_age'].value_counts().sort_index().plot(kind='bar')
plt.xlabel('Housing Median Age')
plt.ylabel('Count')
plt.title('Housing Count by Median Age')
plt.savefig('housing_count_by_median_age_barplot.png')
plt.show()
*barplot showing the count of neighbourhoods for every single housing age in our dataset,sorted chronologically from younest to oldest. *its shows the enire distribution of housing ages,rather than just the top 10


VIII
import matplotlib.pyplot as plt
import seaborn as sns
sns.scatterplot(x='median_income',y='median_house_value',data=df,color='purple')
plt.xlabel('Median Income')
plt.ylabel('Median House Value')
plt.title('Median Income vs. Median House Value')
plt.savefig('median_income_vs_median_house_value_scatterplot.png')
plt.show()
*This code creates a sctter plot using seaborn to look at the relation between median income and median house value *scatter plot is the absoulte best choise for this task because both variable are continuous numbers allowing .we to see if a higher income directly correlates with more expensive housing.
*colour=purple --> colors all the scatter points a vibrant purple. *when you view this plot,you will see two very distinct and famoius patterns in the california housing data


IX
import matplotlib.pyplot as plt
sns.histplot(df['median_house_value'],bins=30,kde=True,color='green')
plt.xlabel('Median House Value')
plt.ylabel('Frequency')
plt.title('Distribution of Median House Value')
plt.savefig('distribution_of_median_house_value_histplot.png')
plt.show()
*this code creates a histogram with a smooth trend line(KDE CURVE)USING SEABORN TO Analyze the distribution of median house value. *a histogram is the perfect tool for this because it lets you see how the home prices are spread out.where the most common price points lie and whether the data is skewed. *bins=30--> splits the range of house value into exactly 30 vertical bars. *Kde=true-->this stands for kernel density on the top of the bar . *color=green-->turns both bars and cure looks green.


X
import matplotlib.pyplot as plt
plt.figure(figsize=(10,8))
corr_matrix=df.corr()
sns.heatmap(corr_matrix,annot=True,cmap='coolwarm',fmt='.2f')
plt.title('Correlation Matrix')
plt.savefig('correlation_matrix_heatmap.png')
plt.show()
*this codes creates a correlation matrix heatmao using seaborn.this is a. crucial step in exploratory dta analysis(EDA),as it visualizes how strongly every single numeric column in our dataset relates to every other coloumn . *df.corr()-->this is a powerfuk pandas function.it automatically pairs up every single column with every other column and calculates their person correlation co efficient. -->value of 1.0 mean positive relationship (one goes up other goes up) -->value of -1.0 means perfect negative relationship(ones goes up,other goes down) -->value of 0.0 means there is no linear relationshipo at all. *annot=true-->short forn "annotate".this forces seaborn to print the actual correlation number inside each square,rather than just showing colors. *cmap='coolwarm'-->specifies the color palette.coolwarm is excellent for correlations because negative correlation show up as cool blues no correlation positive correlations showsup as warm reds. *fmt='.2f'-->formats the numbers inside the boxes to show exactly 2 decimal places.


XI
import matplotlib.pyplot as plt
sns.pairplot(df[['median_house_value','median_income','total_rooms','housing_median_age']])
plt.savefig('pairplot.png')
plt.show()
*this codes creates a pairplot also known as a scatter plot matriux)using sesborn. -->this is one of the most p[opwerful visualization techniques in data science becauise it allows us to see everything to see. *df[['coloumn1,'column2',...]]-->passes subset of our data frame containing only 4 coloumns you care about.if we ran sn.pairplot(df) on the whole dataset,it would generate 9x9 grid it would take a long time no compute and be too small to read. *sna,pairplot()-->instruct sesborn to build a grid based on your 4 selected variable.it will create 4x4 grid . containing 16 individual plots


XII
df.to_csv('cleaned_data.csv',index=False)
*this line of code is the final step of our data cleaning pipeline.it take your fully cleaned duplicate free and correctly formatted dataframe(df)and save it back to your computer as a new csv filke named cleaned_data.csv
*df.to_csv()-->this is a built in pandas function that converts your liove python dataframe back into a flat ,comma-separated text file dormat. *cleaned_data.csv-->name of the new file *index=false by default pandas will include the row numbers(0,1,2,3....)as the very first column in your new csc file. *setting index=false tells pandas-->"do not include those row numbers in the output file."
