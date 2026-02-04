from logger import setup_logger
from exceptions import InvalidAgeError

logger = setup_logger("demo_logger")


def validate_age(age: int) -> None:
    if age < 0:
        logger.error("Invalid age provided: %s", age)
        raise InvalidAgeError("Age cannot be negative")
    logger.info("Valid age: %s", age)


def main() -> None:
    try:
        validate_age(25)
        validate_age(-5)
    except InvalidAgeError as exc:
        logger.exception("Exception occurred: %s", exc)


if __name__ == "__main__":
    main()
