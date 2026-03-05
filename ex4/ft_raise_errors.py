#!/usr/bin/env python3

class PlantError(Exception):
    """Base class for Plant-related errors."""


class PlantNameEmptyError(PlantError):
    """Base class for plant name-related errors."""
    def __init__(self) -> None:
        super().__init__("Plant name cannot be empty!")


class WaterLevelTooLowError(PlantError):
    """Base class for water-related errors."""
    def __init__(self, level: int) -> None:
        super().__init__(f"Water level {level} is too low (min 1)")


class WaterLevelTooHighError(PlantError):
    """Base class for water-related errors."""
    def __init__(self, level: int) -> None:
        super().__init__(f"Water level {level} is too high (max 10)")


class SunlightTooLowError(PlantError):
    """Base class for sunlight-related errors."""
    def __init__(self, sunlight: int) -> None:
        super().__init__(f"Sunlight hours {sunlight} is too low (min 2)")


class SunlightTooHighError(PlantError):
    """Base class for sunlight-related errors."""
    def __init__(self, sunlight: int) -> None:
        super().__init__(f"Sunlight hours {sunlight} is too high (max 12)")


def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    try:
        if plant_name == "":
            raise PlantNameEmptyError()
        if water_level < 1:
            raise WaterLevelTooLowError(water_level)
        if water_level > 10:
            raise WaterLevelTooHighError(water_level)
        if sunlight_hours < 2:
            raise SunlightTooLowError(sunlight_hours)
        if sunlight_hours > 12:
            raise SunlightTooHighError(sunlight_hours)
    except PlantError as e:
        print(f"Error: {e}")
    else:
        print(f"Plant ’{plant_name}’ is healthy!")


def test_plant_checks() -> None:
    print("\nTesting good values...")
    check_plant_health("tomato", 5, 8)
    print("\nTesting empty plant name...")
    check_plant_health("", 5, 8)
    print("\nTesting bad water level...")
    check_plant_health("tomato", -4, 8)
    print("\nTesting bad water level...")
    check_plant_health("tomato", 42, 8)
    print("\nTesting bad sunlight hours...")
    check_plant_health("tomato", 5, 1)
    print("\nTesting bad sunlight hours...")
    check_plant_health("tomato", 5, 42)


if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===")
    test_plant_checks()
    print("\nAll error raising tests completed!")
