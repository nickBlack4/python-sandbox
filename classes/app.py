class Point:
    default_color = "red"  # class level attribute

    """
        the methods that we define in a class should have at least one parameter which by convention is called self.  this references the current object we are working with.  When calling methods of an object we never have to supply a value for the self parameter, python interpreter does that for us.
    """

    # a magic method

    # self is a reference to the current point object.  so sounds like 'this'
    # when we call teh Point class, python will internally create the point object in memory and set self to reference that object

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # in this block we will define all the funcs related to points

    def draw(self):
        print(f"Point ({self.x}, {self.y})")

    # magic method
    def __str__(self):
        return f"({self.x}, {self.y})"


# point = Point()
# print(type(point))
# print(isinstance(point, int))
# # is this object an instance of a given class?

Point.default_color = "yellow"

point = Point(1, 2)
# print(point.default_color)
# point.z = 10
# python is dynamic so don't have to define all the attributes in constructor

# these attributes are all instance attributes
point.draw()

# another = Point(3, 4)
# another.draw()

# we can also define class attributes.  attributes that we define at the class level.  These attributes are shared by all instances.


# going to take notes down here vs running all these examples for expediency


# magic methods
print(point)
# print(point)
print(str(point))
