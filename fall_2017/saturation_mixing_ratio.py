
# coding: utf-8

# In[1]:

# saturation_mixing_ratio
#
# Computes saturation mixing, w_s, given a temperature and pressure.
#
# Steven Cavallo
# University of Oklahoma
# September 2015, 2016, 2017


# In[2]:

###########################
# imports
###########################
import matplotlib.pyplot as plt
import numpy as np
import sys
import pylab
# New import: Requires weather_modules.py and mstats.py.  
# The below says to import all functions inside weather_modules.py as wm.  So you must use "wm" to access them.
import weather_modules as wm


# In[3]:

T = 10. # degrees Celsius
p = 1000 # hPa
Rd = 287. # The dot makes it a floating point value
Rv = 461.
epsi = Rd/Rv

A = (2.53*10**(8.0))*10**(3.0) # convert to Pa
B = 5.42*10**(3.0) # Kelvin


# In[4]:

T = T + 273.15 # Convert to Kelvin
p = p * 100. # Convert to Pa
# Saturation mixing ratio
es = wm.claus_clap(T) # Pa

# Let's try the way we computed in class:
es_alt = A*np.exp(-B/T) # Calculation in SI units
print('Saturation vapor pressure is %7.2f hPa from function and %7.2f hPa from above' %(es/100.,es_alt/100.)) 



#Now we can compute saturation mixing ratio:
ws = epsi*(es/(p-es))*1000. # Convert to g/kg
print('The saturation mixing ratio at ', T-273.15, ' degrees Celsius and ', p/100, ' hPa is ', ws, ' g/kg')


# In[5]:

# Just for fun, let's check to see what the error in saturation mixing ratio is by the approximation we made to the formula.
# ws = 0.622*(es/p).  
ws_approx = epsi*(es/p)*1000.
ws_err = ws - ws_approx
perc_acc = ws_approx/ws*100.

print("The accuracy in making the approximation at %5.2f K and %5.2f hPa is %5.2f percent" %(T, p/100, perc_acc))
print('The error value is ', ws_err, ' g/kg')


# In[ ]:




# In[ ]:


