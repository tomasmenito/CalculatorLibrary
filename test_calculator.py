"""
Unit tests for calculator
"""
import calculator


class TestCalculatro:

    def test_addition(self):
        assert 3 == calculator.add(1, 2)

    def test_subtraction(self):
        assert -1 == calculator.subtract(2, 3)

    def test_multiplication(self):
        assert -9 == calculator.multiply(3, -3)
