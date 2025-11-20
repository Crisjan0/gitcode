"""
Simple calculator example in Python.

This script defines four basic functions: `add`, `subtract`, `multiply`, and `divide`.
It then demonstrates their usage in a short, non-interactive demo so you can run
the file directly and see the output.

Run: `python index.py`
"""

def add(a, b):
	"""Return the sum of a and b."""
	return a + b


def subtract(a, b):
	"""Return a minus b."""
	return a - b


def multiply(a, b):
	"""Return the product of a and b."""
	return a * b


def divide(a, b):
	"""Return a divided by b. Raises ValueError on division by zero."""
	if b == 0:
		raise ValueError("Cannot divide by zero")
	return a / b


def demo():
	"""Run a few example operations and print the results."""
	a, b = 12, 4
	print(f"Demo values: a={a}, b={b}")
	print(f"add(a, b) => {add(a, b)}")
	print(f"subtract(a, b) => {subtract(a, b)}")
	print(f"multiply(a, b) => {multiply(a, b)}")
	print(f"divide(a, b) => {divide(a, b)}")


if __name__ == "__main__":
	demo()
