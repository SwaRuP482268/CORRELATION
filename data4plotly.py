import pandas as pd
import plotly.express as px
import csv 

with open("./data4.csv")as f:
        df = csv.DictReader(f)
        fig = px.scatter(df,x = "week",y = "Coffee in ml")


fig.show()        
