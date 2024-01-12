from fire import Fire

from echo.utils.logging import logger


# Functions called via primary command should always return either int, a process or a thread
def echo(**kwargs) -> int:
    logger.info(f"echo: {kwargs=}")
    return 0


if __name__ == "__main__":
    logger.setLevel(10)
    Fire(echo)
