import pandas as pd

# pandas series is one-dimensional labeled array

# data = / index = can be removed and will still be recognized
# datatype is also flexible
series1 = pd.Series(data = [100, 200, 300, 400, 500], index = ['Lexus', 'Toyota', 'Honda', 'BMW', 'Acura'])
print(series1)
print(series1.index)

series2 = pd.Series([100, 'car', 300, 400, 500], ['Lexus', 'Toyota', 'Honda', 'BMW', 'Acura'])
print(series2)
print(series2['Toyota'])
print()
print(series2.loc['Lexus'])
print()
print(series2.loc[['Lexus','Acura']])
print()
print(series2[[0,1,3]])
print()
print(series2.iloc[2])
print()

print('BMW' in series2)
print(series2 * 2)
print()
print(series2[['Lexus','BMW']] ** 2)

# pandas dataframe is a 2-dimensional labeled data structure

data = {'one': pd.Series([100.,200.,300.], index=['apple','ball','clock']),
  'two': pd.Series([111.,222.,333.,4444.], index=['apple','ball','cerill','dancy'])
  } 
df1 = pd.DataFrame(data)
print(df1)
print(df1.index)
print(df1.columns)
print()
# show only selectd indicies
print(pd.DataFrame(data, index = ['apple','clock','dancy']))
print(pd.DataFrame(data, index = ['apple','clock','dancy'], columns = ['two','five']))
print()

# create dataframe from list of python dictionaries
data2 = [{'alex':1,'joe':2}, {'ema':5, 'dora':10, 'alice':20}]
print(pd.DataFrame(data2))
# privide index label array to dataframe
print(pd.DataFrame(data2, index=['orange','red']))
# select elements from dictionary
print(pd.DataFrame(data2, columns=['joe','dora','alice']))
print()

# Basec DataFrame operations
print(df1)
print()
print(df1['one'])
print()
# numerical operation
df1['three'] = df1['one'] * df1['two']
print(df1)
print()
# logical operation
df1['flag'] = df1['one'] > 150
print(df1)
print()
# remove data from dataframe(return value)
three = df1.pop('three')
print(three)
print(df1)
print()
# delete data from dataframe(pure delete)
del df1['two']
print(df1)
print()
# create new column by selecting another column, put under position 2
df1.insert(2, 'copy_of_one', df1['one'])
print(df1)
print()
# copy first 2 rows of specific columns
df1['first_2_of_one'] = df1['one'][:2]
print(df1)