class BezierPolynomial:
    def __init__(self, p1, p2, p3=None, p4=None):
        self.linearX = lambda t: (1 - t) * p1[0] + t * p2[0]
        self.linearY = lambda t: (1 - t) * p1[1] + t * p2[1]
        self.quadraticX = None
        self.quadraticY = None
        self.cubicX = None
        self.cubicY = None
        if p3 is not None:
            self.linearX2 = lambda t: (1 - t) * p2[0] + t * p3[0]
            self.linearY2 = lambda t: (1 - t) * p2[1] + t * p3[1]
            self.quadraticX = lambda t: (1 - t) * self.linearX(t) + t * self.linearX2(t)
            self.quadraticY = lambda t: (1 - t) * self.linearY(t) + t * self.linearY2(t)
        else:
            self.linearX2 = None
            self.linearY2 = None
        
        if p4 is not None:
            self.linearX3 = lambda t: (1 - t) * p3[0] + t * p4[0]
            self.linearY3 = lambda t: (1 - t) * p3[1] + t * p4[1]
            
            self.quadraticX2 = lambda t: (1 - t) * self.linearX2(t) + t * self.linearX3(t)
            self.quadraticY2 = lambda t: (1 - t) * self.linearY2(t) + t * self.linearY3(t)

            self.cubicX = lambda t: (1 - t) * self.quadraticX(t) + t * self.quadraticX2(t)
            self.cubicY = lambda t: (1 - t) * self.quadraticY(t) + t * self.quadraticY2(t)
        else:
            self.cubicX = None
            self.cubicY = None
