def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")  # Use ValueError instead of AssertionError
    return a / b
