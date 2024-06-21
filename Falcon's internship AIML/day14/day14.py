# data visualization tool
import seaborn as sns

from matplotlib import pyplot as plt

sns.get_dataset_names()


data=sns.load_dataset('fmri')
data.head()

data.tail()


# line plot
sns.lineplot(x='timepoint' , y='signal' , data=data)

plt.show()


sns.lineplot(x='timepoint' ,y='signal' , data=data , hue='event')
plt.show()


sns.lineplot(x='timepoint' ,y='signal' , data=data , hue='event' , style='event' ,markers=True)
plt.show()

# bar plot

dim=sns.load_dataset('diamonds')
plt.show()
dim.head()

# bar plot

sns.barplot(x='cut' , y='carat' , data=dim)
plt.show()


mpg=sns.load_dataset('mpg')
mpg.head()


sns.barplot(x='origin' ,y='horsepower' , data=mpg )
plt.show()

sns.barplot(x='origin' ,y='horsepower' ,data=mpg , palette='rocket' )
plt.show()

sns.barplot(x='origin' ,y='horsepower' ,data=mpg , color='pink' )
plt.show()

# scatter plot ==> used to make relationship between two numerical entities

peng=sns.load_dataset('penguins')
peng.head()

sns.scatterplot(x='bill_depth_mm' ,y='flipper_length_mm',data=peng)
plt.show()


sns.scatterplot(x='bill_depth_mm' ,y='flipper_length_mm',data=peng  , hue='species' , style='species')
plt.show()

# histogram  / distplot() // frequency curve

# distploat()

dim=sns.load_dataset('diamonds')
plt.show()
dim.head()



sns.distplot(dim['price'])
plt.show()


sns.distplot(dim['price'], hist=False ,color='green')
plt.show()


# histogram without frequency curve using kde

sns.distplot(dim['price'] ,bins=10, kde=False , color='yellow')
plt.show()

# distplot in  y axis

sns.distplot(dim['price'] ,vertical=True)
plt.show()


# jointPlot  ==> combinition of scatter plot and histogram

iris=sns.load_dataset('iris')
iris.head()


sns.jointplot(x='sepal_length' , y='petal_length' , data=iris  , hue='species')



sns.jointplot(x='sepal_length' , y='petal_length' , data=iris , kind='reg')

# box ploat

taxis=sns.load_dataset('taxis')
taxis.head()


sns.boxplot(x='payment', y='total', data=taxis)

sns.boxplot(x='payment' ,y='distance', data=taxis)
plt.show()

tips=sns.load_dataset('tips')
tips.head()