import pandas as pd
import numpy as np



def preprocessing_input_data(input_data):

    orientations = ['N', 'E', 'S', 'W']

    new_data = {f'orientation_{o}': 0 for o in orientations}

    if 'orientation' in input_data:
        selected_orientation = input_data['orientation'][0].upper()  # Get first letter and uppercase it
        if f'orientation_{selected_orientation}' in new_data:
            new_data[f'orientation_{selected_orientation}'] = 1  # Set the correct orientation to 1

    for key, value in input_data.items():
        if key != 'orientation': 
            new_data[key] = value

    return new_data
    