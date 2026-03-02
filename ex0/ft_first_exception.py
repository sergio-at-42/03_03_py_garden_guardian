#!/usr/bin/env python3

class PlantError(Exception):
    """Base class for plant-related errors."""
    pass


class ToColdError(PlantError):
    """Error when temperature is too cold for plants."""
    pass


class ToHotError(PlantError):
    """Error when temperature is too hot for plants."""
    pass


def check_temperature(temp_str: str) -> int:
    temp: int = 0
    try:
        print(f"Testing temperature: {temp_str}")
        temp = int(temp_str)
        if temp < 0:
            raise ToColdError()
        elif temp > 40:
            raise ToHotError()
    except ValueError:
        print(f"Error: ’{temp_str}’ is not a valid number")
    except ToColdError:
        print(f"Error: {temp}°C is too cold for plants (min 0°C)")
    except ToHotError:
        print(f"Error: {temp}°C is too hot for plants (max 40°C)")
    else:
        print(f"Temperature {temp_str}°C is perfect for plants!")
    finally:
        print("")
    return (temp)


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===")
    print("")
    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")
    print("All tests completed - program didn’t crash!")


if __name__ == "__main__":
    test_temperature_input()
