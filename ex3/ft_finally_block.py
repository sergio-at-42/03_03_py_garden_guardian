#!/usr/bin/env python3

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


class WaterError(Exception):
    """Base class for water-related errors."""
    def __init__(self, plant_name: str | None) -> None:
        super().__init__(f"Cannot water {plant_name} - invalid plant!")


def water_plants(plant_list: list[Plant | None]) -> None:
    try:
        print("Opening watering system")
        for p in plant_list:
            if isinstance(p, Plant):
                p.watering()
            else:
                raise WaterError(p)
        print("Watering completed successfully!")
    except WaterError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    plant_list: list[Plant | None] = [Plant("tomato"),
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
