"""
Test suite for the Calculator class.
"""

import pytest
from calculator.calculator import Calculator, InvalidInputException, MAX_VALUE, MIN_VALUE

@pytest.fixture
def calc():
    return Calculator()

class TestAddition:
    """Tests for the add method."""

    def test_add_positive_numbers(self, calc : Calculator):
        """Test adding two positive numbers."""
        # Arrange
        a = 5
        b = 3
        expected = 8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_numbers(self, calc : Calculator):
        """Test adding two negative numbers."""
        # Arrange
        a = -5
        b = -3
        expected = -8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_and_negative(self, calc : Calculator):
        """Test adding positive and negative numbers."""
        # Arrange
        a = 5
        b = -3
        expected = 2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_and_positive(self, calc : Calculator):
        """Test adding negative and positive numbers."""
        # Arrange
        a = -5
        b = 3
        expected = -2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_with_zero(self, calc : Calculator):
        """Test adding positive number with zero."""
        # Arrange
        a = 5
        b = 0
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_zero_with_positive(self, calc : Calculator):
        """Test adding zero with positive number."""
        # Arrange
        a = 0
        b = 5
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_floats(self, calc : Calculator):
        """Test adding floating point numbers."""
        # Arrange
        a = 2.5
        b = 3.7
        expected = 6.2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == pytest.approx(expected)


class TestSubtraction:
    """Tests for the subtract method."""

    def test_subtract_positive_numbers(self, calc : Calculator):
        """Test subtracting positive numbers."""
        a = 5
        b = 3
        expected = 2
        result = calc.subtract(a, b)
        assert result == expected

class TestMultiplication:
    """Tests for the multiply method."""

    def test_multiply_positive_numbers(self, calc : Calculator):
        """Test multiplying positive numbers."""
        a = 5
        b = 3
        expected = 15
        result = calc.multiply(a, b)
        assert result == expected

class TestDivision:
    """Tests for the divide method."""

    def test_divide_positive_numbers(self, calc : Calculator):
        """Test dividing positive numbers."""
        a = 6
        b = 3
        expected = 2
        result = calc.divide(a, b)
        assert result == expected

class TestInvalidInput:

    @staticmethod
    def __check_expception_message(message: str):
        """Helper method to check exception message."""
        return lambda exc_info: str(exc_info) == message
    
    def __test_invalid_input_exception(self, callable):
        check = self.__check_expception_message("Input value out of valid range")

        with pytest.raises(InvalidInputException) as exc_info:
            callable(MAX_VALUE + 1, 1)
        assert check(exc_info.value)
        
        with pytest.raises(InvalidInputException) as exc_info:
            callable(MIN_VALUE - 1, 1)
        assert check(exc_info.value)

        with pytest.raises(InvalidInputException) as exc_info:
            callable(1, MAX_VALUE + 1)
        assert check(exc_info.value)
        
        with pytest.raises(InvalidInputException) as exc_info:
            callable(1, MIN_VALUE - 1)
        assert check(exc_info.value)
    
    def test_add_invalid_input(self, calc : Calculator):
        """Test adding invalid input raises exception."""
        self.__test_invalid_input_exception(calc.add)

        assert calc.add(MAX_VALUE, 1) == MAX_VALUE + 1
        assert calc.add(MIN_VALUE, 1) == MIN_VALUE + 1
        assert calc.add(1, MAX_VALUE) == MAX_VALUE + 1
        assert calc.add(1, MIN_VALUE) == MIN_VALUE + 1
    
    def test_subtract_invalid_input(self, calc : Calculator):
        self.__test_invalid_input_exception(calc.subtract)
        
        assert calc.subtract(MAX_VALUE, 1) == MAX_VALUE - 1
        assert calc.subtract(MIN_VALUE, 1) == MIN_VALUE - 1
        assert calc.subtract(1, MAX_VALUE) == 1 - MAX_VALUE
        assert calc.subtract(1, MIN_VALUE) == 1 - MIN_VALUE
    
    def test_multiply_invalid_input(self, calc : Calculator):
        self.__test_invalid_input_exception(calc.multiply)
        
        assert calc.multiply(MAX_VALUE, 1) == MAX_VALUE
        assert calc.multiply(MIN_VALUE, 1) == MIN_VALUE
        assert calc.multiply(1, MAX_VALUE) == MAX_VALUE
        assert calc.multiply(1, MIN_VALUE) == MIN_VALUE
    
    def test_divide_invalid_input(self, calc : Calculator):
        self.__test_invalid_input_exception(calc.divide)
        
        assert calc.divide(MAX_VALUE, 1) == MAX_VALUE
        assert calc.divide(MIN_VALUE, 1) == MIN_VALUE
        assert calc.divide(1, MAX_VALUE) == 1 / MAX_VALUE
        assert calc.divide(1, MIN_VALUE) == 1 / MIN_VALUE

    def test_divide_by_zero(self, calc : Calculator):
        """Test dividing by zero raises ValueError."""
        def check(exc_info):
            return str(exc_info) == "Cannot divide by zero"

        with pytest.raises(ValueError) as exc_info:
            calc.divide(5, 0)
        assert check(exc_info.value)
        
        assert calc.divide(0, 5) == 0
        assert calc.divide(5, 1) == 5
        assert calc.divide(-5, 1) == -5
        assert calc.divide(1, -5) == -1/5
        assert calc.divide(-5, -1) == 5