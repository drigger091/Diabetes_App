
import numpy as np
from sklearn.preprocessing import StandardScaler

from model import model_bulding , predict_data
from data import data_clean

features = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']

input_data = []

for feature_name in features:
    while True:
        try:
            val = float(input(f"Enter {feature_name}: "))
            # Add constraints here
            if feature_name == 'Pregnancies':
                if val < 0:
                    print("Number of pregnancies cannot be that much. Please enter a valid number.")
                    continue
            elif feature_name == 'Glucose':
                if val < 0 or val > 300:  
                    print("Glucose level should be between 0 and 300. Please enter a valid number.")
                    continue
            
            elif feature_name == 'Age':
                if val < 0 or val > 120:  
                    print("Age should be between 0 and 120. Please enter a valid number.")
                    continue
            
            elif feature_name == "Bloodpressure":
                if val < 60 or val >140:
                    print("Blood  Pressure should be with in 60 to 140")
                    continue
            
            
            input_data.append(val)
            break  
        except ValueError:
            print("Invalid input. Please enter a valid number.")

input_data = np.array(input_data).reshape(1, -1)


predict_data(input_data)


