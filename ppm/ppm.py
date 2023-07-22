import pickle
import numpy as np
import json

# Load the columns_ppm.json file to get the mapping of locations to indices
with open("columns_ppm.json") as f:
    columns = json.load(f)

# Provide the column names or features manually
X_columns = ["square_feet", "bathroom", "bhk"] + columns['data_col']

def predict_price(location_name, sqft, bath, bhk):
    with open('realestate/price_prediction_model.pickle', 'rb') as f:
        model_module = pickle.load(f)

    # Initialize x array with zeros
    x = np.zeros(len(X_columns))

    # Set values for square_feet, bathroom, and bhk
    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    # Check if the location name is present in the columns dictionary
    if location_name in columns['data_col']:
        loc_index = X_columns.index(location_name) + 3  # Add 3 to adjust for the first 3 columns
        x[loc_index] = 1
    else:
        # Handle the case when the location is not found in the column names
        # You can decide what to do in this case, for example, set a default location value
        pass

    return model_module.predict([x])[0]
