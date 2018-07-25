
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
import numpy as np
get_ipython().magic(u'matplotlib inline')
distance= [ 4.469, 3.737, 0.019,  0.959, 0.0078, 0.0070]
x = np.random.normal(size = 1000)
plt.hist(x, normed=True, bins=30)
plt.ylabel('distance');

