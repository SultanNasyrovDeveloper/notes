import pandas as pd

# get data
# prepare
# analise
# present

# === creation ===
# -= df =-
data = [[1, 2], [3, 4]]
df = pd.DataFrame(data, index=['a', 'b'], columns=['k', 'l'])
# -= reading =-
df.to_csv('filename.csv')
df.read_csv('filename.csv')
# -= s =-

# === base functions ===
df.head(x)  # show first x rows
df.tail(x)  # show last x rows
df.info()
df.describe()
df.dtypes  # check data types be column
df.index
df.columns
df.shape  # number of rows and column
df.to_string()
df.value_counts()  # histogramming(counts number of unigue values)
df.mode()  # most frequently occuring values

df.values  # to get the actual data inside data structure

# ===== options =====
# -= 5 functions =-
# get or set_option()  # pd.get_option('display.max_rows') / pd.set_option('display.max_rows', 99)
# reset_option()
# describe_option()
# option_context()

# -= frequently used options =-
pd.set_option('max_rows', x)  # will not display more than x rows
pd.set_option('max_columns', x)  # same with columns
pd.set_option('expand_frame_repr', bool)  # whether to show all columns ot not while displaying df
pd.set_option('large_repr', 'truncate'/'info')  # регулирует отображение df
# которые предышают утсановленную опцию max_rows, max_columns: truncate - обрезать, info - summary


# ===== assign =====
# methog for creating new columns
df.assign(C=lambda x: x['A'] + x['B'], D=lambda x: x['A'] + x['C'])

# === common methods ===
df.first()  # first data value
df.last()  # last valid value
df.ohlc()  # ??
df.max()  # max value
df.min()   # min value
df.sum()  # sum all given values
df.count()  # coun values
df.var()  # variance
df.mean()
df.median()
df.std()
df.unique()   # return series of unique values

# === common methods 2 ===
df.pipe()  # tablewise functions
df.apply(lambda x: pass, axis=1) # column or row wise functions x=column or row
    # aplly takes series and shoud return series
df.agg()
df.map(dictionary) # changes value according to map(dictionary)

df.groupby('column')  # groupin by unique 'column' values

# === selecting ===
df['column']  # returns Series
df[['column1', 'column2']]  # return df
df.get_value(index, column)  # for selecting actual attribute value

# -= boolean indexing =-

# -= select scalar value(single cell value) =-
df.at[index_label, column_label]
df.iat[index_pos, column_pos]

# -= loc =-
# label oriented slicing. Setting also available
# attrubute can be label, array of labels, slice, boolean array
df.loc[indexes, columns]
df.loc['a']  # select row with 'a' label
df.loc[['a', 'b', 'c'], :]  # select rows 'a', 'b', 'c' and all columns
df.loc[:, 'A': 'G']  # slicing columns
df.loc['b':, 'A': 'C']  # select all row starting from 'b', and columns from 'A" to 'C'
df.loc[:, df.loc['a'] > 0]  # select all rows in columns where 'a' row value more than 0

# -= iloc =-
# position oriented selection. Setting also available
# attrubute can be label, array of labels, slice, boolean array
df.iloc[index, column]

df.iloc[1, :]
df.iloc[[1, 5, 16, 46], [1, 2]]
df.iloc[1:10, :]
df.iloc[:, 1:8:2]


# === reshaping ===
df.T  # change axes(columns become indexes)
df.sort_index(axis=1, ascending=True) # sort by indexes, axis 1 - column, 0 - index
df.sort_values(by='column name')  # sort rows by column
df.set_index(keys=[],)

# === adding ===
# -= concat =-
df = pd.concat([df1, df2])  # concat 2 objects
    axis=0/1 # default 0(adding new rows) 1 adding new columns
    ignore_index=bool  # if True default objects indexes wont br used
    keys=[]  # последовательность имен для связываемых объектов
# -= append =-
# concatination only by 0 axis(add row)
df1.append(df2)

# -= merge =-
# advanced database like concatination option
pd.merge()
    left # fisrt dataframe
    right # seconds df
    on='column or index name' # признак по которому будет производитсья соединение
        # должен присутствовать в обоих объектах


df.values.to_list()  # make row values list

df.sample(n=12, axis=0,) # random row or column axis=1


df.drop_duplicates()  # drop duplicated rows
df.drop_duplicates(subset='column')  # drop duplicates by one column
