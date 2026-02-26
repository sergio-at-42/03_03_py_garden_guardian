#!/usr/bin/env python3

def check_temperature(temp_str) -> int:
    temp: int = 0
    pass
    return (temp)


def test_temperature_input() -> None:
    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")


if __name__ == "__main__":
    test_temperature_input()
