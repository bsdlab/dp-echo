from dareplane_utils.default_server.server import DefaultServer
from fire import Fire

from echo.main import echo
from echo.utils.logging import logger


def main(port: int = 8080, ip: str = "127.0.0.1", loglevel: int = 10):
    logger.setLevel(loglevel)
    pcommand_map = {"ECHO": echo}

    server = DefaultServer(
        port,
        ip=ip,
        pcommand_map=pcommand_map,
        name="echo_to_log_server",
        logger=logger,
    )

    # initialize to start the socket
    server.init_server()

    logger.debug(f"Server started at {ip}:{port}")
    # start processing of the server
    server.start_listening()

    return 0


if __name__ == "__main__":
    Fire(main)
