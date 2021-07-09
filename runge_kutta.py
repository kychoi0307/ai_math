import matplotlib.pyplot as plt
import numpy as np

a = np.arange(-100, 100, 0.1)


def main():
    plt.plot(a, np.cos(a))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


if __name__ == '__main__':
    main()
