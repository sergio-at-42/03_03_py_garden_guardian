#!/usr/bin/env python3

class GardenError(Exception):
    """Base class for Plant-related errors."""


class NotEnoughWaterInTankError(GardenError):
    """Base class for tank-related errors."""
    def __init__(self) -> None:
        super().__init__("Not enough water in tank")


class PlantError(GardenError):
    """Base class for Plant-related errors."""


class PlantNameEmptyError(PlantError):
    """Base class for plant name-related errors."""
    def __init__(self) -> None:
        super().__init__("Plant name cannot be empty!")


class PlantNameNotFound(PlantError):
    """Base class for plant name-related errors."""
    def __init__(self, plant_name: str = "") -> None:
        super().__init__(f"Plant '{plant_name}' not found!")


class PlantNameAlreadyExist(PlantError):
    """Base class for plant name-related errors."""
    def __init__(self, plant_name: str = "") -> None:
        super().__init__(f"Plant '{plant_name}' already exist!")


class WaterLevelTooLowError(PlantError):
    """Base class for water-related errors."""
    def __init__(self, level: int) -> None:
        super().__init__(f"Water level {level} is too low (min 1)")


class WaterLevelTooHightError(PlantError):
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


class Plant:

    def __init__(self, name: str = "Plant", water: int = 0, sun: int = 0) -> None:
        self._name: str = ""
        self.water: int = 0
        self.sun: int = 0
        self.set_name(name)
        self.set_water(water)
        self.set_sun(sun)

    def get_name(self) -> str:
        return (self._name)

    def get_water(self) -> str:
        return (self._water)

    def get_sun(self) -> str:
        return (self._sun)

    def set_name(self, name: str) -> None:
        self._name = name

    def set_water(self, water: str) -> None:
        self._water = water

    def set_sun(self, sun: str) -> None:
        self._sun = sun


class GardenManager:

    def __init__(self) -> None:
        self.plants: list[Plant] = []
        self.tank: int = 42
    
    def add_plant(self, plant_name: str, water: int = 0, sun: int = 0) -> bool:
        error: bool = False
        try:
            if plant_name == "":
                raise PlantNameEmptyError()
            plant = next((p for p in self.plants if p.get_name() == plant_name), None)
            if plant is None:
                self.plants.append(Plant(plant_name, water, sun))
            else:
                raise PlantNameAlreadyExist(plant_name)
        except PlantError as e:
            print(f"Error adding plant: {e}")
            error = True
        else:
            print(f"Added {plant_name} successfully")
            error = False
        finally:
            return (error)

    def watering(self, plant_list: list[tuple[str, int]]) -> bool:
        try:
            error: bool = False
            print("Opening watering system")
            for plant_name, water in plant_list:
                try:
                    if plant_name == "":
                        raise PlantNameEmptyError()
                    plant = next((p for p in self.plants if p.get_name() == plant_name), None)
                    if plant is None:
                        raise PlantNameNotFound(plant_name)
                    if water > self.tank:
                        raise NotEnoughWaterInTankError
                except GardenError as e:
                    print(f"Error Watering {plant_name} : {e}")
                    error = True
                else:
                    plant.set_water(water)
                    self.tank -= water
                    print(f"Watering {plant.get_name()} - success")
                    error = False
        finally:
            print("Closing watering system (cleanup)")
        return (error)


    def check_plant_health(self) -> bool:
        error: bool = False
        for plant in self.plants:
            try:
                if plant.get_water() < 1:
                    raise WaterLevelTooLowError(plant.get_water())
                if plant.get_water() > 10:
                    raise WaterLevelTooHightError(plant.get_water())
                if plant.get_sun() < 2:
                    raise SunlightTooLowError(plant.get_sun())
                if plant.get_sun() > 12:
                    raise SunlightTooHighError(plant.get_sun())
            except PlantError as e:
                print(f"Error checking {plant.get_name()} : {e}")
                error = True
            else:
                print(f"{plant.get_name()}: healthy (water: {plant.get_water()}, sun: {plant.get_sun()})")
                error = False
        return (error)


def test_garden_management() -> None:
    print("=== Garden Management System ===")
    garden = GardenManager()
    print("\nAdding plants to garden...")
    garden.add_plant("tomato", 3, 8)
    garden.add_plant("lettuce", 15, 12)
    garden.add_plant("")
    garden.add_plant("tomato")

    print("\nWatering plants...")
    garden.watering([("tomato", 5),
                     ("lettuce", 4),
                     ("lettuce", 15),
                     ("lettuce", 42),
                     ("", 2),
                     ("carrot", 2)])

    print("\nChecking plant health...")
    garden.check_plant_health()

    print("\nTesting error recovery...")
    try:
        raise NotEnoughWaterInTankError()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()    
