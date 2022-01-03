
import plotly.express as px
import csv 
import numpy as np

def getDataSource(data_path):
        Coffee_in_ml = []
        sleep_in_hours = []
        with open(data_path)as f:
                df = csv.DictReader(f)
                for row in df:
                     Coffee_in_ml.append(float(row["Coffee in ml"]))
                     sleep_in_hours.append(float(row["sleep in hours"]))

        return{"x":Coffee_in_ml,"y":sleep_in_hours}

def findCorrelation(datasource):
        correlation = np.corrcoef(datasource["x"],datasource["y"])
        print("Correlation between Hours sleeped vs Coffee in ml ->",correlation[0,1])

def main():    
        data_path = "./data4.csv"
        datasource = getDataSource(data_path)
        findCorrelation(datasource)

main()              


