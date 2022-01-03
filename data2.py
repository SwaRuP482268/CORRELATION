
import plotly.express as px
import csv 
import numpy as np

def getDataSource(data_path):
        size_of_tv = []
        avg_timespent = []
        with open(data_path)as f:
                df = csv.DictReader(f)
                for row in df:
                     size_of_tv.append(float(row["Size of TV"]))
                     avg_timespent.append(float(row["\tAverage time spent watching TV in a week"]))

        return{"x":size_of_tv,"y":avg_timespent}

def findCorrelation(datasource):
        correlation = np.corrcoef(datasource["x"],datasource["y"])
        print("Correlation between Size of TV vs Avg Time Spent ->",correlation[0,1])

def main():    
        data_path = "./data2.csv"
        datasource = getDataSource(data_path)
        findCorrelation(datasource)

main()              


