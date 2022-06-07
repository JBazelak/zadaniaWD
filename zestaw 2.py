import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image



fig, (ax) = plt.subplots(figsize=(10,5))

x = np.arange(-6,7,1)
y= 20*np.sin(x)

# ax.set(xticks=np.arange(-6,7, 1),
#        yticks=np.arange(-30,31,10))
ax.plot(x, y)



plt.show()