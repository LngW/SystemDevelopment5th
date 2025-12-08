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
    def test_add_invalid_input(self, calc : Calculator):
        """Test adding invalid input raises exception."""
        with pytest.raises(InvalidInputException):
            calc.add(MAX_VALUE + 1, 5)

        with pytest.raises(InvalidInputException):
            calc.add(MIN_VALUE - 1, 5)

        with pytest.raises(InvalidInputException):
            calc.add(5, MAX_VALUE + 10)

        with pytest.raises(InvalidInputException):
            calc.add(5, MIN_VALUE - 10)
        
        assert calc.add(MAX_VALUE, 5) == MAX_VALUE + 5
        assert calc.add(MIN_VALUE, 5) == MIN_VALUE + 5

    def test_subtract_invalid_input(self, calc : Calculator):
        with pytest.raises(InvalidInputException):
            calc.subtract(MIN_VALUE - 1, 5)
        
        with pytest.raises(InvalidInputException):
            calc.subtract(MAX_VALUE + 1, 5)

        with pytest.raises(InvalidInputException):
            calc.subtract(5, MIN_VALUE - 10)
        
        with pytest.raises(InvalidInputException):
            calc.subtract(5, MAX_VALUE + 10)
        
        assert calc.subtract(MIN_VALUE, 5) == MIN_VALUE - 5
        assert calc.subtract(5, MAX_VALUE) == 5 - MAX_VALUE
    
    def test_multiply_invalid_input(self, calc : Calculator):
        with pytest.raises(InvalidInputException):
            calc.multiply(5, MAX_VALUE + 10)
        
        with pytest.raises(InvalidInputException):
            calc.multiply(MIN_VALUE - 1, 5)
        
        with pytest.raises(InvalidInputException):
            calc.multiply(MAX_VALUE + 1, 5)
        
        with pytest.raises(InvalidInputException):
            calc.multiply(5, MIN_VALUE - 10)
        
        assert calc.multiply(5, MAX_VALUE) == 5 * MAX_VALUE
    
    def test_divide_invalid_input(self, calc : Calculator):
        with pytest.raises(InvalidInputException):
            calc.divide(MAX_VALUE + 1, 1)
        with pytest.raises(InvalidInputException):
            calc.divide(MIN_VALUE - 1, 1)
        with pytest.raises(InvalidInputException):
            calc.divide(1, MAX_VALUE + 1)
        with pytest.raises(InvalidInputException):
            calc.divide(1, MIN_VALUE - 1)
        
        assert calc.divide(MAX_VALUE, 1) == MAX_VALUE

    def test_divide_by_zero(self, calc : Calculator):
        """Test dividing by zero raises ValueError."""
        with pytest.raises(ValueError):
            calc.divide(5, 0)
        
        assert calc.divide(0, 5) == 0
        assert calc.divide(5, 1) == 5