import numpy as np
import pandas as pd

# RMS Titanic data visualization code
# from titanic_visualizations import survival_stats
from IPython.display import display

# Load the dataset
in_file = 'titanic_data.csv'
full_data = pd.read_csv(in_file)

# Store the 'Survived' feature in a new variable and remove it from the dataset
outcomes = full_data['Survived']
data = full_data.drop('Survived', axis = 1)

# Treat the passenger's 'Pclass' as a categorical variable
data['Pclass'] = data['Pclass'].astype(str)

# Show the new dataset with 'Survived' removed
display(data.head())


def accuracy_score(truth, pred):
    """ Returns accuracy score for input truth and predictions. """

    # Ensure that the number of predictions matches number of outcomes
    if len(truth) == len(pred):

        # Calculate and return the accuracy as a percent
        return "Predictions have an accuracy of {:.2f}%.".format((truth == pred).mean()*100)

    else:
        return "Number of predictions does not match number of outcomes!"

# # Test the 'accuracy_score' function
# predictions = pd.Series(np.ones(5, dtype = int))
# print accuracy_score(predictions, outcomes[:5])

def predictions_1(data):
    """ Model with one feature:
            - Predict a passenger survived if they are female. """

    predictions = []
    for _, passenger in data.iterrows():

        # Remove the 'pass' statement below
        # and write your prediction conditions here
        survive = 0
        if passenger['Sex'] == 'female' or passenger['Age'] < 10:
            survive = 1
            
        predictions.append(survive)

    # Return our predictions
    return pd.Series(predictions)

# Make the predictions
predictions = predictions_1(data)
print accuracy_score(outcomes, predictions)

