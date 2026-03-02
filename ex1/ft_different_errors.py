def test_error_types(e: Exception) -> None:
    try:
        raise e
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file ’missing.txt’")
    except KeyError:
        print("Caught KeyError: ’missing_plant’")


def garden_operations() -> None:
    print("=== Garden Error Types Demo ===")
    print("")
    print("Testing ValueError...")
    try:
        int("abc")
    except Exception as e:
        test_error_types(e)
    finally:
        print("")
    print("Testing ZeroDivisionError...")
    try:
        12 / 0
    except Exception as e:
        test_error_types(e)
    finally:
        print("")
    print("Testing FileNotFoundError...")
    try:
        open("missing.txt")
    except Exception as e:
        test_error_types(e)
    finally:
        print("")
    print("Testing KeyError...")
    plant: dict[str, int] = {}
    try:
        plant["42"]
    except Exception as e:
        test_error_types(e)
    finally:
        print("")
    print("All error types tested successfully!")


if __name__ == "__main__":
    garden_operations()
