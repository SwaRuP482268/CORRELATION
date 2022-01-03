import pandas as pd
import plotly.express as px
import csv 

with open("./data3.csv")as f:
        df = csv.DictReader(f)
        fig = px.scatter(df,x = "Marks In Percentage",y = "Roll No")


fig.show()        
