from data import data_clean
import numpy as np
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pickle
scaler = StandardScaler()

def model_bulding():

    X , Y = data_clean()

    classifier = classifier = svm.SVC(kernel='linear')

    

    X_train , X_test , Y_train , Y_test = train_test_split(X , Y , test_size=0.2 ,stratify=Y , random_state=2)

    classifier.fit(X_train, Y_train)

    X_train_prediction = classifier.predict(X_train)
    train_data_accuracy = accuracy_score(X_train_prediction,Y_train)
    #print(f"The accuarcy on the training data is {train_data_accuracy}")

    #accuracy score of test_data

    X_test_prediction = classifier.predict(X_test)
    test_data_Accuarcy = accuracy_score(X_test_prediction,Y_test)
    #print(f"The Test accuracy is {test_data_Accuarcy}")


    return classifier





def predict_data(input_data):

    model = model_bulding()

    numpy_array = np.asarray(input_data)
    reshaped_data = numpy_array.reshape(1,-1)

    scaler.fit(reshaped_data)
    std_data = scaler.transform(reshaped_data)

    prediction = model.predict(std_data)
    print(prediction)


    if (prediction == 0):
        print('The person is not diabetic')
    else:
        print('The Person is diabetic')

    file_name = 'Diabetes_model.pkl'
    pickle.dump(model,open(file_name,'wb'))



