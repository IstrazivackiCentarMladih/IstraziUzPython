import matplotlib.pyplot as plt
import random
import numpy as np

def calculate_projectile_motion_points(vx, vy, h0=0, dt=0.01, noise=0):
    data = {'x': [], 'y': [], 't': []}

    g = 9.81

    # initial conditions
    x0 = x = 0
    y0 = y = h0
    t = 0

    while y >= 0:
        data['x'].append(x)
        data['y'].append(y)
        data['t'].append(t)

        t += dt
        x = x0 + vx*t + (random.random()-0.5)*noise*vx
        y = y0 + vy*t - 0.5*9.81*t**2 + (random.random()-0.5)*noise*vy

    return data


def plot_data(theory, simulation=None):
    fig, ax = plt.subplots(2, 2)
    ax[-1, -1].axis('off') # we will use only 3 out of 4 plots

    ax[0][0].plot(theory['x'], theory['y'], 'r--', label='y vs x theory')
    ax[0][0].plot(simulation['x'], simulation['y'], 'bx', label='y vs x simulation')
    ax[0][0].set_title('Projectile path')
    ax[0][0].set_xlabel('x(m)')
    ax[0][0].set_ylabel('y(m)')
    
    ax[0][1].plot(theory['t'], theory['y'], 'r--', label='y vs t theory')
    ax[0][1].plot(simulation['t'], simulation['y'], 'bx', label='y vs t simulation')
    ax[0][1].set_title('Vertical motion of projectile in time')
    ax[0][1].set_xlabel('x(m)')
    ax[0][1].set_ylabel('y(m)')

    ax[1][0].plot(theory['t'], theory['x'], 'r--', label='x vs t theory')
    ax[1][0].plot(simulation['t'], simulation['x'], 'bx', label='x vs t simulation')
    ax[1][0].set_title('Horizontal motion of projectile in time')
    ax[1][0].set_xlabel('x(m)')
    ax[1][0].set_ylabel('y(m)')
    
    plt.show()


vx = 10
vy = 20
h0 = 5

theory = calculate_projectile_motion_points(vx, vy, h0)
simulation = calculate_projectile_motion_points(vx, vy, h0, dt = 0.1, noise=0.5)
plot_data(theory, simulation)
