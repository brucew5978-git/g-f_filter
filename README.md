# Motivation 

With real world sensor data, various factors - such as sensor inaccuracies, or random error, can seriously impacted the decision making of the controller system. 
However, filters can be used to combine both sensor data with prediction data from residual memory to decrease the effect of sensor errors. 

THe G-H or Alpha-Beta filter is a simplified filter for control applications, and is closely related to the more advanced Kalman filters.

This repo aims to explore and understand the theory behind G-F Filters and what makes them so affective at balancing sensor measurement and system prediction.

# Usage

This repo contains short explanation of g-h filter workings as well as a code file for experimentation.
Refer to algorithm_theory.md for theory and g-h_filter.py for filter's demonstration

## Source: 
- https://github.com/rlabbe/Kalman-and-Bayesian-Filters-in-Python/blob/master/01-g-h-filter.ipynb
- https://en.wikipedia.org/wiki/Alpha_beta_filter
