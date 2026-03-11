# Stock-Price-Prediction-using-historical-data-w-simple-Linear-Regression
Stock Price Predictor (Linear Regression)A lightweight Python application that utilizes Scikit-Learn to predict future stock prices based on historical trends using simple Linear Regression.## Project OverviewThis script demonstrates a basic machine learning pipeline:Data Creation: Generates a sample dataset of stock "Close" prices.Preprocessing: Converts date strings into ordinal integers for model compatibility.Model Training: Uses LinearRegression to find the line of best fit through the data.Evaluation: Calculates Mean Squared Error (MSE) and $R^2$ score to measure accuracy.Visualization: Plots actual vs. predicted values using Matplotlib.Forecasting: Predicts the stock price for a specific future date.## Getting Started### PrerequisitesEnsure you have Python installed along with the following libraries:pandasscikit-learnmatplotlibYou can install them via pip:Bashpip install pandas scikit-learn matplotlib
### Running the ScriptSave the code as stock.py.Run the script from your terminal:Bashpython stock.py
## Code StructureData Handling: The script uses a dictionary-to-DataFrame approach with pd.date_range.Feature Engineering: The Date column is mapped to ordinals using pd.Timestamp.toordinal to allow the linear model to process time as a continuous numerical feature.Splitting: Data is split into 80% training and 20% testing sets.Output: The script prints the predicted price for 2026-01-11 and displays a comparison graph.## Example OutputPlaintextStock Price Data:
     Date  Close
0  739617    150
1  739618    151
...
Mean Squared Error: 0.0
R2 Score: 1.0
Predicted stock price: $160.00
