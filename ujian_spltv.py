import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

'''
x - 2y +z = 6
3x + y - 2z = 4
7x - 6y -z = 10
'''

a = np.array([[1,-2,1],[3,1,-2],[7,-6,-1]])
r = np.array([6,4,10])
b = np.linalg.solve(a,r)
print('nilai x =',b[0])
print('nilai y =',np.round(b[1]))
print('nilai z =',b[2])

'''
3d plotting
'''
fig = plt.figure('3D Plotting')
fig.set_figheight(5)
fig.set_figwidth(12)
ax = fig.add_subplot(131, projection = '3d')
x = np.array([6,0,0])
y = np.array([0,-3,0])
z = np.array([0,0,6])
ax.plot_trisurf(x,y,z, color = 'red', alpha=0.4)
ax.scatter(x,y,z)
ax.set_xlabel('nilai X')
ax.set_ylabel('nilai Y')
ax.set_zlabel('nilai Z')
ax.set_title('x-2y+z=6')
bx = fig.add_subplot(132, projection ='3d')
x1 = np.array([4/3,0,0])
y1 = np.array([0,4,0])
z1 = np.array([0,0,-2])
bx.plot_trisurf(x1,y1,z1, color = 'green', alpha=0.4)
bx.scatter(x1,y1,z1, color ='red', alpha=0.5)
bx.set_xlabel('nilai X')
bx.set_ylabel('nilai Y')
bx.set_zlabel('nilai Z')
bx.set_title('3x+y-2z=4')
cx = fig.add_subplot(133, projection ='3d')
x2 = np.array([10/7,0,0])
y2 = np.array([0,-5/3,0])
z2 = np.array([0,0,-10])
cx.set_xlabel('nilai X')
cx.set_ylabel('nilai Y')
cx.set_zlabel('nilai Z')
cx.plot_trisurf(x2,y2,z2, color = 'blue', alpha=0.4)
cx.scatter(x2,y2,z2)
cx.set_title('7x-6y-z=10')
plt.show()













# x, y = np.arange(-10,10)
# X, Y = np.meshgrid(x,y)
# Z1 = 6 - X + 2*Y
# Z2 = (3*X - 4 + Y) / 2
# Z3 = 7*X - 10 + 6*Y

# ax.plot_surface(X,Y,Z1, alpha=0.5, rstride=100, cstride=100)
# ax.plot_surface(X,Y,Z2, alpha=0.5, rstride=100, cstride=100)


# ax.plot((1,1),(-8,8),(-9,23), lw=2, c='b')
# ax.plot_surface(X,Y,Z3, alpha=0.5, facecolors='g', rstride=100, cstride=100)
# ax.plot((1,),(-2,),(3,), lw=2, c='k', marker='o')

# plt.show()