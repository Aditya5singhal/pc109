import pandas as pd
import plotly.figure_factory as px 
import csv
import statistics

df=pd.read_csv('sp.csv')
#fig=px.create_distplot([df["Weight(Pounds)"].tolist()],["Weight"],show_hist=False)
#fig.show()
heightlist=df["reading score"].to_list()
weightlist=df["writing score"].to_list()

heightmean=statistics.mean(heightlist)
print(heightmean)

weightmean=statistics.mean(weightlist)
print(weightmean)

heightmean=statistics.mode(heightlist)
print(heightmean)



weightmean=statistics.mode(weightlist)
print(weightmean)

heightmean=statistics.median(heightlist)
print(heightmean)

weightmean=statistics.median(weightlist)
print(weightmean)

heightstdiv=statistics.stdev(heightlist)
weightstdiv=statistics.stdev(weightlist)
print(heightstdiv)
print(weightstdiv)


heightstdivstart=heightmean-heightstdiv
print(heightstdivstart)


heightstdivend=heightmean+heightstdiv
print(heightstdivend)

weightstdivstart=weightmean-weightstdiv
print(weightstdivstart)


weightstdivend=weightmean+weightstdiv
print(weightstdivend)