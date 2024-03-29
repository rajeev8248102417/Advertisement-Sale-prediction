#Installing Python Libraries
!pip install numpy
!pip install pandas

#Importing Python Libraries
import numpy as np
import pandas as pd

#Choose Dataset file from Local Directory
from google.colab import files
uploaded = files.upload()

#Load dataset into Colab
dataset = pd.read_csv('DigitalAd_dataset.csv')
print(dataset)

#Summarize the data

#shape of data
dataset.shape

#header of data
dataset.head()

#tail of data
dataset.tail()

#segregating dataset into X & Y values
X = dataset.iloc[:,:-1]
Y = dataset.iloc[:,-1]

#splitting dataset into train and test
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size= 0.25,random_state= 0)

#future scaling
#we scale our data to make all the features contribute equally to the result
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

#Training the algorithm
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(random_state = 0)
model.fit(x_train, y_train)

#predict for all test data
y_pred = model.predict(x_test)
concatenated_data = np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.values.reshape(len(y_test), 1)), axis=1)
result_df = pd.DataFrame(concatenated_data, columns=['Predicted', 'Actual'])
print(result_df)


# *Evaluating Model - CONFUSION MATRIX
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix: ")
print(cm)
print("Accuracy of the Model: {0}%".format(accuracy_score(y_test, y_pred)*100))


# *Predicting, wheather new customer with Age & Salary will Buy or Not
age = int(input("Enter New Customer Age: "))
sal = int(input("Enter New Customer Salary: "))
newCust = [[age,sal]]
result = model.predict(sc.transform(newCust))
print(result)
if result == 1:
  print("Customer will Buy")
else:
  print("Customer won't Buy")
