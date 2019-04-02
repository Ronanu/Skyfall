import numpy as np


class Spline:
    def __init__(self, tck):
        self.tck = tck
        self.cx = tck[1][0]
        self.cy = tck[1][1]

    def cont_p(self, i):
        return np.array([self.cx[i], self.cy[i]])

    def f(self, t):
        t_max = len(self.cx)-3
        i = 0
        while i <= t_max:
            f_ = (1-t)**3*self.cont_p(0)+3*t*(1-t)**2*self.cont_p(1)+3*t*(1-t)**2*self.cont_p(2)+t**3*self.cont_p(3)
        return f_, t_max

    def points(self, tt):
        pp = []
        for x in tt:
            pp.append(self.f(x))
        return pp
