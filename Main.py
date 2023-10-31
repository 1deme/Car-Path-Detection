import cv2
from BezierPolynomialArray import BezierPolynomialArray
from Visualize import Visualize
from ImagePointSelector import ImagePointSelector

background_image_path = 'maze_image.png'

image = cv2.imread(background_image_path)

selector = ImagePointSelector(background_image_path)
selected_points = selector.select_points()

beziers = BezierPolynomialArray(selected_points)

visualizer = Visualize(beziers.bezier_array,background_image_path=background_image_path)
visualizer.plot()
