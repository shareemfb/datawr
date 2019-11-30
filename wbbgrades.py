import pandas as pd
wbb1 = {'Student':['Ice Bear', 'Panda', 'Grizzly'], 'Math':[80,95,79]}
df1 = pd.DataFrame(wbb1, columns=['Student','Math'])
wbb2 = {'Student':['Ice Bear', 'Panda', 'Grizzly'], 'Electronics':[81,85,83]}
df2 = pd.DataFrame(wbb2, columns=['Student','Electronics'])
wbb3 = {'Student':['Ice Bear', 'Panda', 'Grizzly'], 'GEAS':[90,79,93]}
df3 = pd.DataFrame(wbb3, columns=['Student','GEAS'])
wbb4 = {'Student':['Ice Bear', 'Panda', 'Grizzly'], 'ESAT':[93,89,88]}
df4 = pd.DataFrame(wbb4, columns=['Student','ESAT'])

resultdf1 = pd.merge(df1, df2, how='outer', on = 'Student')
resultdf2 = pd.merge(df3, df4, how='outer', on = 'Student')
finalres = pd.merge(resultdf1, resultdf2, how='outer', on='Student')
print('The resulting dataframe from merging the four dataframes:\n', finalres, '\n')

tidy = pd.melt(finalres, id_vars=['Student'], value_vars = ['Math', 'Electronics', 'GEAS', 'ESAT'])
tidyR = tidy.rename(columns={'variable':'Subjects', 'value': 'Grades'})
tidyS = tidyR.sort_values('Student')
tidyfinal = tidyS.reset_index().drop(columns=['index'])
print('The dataframe in long format:\n', tidyfinal, '\n')

