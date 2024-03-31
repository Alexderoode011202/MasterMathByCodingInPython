import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
from typing import Tuple

# Define your function
x = sym.symbols('x')
func1 = 2*x + 2

def plot_function(func_list: list, xlim: Tuple[int, int], ylim: Tuple[int, int]) -> None:
    """Only plots a function in a basic way"""
    x_vals = np.linspace(xlim[0], xlim[1], 101)
    func_dict = {}
    for func in func_list:
        y_vals = []
        for num in x_vals:
            y_vals.append(func.subs({x:num}))
        y_vals = np.array(y_vals)
        func_dict[sym.latex(func)] = y_vals
    
    for func in func_dict:
        plt.plot(x_vals, func_dict[func], label="$%s$"%(func))
        
    plt.plot((xlim[0], xlim[1]), (0, 0), color="black", linestyle="--")
    plt.plot((0, 0), (ylim[0], ylim[1]), color="black", linestyle="--")
    
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    
    plt.show()

