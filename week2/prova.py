import numpy as np
from numpy import random
import matplotlib.pyplot as plt

def arr_n(n):
  return np.reshape(np.linspace(0,1,n), (1,n))

nb = int(input("Inserisci un numero\n"))
new_matrix = arr_n(nb)
tupla = (new_matrix,)*10
matrix = np.concatenate(tupla)
plt.imshow(matrix)
plt.matshow(matrix)