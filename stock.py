#Import Necessary Libraries
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

#Sample Historical stock price data
data = {
	'Date': pd.date_range(start='2026-01-01', periods=10, freq='D'),
	'Close': [150, 151, 152, 153, 154, 155, 156, 157, 158, 159]
}

#Convert the Dataset into Dataframe
df = pd.DataFrame(data)

df['Date'] = df['Date'].map(pd.Timestamp.toordinal)

print("Stock Price Data:")
print(df.head())

X = df[['Date']]
y = df['Close']

#Splitting the Datasets into training & testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\nMean Squared Error: {mse}")
print(f"\nR2 Score: {r2}")

plt.figure(figsize=(10, 6))
plt.plot(X_test, y_test, label="Actual Stock Prices", marker='o')
plt.plot(X_test, y_pred, label="Predicted Stock Prices", marker='x')
plt.title("Actual vs Predicted Stock Prices")
plt.xlabel("Date (Ordinal)")
plt.ylabel("Stock Price ($)")
plt.legend()
plt.show()

future_date = pd.Timestamp('2026-01-11').toordinal()

future_date = pd.DataFrame({'Date': [future_date]})

predicted_price = model.predict(future_date)
print(f"Predicted stock price: ${predicted_price[0]:.2f}")