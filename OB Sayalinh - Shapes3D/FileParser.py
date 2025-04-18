import Shapes

round_digit = 10000

class Solver():

    str_to_request = {
        "cuboid" : Shapes.Cuboid,
        "cube" : Shapes.Cube,
        "cylinder" : Shapes.Cylinder,
        "sphere" : Shapes.Sphere,
        "prism" : Shapes.NGonPrism,
        "area" : "area",
        "volume" : "volume"
    }

    def __init__(self):
        pass

    def solve(self, file_name):
        f = open(file_name)

        text = f.readlines()

        pairs = []

        for request in text:
            request.replace("\\\n", "")
            pair = request.split(",")
            pairs.append(pair)

        commands = []

        # Turn Pairs into commands

        for pair in pairs:

            params_string = pair[1:]

            params = []

            for param in params_string:
                params.append(float(param))

            request = self.str_to_request[pair[0]]

            commands.append([request] + params)

        objects = []

        total = 0

        for command in commands:

            if command[0] == "volume":

                volume = 0

                for instance in objects:

                    add = instance.get_volume()

                    volume += add

                total += round(volume * command[1], round_digit)
                objects = []

            elif command[0] == "area":

                surface_area = 0

                for instance in objects:

                    add = instance.get_surface_area()

                    surface_area += add

                total += round(surface_area * command[1], round_digit)
                objects = []

            else:
                my_object = command[0](*command[1:])
                objects.append(my_object)

        return total
























