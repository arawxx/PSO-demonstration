import numpy as np
from numpy import pi, e, sqrt, exp, sin, cos


# Custom function
# global minimum = (3.182, 3.131)
# preferred domain = (0,5 / 0,5)
def f1(position):
    x = position[0]
    y = position[1]

    return (x - pi) ** 2 + (y - e) ** 2 + sin(3 * x + 1.41) + sin(4 * y - 1.73)


# Ackley function
# global minimum = (0, 0)
# preferred domain = (-32.768,32.768 / -32.768,32.768)
def f2(position):
    a = 20
    b = 0.2
    c = 2 * pi
    d = 2

    x = position[0]
    y = position[1]

    return -a * exp(-b * sqrt((1 / d) * (x ** 2 + y ** 2))) - exp((1 / d) * (cos(c * x) + cos(c * y))) + a + exp(1)


# Bukin function
# global minimum = (-10 / 1)
# preferred domain = (-15,-5 / -3,3)
def f3(position):
    x = position[0]
    y = position[1]

    return 100*sqrt(abs(y - 0.01*(x**2))) + 0.01*abs(x + 10)


# Cross-in-Tray function
# global minimum = (1.3491, 1.3491), (-1.3491, 1.3491), (1.3491, -1.3491), (-1.3491, -1.3491)
# preferred domain = (-10,10 / -10,10)
def f4(position):
    x = position[0]
    y = position[1]

    return -0.0001*(abs(sin(x)*sin(y)*exp(abs(100 - (sqrt(x**2 + y**2)/pi))))+1)**0.1


# Drop-Wave function
# global minimum = (0, 0)
# preferred domain = (-5.12,5.12 / -5.12,5.12)
def f5(position):
    x = position[0]
    y = position[1]

    return -(1 + cos(12*sqrt(x**2 + y**2))) / (0.5*(x**2 + y**2) + 2)


# Eggholder function
# global minimum = (512, 404.2319)
# preferred domain = (-512,512 / -512,512)
def f6(position):
    x = position[0]
    y = position[1]

    return -(y - 47)*sin(sqrt(abs(y + x/2 + 47))) - x*(sin(sqrt(abs(x - (y + 47)))))


# Levy function
# global minimum = (1, 1)
# preferred domain = (-10,10 / -10,10)
def f7(position):
    x = position[0]
    y = position[1]

    wx = 1 + (x - 1)/4
    wy = 1 + (y - 1)/4

    return sin(pi*wx)**2 + ((wx - 1)**2)*(1 + 10*sin(pi*wx + 1)**2) + (wy - 1)**2*(1 + sin(2*pi*wy)**2)


# Holder Table function
# global minimum = (8.05502, 9.66459), (-8.05502, 9.66459), (8.05502, -9.66459), (-8.05502, -9.66459)
# preferred domain = (-10,10 / -10,10)
def f8(position):
    x = position[0]
    y = position[1]

    return -1*abs(sin(x)*cos(y)*exp(abs(1-(sqrt(x**2 + y**2))/pi)))


# Goldstein–Price function
# global minimum = (0, -1)
# preferred domain = (-2,2 / -2,2)
def f9(position):
    x = position[0]
    y = position[1]

    return (1 + (x + y + 1)**2 * (19 - 14*x + 3*x**2 - 14*y + 6*x*y + 3*y**2)) *\
           (30 + (2*x - 3*y)**2 * (18 - 32*x + 12*x**2 + 48*y - 36*x*y + 27*y**2))


# Schwefel function
# global minimum = (420.9687, 420.9687)
# preferred domain = (-500,500 / -500,500)
def f10(position):
    x = position[0]
    y = position[1]

    return 837.9658 - (x*sin(sqrt(abs(x))) + y*sin(sqrt(abs(y))))


dictionary = {1: {'func': f1, 'x_low': 0, 'x_high': 5,
                  'y_low': 0, 'y_high': 5, 'name': 'Custom Function',
                  'minimum_x': 3.182, 'minimum_y': 3.131},

              2: {'func': f2, 'x_low': -32.768, 'x_high': 32.768,
                  'y_low': -32.768, 'y_high': 32.768, 'name': 'Ackley Function',
                  'minimum_x': 0, 'minimum_y': 0},

              3: {'func': f3, 'x_low': -15, 'x_high': -5,
                  'y_low': -3, 'y_high': 3, 'name': 'Bukin Function',
                  'minimum_x': -10, 'minimum_y': 1},

              4: {'func': f4, 'x_low': -10, 'x_high': 10,
                  'y_low': -10, 'y_high': 10, 'name': 'Cross-in-Tray Function',
                  'minimum_x': np.array([-1.3491, 1.3491]), 'minimum_y': np.array([-1.3491, 1.3491])},

              5: {'func': f5, 'x_low': -5.12, 'x_high': 5.12,
                  'y_low': -5.12, 'y_high': 5.12, 'name': 'Drop-Wave Function',
                  'minimum_x': 0, 'minimum_y': 0},

              6: {'func': f6, 'x_low': -512, 'x_high': 512,
                  'y_low': -512, 'y_high': 512, 'name': 'Eggholder Function',
                  'minimum_x': 512, 'minimum_y': 404.2319},

              7: {'func': f7, 'x_low': -10, 'x_high': 10,
                  'y_low': -10, 'y_high': 10, 'name': 'Levy Function',
                  'minimum_x': 1, 'minimum_y': 1},

              8: {'func': f8, 'x_low': -10, 'x_high': 10,
                  'y_low': -10, 'y_high': 10, 'name': 'Holder Table Function',
                  'minimum_x': np.array([-8.05502, 8.05502]), 'minimum_y': np.array([-9.66459, 9.66459])},

              9: {'func': f9, 'x_low': -2, 'x_high': 2,
                  'y_low': -2, 'y_high': 2, 'name': 'Goldstein–Price Function',
                  'minimum_x': 0, 'minimum_y': -1},

              10: {'func': f10, 'x_low': -500, 'x_high': 500,
                   'y_low': -500, 'y_high': 500, 'name': 'Schwefel Function',
                   'minimum_x': 420.9687, 'minimum_y': 420.9687}
              }
