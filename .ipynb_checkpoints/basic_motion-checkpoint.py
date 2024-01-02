#!/usr/bin/env python
# coding: utf-8

# Execute the following block of code by selecting it and clicking ``ctrl + enter`` to create an ``NvidiaRacecar`` class.  

# In[1]:


from jetracer.nvidia_racecar import NvidiaRacecar

car = NvidiaRacecar()


# The ``NvidiaRacecar`` implements the ``Racecar`` class, so it has two attributes ``throttle`` and ``steering``. 
# 
# We can assign values in the range ``[-1, 1]`` to these attributes.  Execute the following to set the steering to 0.4.
# 
# > If the car does not respond, it may still be in ``manual`` mode.  Flip the manual override switch on the RC transmitter.

# In[2]:


car.steering = 0.0


# The ``NvidiaRacecar`` class has two values ``steering_gain`` and ``steering_bias`` that can be used to calibrate the steering.
# 
# We can view the default values by executing the cells below.

# In[3]:


print(car.steering_gain)


# In[4]:


print(car.steering_offset)


# The final steering value is computed using the equation
# 
# $y = a \times x + b$
# 
# Where,
# 
# * $a$ is ``car.steering_gain``
# * $b$ is ``car.steering_offset``
# * $x$ is ``car.steering``
# * $y$ is the value written to the motor driver
# 
# You can adjust these values calibrate the car so that setting a value of ``0`` moves forward, and setting a value of ``1`` goes fully right, and ``-1`` fully left.

# To set the throttle of the car to ``0.2``, you can call the following.
# 
# > Give JetRacer lots of space to move, and be ready on the manual override, JetRacer is *fast*

# In[5]:


car.throttle = -0.4


# The throttle also has a gain value that could be used to control the speed response.  The throttle output is computed as
# 
# $y = a \times x$
# 
# Where,
# 
# * $a$ is ``car.throttle_gain``
# * $x$ is ``car.throttle``
# * $y$ is the value written to the speed controller
# 
# Execute the following to print the default gain

# In[6]:


print(car.throttle_gain)


# Set the following to limit the throttle to half

# In[7]:


car.throttle_gain = -1.0


# Please note the throttle is directly mapped to the RC car.  When the car is stopped and a negative throttle is set, it will reverse.  If the car is moving forward and a negative throttle is set, it will brake.

# That's it for this notebook!
