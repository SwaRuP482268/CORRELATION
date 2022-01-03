import pandas as pd
import plotly.express as px
import csv 

with open("./data2.csv")as f:
        df = csv.DictReader(f)
        fig = px.scatter(df,x = "Size of TV",y = "Average time spent watching TV in a week")


fig.show()        
