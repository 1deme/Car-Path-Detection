import math
from BezierPolynomial import BezierPolynomial

class BezierPolynomialArray:
    def __init__(self, points):
        self.bezier_array = []
        self.process_points(points)

    def process_points(self, points):
        start = 0
        while start < len(points):
            if start + 3 < len(points):
                if self.calculate_degree(points, start, start + 3) == "cubic":
                    self.bezier_array.append(BezierPolynomial(points[start], points[start + 1], points[start + 2], points[start + 3]))
                    start += 4
                elif start + 2 < len(points):
                    if self.calculate_degree(points, start, start + 2) == "quadratic":
                        self.bezier_array.append(BezierPolynomial(points[start], points[start + 1], points[start + 2]))
                        start += 3
                else:
                    self.bezier_array.append(BezierPolynomial(points[start], points[start + 1]))
                    start += 2
            else:
                self.bezier_array.append(BezierPolynomial(points[start], points[start + 1]))
                start += 2

    def calculate_degree(self, points, start, end):
        angle_sum = 0
        for i in range(start, end):
            if i >= len(points) or start >= len(points):
                break

            if points[i][0] == points[start][0]:
                slope1 = 0
                continue

            slope1 = (points[i][1] - points[start][1]) / (points[i][0] - points[start][0])
            slope2 = (points[end][1] - points[i][1]) / (points[end][0] - points[i][0])
            angle = abs(math.degrees(math.atan(slope1) - math.atan(slope2)))
            angle_sum += angle

        if angle_sum < 60:
            return "linear"
        elif angle_sum < 90:
            return "quadratic"
        else:
            return "cubic"
