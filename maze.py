import cv2
from bezier import BezierPolynomial
from visualize import Visualize
from imagePointSelector import ImagePointSelector


image_path = 'maze.png'  
image = cv2.imread(image_path)
image_height, image_width, _ = image.shape

common_width = 100 
common_height = 100


selector = ImagePointSelector('maze.png')
selected_points = selector.select_points()

transformed_points = []
for image_x, image_y in selected_points:
    common_x = image_x / 3
    common_y = image_y / 3
    transformed_points.append((common_x, common_y))

bezier = BezierPolynomial(transformed_points[0], transformed_points[1])

visualizer = Visualize([(bezier.linearX, bezier.linearY)])
visualizer.plot()
