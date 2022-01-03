
import plotly.express as px
import csv 
import numpy as np

def getDataSource(data_path):
        marks_in_percentage = []
        days_present = []
        with open(data_path)as f:
                df = csv.DictReader(f)
                for row in df:
                     marks_in_percentage.append(float(row["Marks In Percentage"]))
                     days_present.append(float(row["Days Present"]))

        return{"x":marks_in_percentage,"y":days_present}

def findCorrelation(datasource):
        correlation = np.corrcoef(datasource["x"],datasource["y"])
        print("Correlation between Present days vs Marks in Percentage ->",correlation[0,1])

def main():    
        data_path = "./data3.csv"
        datasource = getDataSource(data_path)
        findCorrelation(datasource)

main()              


