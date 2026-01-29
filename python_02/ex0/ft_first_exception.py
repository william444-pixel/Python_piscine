def check_temperature(temp_str):
    """Error handling && print output
    """
    try:
        temp = int(temp_str)
        if -1 < temp < 41:
            print(f"Temperature {temp}°C is perfect for plants!")
        elif temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)")
        elif temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")


def test_temperature_input():
    """Tester
    """
    print("=== Garden Temperature Checker ===")
    user_input = input("\nTesting temperature: ")
    check_temperature(user_input)
    user_input = input("\nTesting temperature: ")
    check_temperature(user_input)
    user_input = input("\nTesting temperature: ")
    check_temperature(user_input)
    user_input = input("\nTesting temperature: ")
    check_temperature(user_input)
    print("\nAll tests completed - program didn't crash!")


test_temperature_input()
