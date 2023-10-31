import cv2
from BezierPolynomial import BezierPolynomial
from Visualize import Visualize
from ImagePointSelector import ImagePointSelector

background_image_path = 'maze_image.png'

image = cv2.imread(background_image_path)

selector = ImagePointSelector(background_image_path)
selected_points = selector.select_points()

print(selected_points)
bezier = BezierPolynomial(selected_points[0], selected_points[1], selected_points[2], selected_points[3])


visualizer = Visualize([(bezier.linearX, bezier.linearY)
                        ,(bezier.quadraticX, bezier.quadraticY)
                        ,(bezier.cubicX, bezier.cubicY)],
                        background_image_path=background_image_path)
visualizer.plot()
