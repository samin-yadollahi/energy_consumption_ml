def output_labeling(predicted_data):

    if predicted_data > 160:
        return "unacceptable"
    
    elif (predicted_data > 100) and (predicted_data <= 160):
        return "EC"
    
    elif (predicted_data > 80) and (predicted_data <= 100):
        return "EC_plus"
    
    elif (predicted_data> 25) and (predicted_data <= 80):
        return "EC_plus_plus"
    
    else:
        return "ECNZ"