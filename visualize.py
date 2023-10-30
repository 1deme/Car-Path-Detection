import numpy as np
import matplotlib.pyplot as plt

class Visualize:
    def __init__(self, bezier_functions, plot_range=250):
        self.bezier_functions = bezier_functions
        self.plot_range = plot_range

    def plot(self, num_points=100):
        t_values = np.linspace(0, 1, num_points)
        for func in self.bezier_functions:
            x_values = [func[0](t) for t in t_values]
            y_values = [func[1](t) for t in t_values]
            plt.plot(x_values, y_values, linewidth=2)
        
        plt.axis('off')
        plt.xlim(-self.plot_range, self.plot_range)
        plt.ylim(-self.plot_range, self.plot_range)
        plt.show()