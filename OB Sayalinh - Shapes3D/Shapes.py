from abc import ABC, abstractmethod
import math

class Shape3D(ABC):

    @abstractmethod
    def get_surface_area(self):
        raise NotImplementedError()

    @abstractmethod
    def get_volume(self):
        raise NotImplementedError()

class Cuboid(Shape3D):
    depth = None
    width = None
    height = None

    def __init__(self, width, height, depth):
        super().__init__()
        self.depth = depth
        self.width = width
        self.height = height

    def get_surface_area(self):
        height = self.height
        width = self.width
        depth = self.depth
        return (height * width * 2) + (height * depth * 2) + (width * depth * 2)

    def get_volume(self):
        return self.depth * self.width * self.height

class Cube(Cuboid):

    side_length = 0

    def __init__(self, side_length):
        super().__init__(side_length, side_length, side_length)
        self.side_length = side_length

class Cylinder(Shape3D):

    radius = 0
    height = 0

    def __init__(self, radius, height):
        super().__init__()
        self.radius = radius
        self.height = height

    def get_surface_area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)

    def get_volume(self):
        return math.pi * (self.radius ** 2) * self.height

class Sphere(Shape3D):

    radius = 0

    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def get_surface_area(self):
        return 4 * math.pi * (self.radius ** 2)

    def get_volume(self):
        return (4 / 3) * math.pi * (self.radius ** 3)

class NGonPrism(Shape3D):

    side_length = 0
    faces = 0
    height = 0
    base_area = 0
    perimeter = 0

    def __init__(self, side_length, faces, height):
        super().__init__()

        self.side_length = side_length
        self.faces = faces
        self.height = height
        sides = self.faces - 2
        self.perimeter = faces * side_length
        pass
        self.base_area = faces * (side_length ** 2) * (1/4) * (1 / math.tan(math.pi/faces))
        pass

    def get_surface_area(self):
        surface_area = (self.perimeter * self.height) + (self.base_area * 2)
        pass
        return surface_area

    def get_volume(self):
        volume = self.base_area * self.height
        return volume

