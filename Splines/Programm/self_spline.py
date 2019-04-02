import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
import Klasse_Spline
from mpl_toolkits.mplot3d import Axes3D

# https://github.com/scipy/scipy/blob/v0.14.0/scipy/interpolate/fitpack.py#L116


# 3D example
total_rad = 5
z_factor = 1
noise = 0

num_true_pts = 40


s_true = np.linspace(0, total_rad, num_true_pts)
x_true = np.cos(s_true)
y_true = np.sin(s_true)

x_true = [7, 5, 2, 3, 6]
y_true = [6, 8, 6, 3, 3]


tck, u = interpolate.splprep([x_true, y_true], k=3, s=0)
Spline = Klasse_Spline.Spline(tck)


x_knots, y_knots = interpolate.splev(tck[0], tck)
u_fine = np.linspace(0, 1, num_true_pts)

x_fine, y_fine = interpolate.splev(u_fine, tck)
#####################################
print(tck[1])
print('Stuetzpunkte')
print(Spline.points(np.array([0, 0.5, 1])))

fig2 = plt.figure(2)

plt.plot(tck[1][0], tck[1][1])

plt.plot(x_true, y_true, 'b')
plt.plot(x_knots, y_knots, 'ro')
plt.plot(x_fine, y_fine, 'g')
fig2.show()
plt.show()






