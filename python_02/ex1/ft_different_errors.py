def garden_operations(error):
    """
    do_errors for test the try and except with test_error_types() function
    """
    if error == "ValueError":
        int("abc")
    if error == "ZeroDivisionError":
        100 / 0
    if error == "FileNotFoundError":
        open("missing.txt", "r")
    if error == "KeyError":
        plants = {"tomato": "red"}
        print(plants["missing\\_plant"])


def test_error_types():
    """
    test errors one by one && multiple error
    """
    print("=== Garden Error Types Demo ===")
    print("\nTesting ValueError...")
    try:
        garden_operations("ValueError")
    except ValueError:
        print("Caught ValueError:  invalid literal for int()")
    print("\nTesting ZeroDivisionError...")
    try:
        garden_operations("ZeroDivisionError")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    print("\nTesting FileNotFoundError...")
    try:
        garden_operations("FileNotFoundError")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    print("\nTesting KeyError...")
    try:
        garden_operations("KeyError")
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'")
    print("\nTesting multiple errors together...")
    try:
        garden_operations("ValueError")
        garden_operations("ZeroDivisionError")
        garden_operations("FileNotFoundError")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")
    print("\nAll error types tested successfully!")


test_error_types()
