import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


n0 = 100 #Initial cell number.
r = 0.1  # Intrinsic growth rate
t = np.linspace(0,250) #Range of generation
k = 1e5 # Carrying capacity

def main():
    # logistic equation of bacterial growth.
    N = (k/(1+((k - n0)/n0)*np.exp(-r*t)))

    plt.grid()
    plt.title("Bacterial Growth Curve \n(Extended logistic equation)")
    plt.xlabel("TIme")
    plt.ylabel("log of bacterial cells")
    plt.tight_layout()

    plt.scatter(t,N)
    plt.show()
if __name__ == "__main__":
    main()