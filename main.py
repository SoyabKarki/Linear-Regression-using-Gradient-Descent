# Gradient Descent for Linear Regression (y = mx + c)

import matplotlib.pyplot as plt  # Visualization

# Dataset
x_data = [0.0, 1.0, 2.2, 3.1]
y_data = [2.4, 5.2, 6.6, 8.0]

# Initialize parameters
m = c = m_pd = c_pd = 0.0
learning_rate = 0.01


def loss_func(x, y, w, b):

    """Loss function
    Returns derivatives of slope and intercept"""

    # squared_error = (y - (w * x + b)) ** 2
    # Take partial derivatives for slope and intercept
    slope_pd = - 2 * x * (y - (w * x + b))
    intercept_pd = - 2 * (y - (w * x + b))

    return slope_pd, intercept_pd


# Iteration
for _ in range(1000):
    slope_sse = intercept_sse = 0.0  # Sum of squared errors
    for x_val, y_val in zip(x_data, y_data):
        m_pd, c_pd = loss_func(x_val, y_val, m, c)
        slope_sse += m_pd
        intercept_sse += c_pd

    # Calculate new parameters (New parameter = Old parameter - Step size)
    m -= (slope_sse/len(x_data)) * learning_rate
    c -= (intercept_sse/len(x_data)) * learning_rate

print(f"y-intercept = {c}")
print(f"slope = {m}")

# Visualize the data
plt.figure(figsize=(8, 6))
plt.plot(x_data, y_data, 'o')

y_hat = [m * x + c for x in x_data]  # y values obtained from linear regression
plt.plot(x_data, y_hat)

plt.title('Linear Regression')
plt.xlabel('X')
plt.ylabel('Y')

plt.show()
