#!/usr/bin/env python3

class GardenError(Exception):
    """Base class for garden-related errors."""


class PlantError(GardenError):
    """Base class for plant-related errors."""
    def __init__(self, plant: str = "salad") -> None:
        super().__init__(f"The {plant} plant is wilting!")


class WaterError(GardenError):
    """Base class for water-related errors."""
    def __init__(self) -> None:
        super().__init__("Not enough water in the tank!")


def custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    try:
        raise PlantError("tomato")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print("\nTesting WaterError...")
    try:
        raise WaterError()
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print("\nTesting catching all garden errors...")
    try:
        raise PlantError()
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        raise WaterError()
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    custom_errors()
