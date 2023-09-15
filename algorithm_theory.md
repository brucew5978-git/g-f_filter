# G-H Filters

For the rest of this file, we will define the "state" to be the actual position or value of object being measured by a sensor. 

What makes the g-h filter unique compared to other software filters is the combination of the gain parameter - g, and the smoothing parameter - h
Both g and h factors are usually values between 0 and 1 where:  

h = smoothing parameter, which is the factor that impacts the relationship between measured and prediction state - such as an object's displacement
g = gain parameter, is the factor that controls the impact between measured and predicted change in state - such as an object's velocity

As a prediction will always be involved, g-h filters also requires a initial guess about the state to be used as the prediction value.

## Algorithm

The g-h filter algorithm can be broken down as follows:

### initialize:
1. initialize filter and system values
2. initialize belief in the state

### predict: 
1. use previous estimation to predict state of next step
2. adjust belief about the system to account for uncertainty in prediction

### update:
1. get a measurement 
2. calculate residual between estimated state and measurement
3. use g and h factors to ensure new estimates on within range of the residual factor

This algorithm is also implemented in the g-h_filter.py file

## Benefits

THe main benefits of using the 

