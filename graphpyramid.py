'''copy this to graph a 3d function'''

import pylab
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

#number of edges on base
n = 5
p = lambda x: 1/np.cos((2.0/n) * np.arcsin(np.sin((n/2.0)*x)))
#parameterized sin function for the edge of the square
psin = lambda x: p(x)*np.sin(x)
pcos = lambda x: p(x)*np.cos(x)

width = 1
height = 8
mesh_size = 80
theta = np.linspace(0, 2*np.pi, mesh_size)

x = pcos(theta)
y = psin(theta)

X, Y = np.meshgrid(x, y)
Z = np.linspace(0, 0, mesh_size)

top = np.array([0, 0, height])

pyramid_mesh = 30.0
surf2 = np.ndarray((mesh_size*pyramid_mesh, 3))
for i in range(0, mesh_size):
    for j in range(0, int(pyramid_mesh)):
        surf2[i*pyramid_mesh+j,:] = np.array([x[i], y[i], 0]) + j/pyramid_mesh*(top - np.array([x[i], y[i], 0]))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#ax.plot_wireframe(X, Y, Z, rstride=1, cstride=1)
ax.plot_wireframe(x, y, Z, color='k')
ax.plot_wireframe(surf2[:,0], surf2[:,1], surf2[:,2], color='k')
#ax.grid('off')
#ax.axis('off')
plt.show()
#plt.savefig('{0}.png'.format(str(img).zfill(4)), bbox_inches='tight')
