#usr/bin/python3
""" This class does what it's asked to do"""


class BaseGeometry:
    """is based on the previous geometry classes"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates name and value.

	Args:
	    name (str): the name of the parameter
	    Value (int): the value of the paramter
        Raises:
              TypeError: if value is not an integer
              ValueError: if value is <= 0.
	"""
        self.name = name
        self.value = value

        if not isinstance(self.value, int):
            raise TypeError("{} must be an integer".format(self.name))
        if self.value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
