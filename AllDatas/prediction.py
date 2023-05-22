def predict_next_values(values, num_predictions, num_values_to_average):
    # Make sure we have enough values to use for prediction
  if len(values) < num_values_to_average:
    raise ValueError(f"Need at least {num_values_to_average} values to make predictions")
  
  # Initialize a list to store the predicted values
  predictions = []
  
  # Iterate over the number of predictions we want to make
  for i in range(num_predictions):
    # Predict the next value by taking the average of the last num_values_to_average values
    prediction = sum(values[-num_values_to_average:]) / num_values_to_average
    # Add the prediction to the list of predictions
    predictions.append(prediction)
    # Add the prediction to the list of values so we can use it for the next prediction
    values.append(prediction)
    
  return predictions

values = [11, 12.21, 13.42, 12.74, 15.64, 18.43, 20.43, 18.3]
print(predict_next_values(values, 30, 8))