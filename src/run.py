"""
Module that run the setup for windscrib's ephemeral port
"""
import logging
import config
from lib.qbit import QbitManager
from logger import setup_logging
from util import write_output_file
from ws import Windscribe

setup_logging()

logger = logging.getLogger("main")

def main() -> None:
    """Main function responsible for setting up ws and qbit.

    Steps:
    - login to ws
    - setup new matching ports
    - setup qbit
    """

    logger.info("Requesting port...")
    with Windscribe(username=config.WS_USERNAME, password=config.WS_PASSWORD) as ws:
        port = ws.setup()

    if not config.QBIT_FOUND:
        logger.warning(
            "Read the latest doc: https://github.com/dhruvinsh/ws-ephemeral#readme"
        )
        return

    logger.info("Setting up port...")
    try:
        qbit = QbitManager(
            host=config.QBIT_HOST,
            port=config.QBIT_PORT,
            username=config.QBIT_USERNAME,
            password=config.QBIT_PASSWORD,
        )
    except Exception:
        logger.error("not able to work with qbit")
        raise

    if qbit.set_listen_port(port):
        write_output_file(port)
    else:
        logger.warn("qBittorrent port didn't change!")

    if config.QBIT_PRIVATE_TRACKER:
        qbit.setup_private_tracker()
    logger.info("Port setup completed.")


if __name__ == "__main__":
    main()
