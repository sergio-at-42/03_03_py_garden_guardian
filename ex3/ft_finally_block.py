#!/usr/bin/env python3

from typing import Any


class Plant:

    def __init__(self, name: str) -> None:
        self._name: str = ""
        self.set_name(name)

    def get_name(self) -> str:
        return (self._name)

    def set_name(self, name: str) -> None:
        self._name = name

    def watering(self) -> None:
        print(f"Watering {self.get_name()}")


def water_plants(plant_list: list[Any]) -> None:
    try:
        print("Opening watering system")
        for p in plant_list:
            p.watering()
        print("Watering completed successfully!")
    except AttributeError:
        print(f"Error: Cannot water {p} - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    plant_list: list[Any] = [Plant("tomato"),
                             Plant("lettuce"),
                             Plant("carrots")]
    print("\nTesting normal watering...")
    water_plants(plant_list)
    print("\nTesting with error...")
    plant_list.insert(1, None)
    water_plants(plant_list)


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    test_watering_system()
    print("\nCleanup always happens, even with errors!")
