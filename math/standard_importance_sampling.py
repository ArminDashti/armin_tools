# Code generated by Microsoft Copilot

import numpy as np
from scipy.stats import norm

# Define the target distribution p(x) as standard normal distribution
def p(x):
    return norm.pdf(x, 0, 1)

# Define the proposal distribution q(x) as normal distribution with mean 5 and variance 4
def q(x):
    return norm.pdf(x, 5, 2)

# Define the function f(x) to be the square of x
def f(x):
    return x**2

# Define the importance sampling function
def importance_sampling(num_samples):
    samples = []
    weights = []
    
    # Draw samples from the proposal distribution q(x)
    for _ in range(num_samples):
        x_i = np.random.normal(5, 2)
        w_i = p(x_i) / q(x_i)
        
        # Calculate the weighted sample
        weighted_sample = f(x_i) * w_i
        
        # Store the samples and weights
        samples.append(weighted_sample)
        weights.append(w_i)
    
    # Calculate the weighted average
    weighted_average = np.sum(samples) / np.sum(weights)
    
    return weighted_average

# Number of samples to draw
num_samples = 10000

# Estimate the expected value using importance sampling
estimated_value = importance_sampling(num_samples)

# Print the estimated value
print(f"The estimated expected value using importance sampling is: {estimated_value}")
