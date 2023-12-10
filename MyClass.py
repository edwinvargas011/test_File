import numpy as np
import matplotlib.pyplot as plt
import pandas
import sklearn
from sklearn.preprocessing import StandardScaler
import math

t_ex = np.ones((2,3));
random_num=np.random.randint(10);
size=np.size(t_ex);
dim=np.ndim(t_ex);
print(t_ex);
print(np.multiply(t_ex,random_num));
print(np.sum(dim, axis=0));
print("Edwin"+str(input("> input: ")));
print([x for x in [elem for elem in np.asarray(t_ex)]]);

print(t_ex);
for i in range(0,10,1):
    print(i,end="\n",sep="-");


# Datos de ejemplo
categorias = ['A', 'B', 'C', 'D']
valores1 = [5, 8, 2, 6]
valores2 = [3, 2, 7, 3]
valores3 = [4, 6, 2, 8]

# Posiciones de las barras
posiciones = np.arange(len(categorias))

# Ancho de las barras
ancho = 0.2

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Crear las barras agrupadas


bar1 = ax.bar(posiciones - ancho, valores1, ancho, label='Valores 1')
bar2 = ax.bar(posiciones, valores2, ancho, label='Valores 2')
bar3 = ax.bar(posiciones + ancho, valores3, ancho, label='Valores 3')

# Etiquetas del eje x y título
ax.set_xticks(posiciones)
ax.set_xticklabels(categorias)
ax.set_xlabel('Categorías')
ax.set_ylabel('Valores')
ax.set_title('Gráfica de Barras Agrupadas')

# Leyenda
ax.legend()

# Mostrar la gráfica
plt.show()