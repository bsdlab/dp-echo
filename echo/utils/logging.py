from dareplane_utils.logging.logger import get_logger

logger = get_logger("echo_to_log")

# Uncomment this for standalone testing
# from logging import Formatter, StreamHandler
# fmt = Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# sh = StreamHandler()
# sh.setFormatter(fmt)
# logger.addHandler(sh)
