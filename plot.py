import pandas as pd
import matplotlib.pyplot as plt
Y=pd.read_csv('filename.csv',header=None)
Y=Y.values
Y=Y.astype('float32')
Y=Y.reshape(1,28,28,1)
plt.imshow(Y.reshape(28,28),cmap='gray')
plt.show()
