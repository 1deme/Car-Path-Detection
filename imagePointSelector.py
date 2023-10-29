import cv2

class ImagePointSelector:
    def __init__(self, image_path):
        self.image_path = image_path
        self.coordinate_list = []

    def click_event(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            image = cv2.imread(self.image_path)
            height, width, _ = image.shape

            center_x = width // 2
            center_y = height // 2
            adjusted_x = x - center_x
            adjusted_y = center_y - y 

            print(f"Adjusted Coordinates (x, y): ({adjusted_x}, {adjusted_y})")
            self.coordinate_list.append((adjusted_x, adjusted_y))
    
    def select_points(self):
        image = cv2.imread(self.image_path)
        cv2.imshow('Image', image)
        cv2.setMouseCallback('Image', self.click_event)

        while True:
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break

        cv2.destroyAllWindows()
        return self.coordinate_list
