import matplotlib.pyplot as plt
import numpy as np

def circle_protter(R=3):
    alpha = np.arange

    x = R * np.cos(alpha)
    y = R * np.sin(alpha)

    plt.plot(x, y, ls= '--', lw =3)
    plt.axis('equal')
    plt.savefig('fig_l.png')

if __name__=='__main__':
    circle_plotter()

