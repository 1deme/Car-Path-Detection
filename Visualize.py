import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

class Visualize:
    def __init__(self, bezier_functions, plot_range=250, background_image_path=None):
        self.bezier_functions = bezier_functions
        self.plot_range = plot_range
        self.background_image_path = background_image_path

    def plot(self, num_points=100):
        t_values = np.linspace(0, 1, num_points)

        fig, ax = plt.subplots()
        
        if self.background_image_path:
            background_image = Image.open(self.background_image_path)
            ax.imshow(background_image, extent=[-self.plot_range, self.plot_range, -self.plot_range, self.plot_range])

        for func in self.bezier_functions:
            if func.cubicX is not None:
                x_values = [func.cubicX(t) for t in t_values]
                y_values = [func.cubicY(t) for t in t_values]
            elif func.quadraticX is not None:
                x_values = [func.quadraticX(t) for t in t_values]
                y_values = [func.quadraticY(t) for t in t_values]
            else:
                x_values = [func.linearX(t) for t in t_values]
                y_values = [func.linearY(t) for t in t_values]

            ax.plot(x_values, y_values, linewidth=2)

        ax.axis('off')
        ax.set_xlim(-self.plot_range, self.plot_range)
        ax.set_ylim(-self.plot_range, self.plot_range)
        plt.show()
