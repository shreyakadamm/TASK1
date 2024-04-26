import matplotlib.pyplot as plt
import numpy as np
data = np.random.randn(500)
plt.hist(data, bins=10, color='skyblue'
         , edgecolor='black')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()