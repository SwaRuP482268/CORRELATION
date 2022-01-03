import pandas as pd
import plotly.express as px
import csv 
import numpy as np

def getDataSource(data_path):
        ice_cream_Sales = []
        cold_drink_sales = []
        with open(data_path)as f:
                df = csv.DictReader(f)
               
                for row in df:
                     ice_cream_Sales.append(float(row["Temperature"]))
                     cold_drink_sales.append(float(row["Ice-cream Sales"]))


        return{"x":ice_cream_Sales,"y":cold_drink_sales}

def findCorrelation(datasource):
        correlation = np.corrcoef(datasource["x"],datasource["y"])
        print("Correlation between Temp vs Ice Cream Sales ->",correlation[0,1])

def main():    
        data_path = "./data1.csv"
        datasource = getDataSource(data_path)
        findCorrelation(datasource)

main()              


