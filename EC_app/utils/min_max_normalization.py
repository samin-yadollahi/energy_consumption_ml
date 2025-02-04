from pathlib import Path
import joblib, os
import numpy as np

def input_data_normalization(input_data):

    scaler_dir = os.path.join(os.path.dirname(__file__), "min_max_scaler.pkl")
    min_max_scaler = joblib.load(scaler_dir)

    dict_to_array = np.array(list(input_data.values()))
    dict_to_array = dict_to_array.reshape(1, 11)
    print(dict_to_array)
    print(type(dict_to_array))
    scaled_data = min_max_scaler.transform(dict_to_array)

    return scaled_data

