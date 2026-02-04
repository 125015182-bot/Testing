from logger import setup_logger
from exceptions import InvalidAgeError, DivisionByZeroCustomError

logger = setup_logger("error_demo")


# 🔹 Type Error Example
def type_error_demo():
    try:
        number = 10
        text = "hello"
        result = number + text  # TypeError
        logger.info("Result: %s", result)
    except TypeError as exc:
        logger.exception("TypeError occurred: %s", exc)


# 🔹 Zero Division Error Example
def zero_division_demo():
    try:
        a = 10
        b = 0
        logger.debug("Attempting division: %s / %s", a, b)

        if b == 0:
            raise DivisionByZeroCustomError("Cannot divide by zero")

        result = a / b
        logger.info("Division result: %s", result)

    except DivisionByZeroCustomError as exc:
        logger.error("Custom Zero Division Error: %s", exc)


# 🔹 Value Error Example
def value_error_demo():
    try:
        value = "abc"
        logger.debug("Converting value to int: %s", value)
        number = int(value)  # ValueError
        logger.info("Converted number: %s", number)
    except ValueError as exc:
        logger.exception("ValueError occurred: %s", exc)


# 🔹 Custom Age Validation
def validate_age(age: int):
    try:
        logger.debug("Validating age: %s", age)

        if age < 0:
            raise InvalidAgeError("Age cannot be negative")

        logger.info("Valid age provided: %s", age)

    except InvalidAgeError as exc:
        logger.warning("Custom InvalidAgeError: %s", exc)


def main():
    logger.info("Starting error demo...")

    type_error_demo()
    zero_division_demo()
    value_error_demo()
    validate_age(25)
    validate_age(-5)

    logger.info("Error demo completed.")


if __name__ == "__main__":
    main()
