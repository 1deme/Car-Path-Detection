import cv2

class ImagePointSelector:
    def __init__(self, image_path, max_dimension=500):
        self.image_path = image_path
        self.max_dimension = max_dimension
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
        # Resize the image before displaying it
        resized_image = self.resize_image(self.image_path, self.max_dimension)
        cv2.imshow('Image', resized_image)
        cv2.setMouseCallback('Image', self.click_event)

        while True:
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break

        cv2.destroyAllWindows()
        return self.coordinate_list

    @staticmethod
    def resize_image(image_path, max_dimension):
        image = cv2.imread(image_path)
        original_height, original_width, _ = image.shape

        scale = min(max_dimension / original_width, max_dimension / original_height)
        new_width = int(original_width * scale)
        new_height = int(original_height * scale)
        resized_image = cv2.resize(image, (new_width, new_height))

        return resized_image
