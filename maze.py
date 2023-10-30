import cv2
from bezier import BezierPolynomial
from visualize import Visualize
from imagePointSelector import ImagePointSelector


image_path = 'maze_image.png'  
image = cv2.imread(image_path)
image_height, image_width, _ = image.shape

common_width = 100 
common_height = 100


selector = ImagePointSelector(image_path)
selected_points = selector.select_points()

print(selected_points)
bezier = BezierPolynomial(selected_points[0], selected_points[1], selected_points[2], selected_points[3])

visualizer = Visualize([(bezier.linearX, bezier.linearY)
                        ,(bezier.quadraticX, bezier.quadraticY)
                        ,(bezier.cubicX, bezier.cubicY)])
visualizer.plot()
