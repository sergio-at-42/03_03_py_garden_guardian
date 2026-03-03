def test_error_types(e: Exception) -> None:
    try:
        raise
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file ’missing.txt’")
    except KeyError:
        print("Caught KeyError: ’missing_plant’")
    except Exception:
        print(f"{type(e).__name__}: {e}")
        print("Caught an error, but program continues!")
    finally:
        print("")


def garden_operations() -> None:
    print("=== Garden Error Types Demo ===")
    print("")
    print("Testing ValueError...")
    try:
        int("abc")
    except Exception as e:
        test_error_types(e)
    print("Testing ZeroDivisionError...")
    try:
        12 / 0
    except Exception as e:
        test_error_types(e)
    print("Testing FileNotFoundError...")
    try:
        open("missing.txt")
    except Exception as e:
        test_error_types(e)
    print("Testing KeyError...")
    plant: dict[str, int] = {}
    try:
        plant["42"]
    except Exception as e:
        test_error_types(e)
    print("Testing multiple errors together...")
    list_plant: list[str] = []
    try:
        list_plant[42]
        # list_plant.toto
    except Exception as e:
        test_error_types(e)
    print("All error types tested successfully!")


if __name__ == "__main__":
    garden_operations()
