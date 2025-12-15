"""
A simple calculator module with basic arithmetic operations.
"""


class InvalidInputException(Exception):
    """Exception raised when input values are outside the valid range."""

    pass


MAX_VALUE = 1_000_000
MIN_VALUE = -1_000_000


class Calculator:
    """Calculator class providing basic arithmetic operations."""

    def _chechk_valid_input(self, *values):
        for value in values:
            if value < MIN_VALUE or value > MAX_VALUE:
                raise InvalidInputException("Input value out of valid range")

    def add(self, a, b):
        """Add two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Sum of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
        """
        self._chechk_valid_input(a, b)
        return a + b

    def subtract(self, a, b):
        """Subtract b from a.

        Args:
            a: First number
            b: Second number

        Returns:
            Difference of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
        """
        self._chechk_valid_input(a, b)
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Product of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
        """
        self._chechk_valid_input(a, b)
        return a * b

    def divide(self, a, b):
        """Divide a by b.

        Args:
            a: Numerator
            b: Denominator

        Returns:
            Quotient of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        self._chechk_valid_input(a, b)
        return a / b
