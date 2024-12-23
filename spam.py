import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load the dataset
df = pd.read_csv('mail_data.csv')
print(df)

# Handle missing values
data = df.where(pd.notnull(df), '')

# Display basic information about the dataset
data.head()
data.info()
data.shape

# Encode the Category column
data.loc[data['Category'] == 'spam', 'Category'] = 0
data.loc[data['Category'] == 'ham', 'Category'] = 1

# Split the dataset into features and labels
X = data['Message']
y = data['Category']
print(X)
print(y)

# Split the dataset into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.3, random_state=42)
print(X.shape)
print(X_train.shape)
print(X_test.shape)
print(y.shape)
print(Y_train.shape)
print(Y_test.shape)

# Feature extraction
feature_extraction = TfidfVectorizer(min_df=1, stop_words='english', lowercase=True)
X_train_feature = feature_extraction.fit_transform(X_train)
X_test_feature = feature_extraction.transform(X_test)

# Convert the labels to integers
Y_train = Y_train.astype('int')
Y_test = Y_test.astype('int')

print(X_train)
print(X_train_feature)

# Create and train the Logistic Regression model
model = LogisticRegression()
model.fit(X_train_feature, Y_train)

# Make predictions on the training set
train_predictions = model.predict(X_train_feature)
train_accuracy = accuracy_score(Y_train, train_predictions)
print(f'Training Accuracy: {train_accuracy}')

# Make predictions on the test set
test_predictions = model.predict(X_test_feature)
test_accuracy = accuracy_score(Y_test, test_predictions)
print(f'Test Accuracy: {test_accuracy}')
