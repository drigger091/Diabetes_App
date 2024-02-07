import pandas as pd
import numpy as mp
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings("ignore")


# reading the dataset 



def data_clean():

    df = pd.read_csv("F:\Diabetes app\diabetes.csv")

    X = df.drop(columns="Outcome",axis=1)
    Y = df[['Outcome']]

    scaler = StandardScaler()
    scaler.fit(X)

    standard_data = scaler.transform(X)
    X = standard_data

    return X , Y


    


