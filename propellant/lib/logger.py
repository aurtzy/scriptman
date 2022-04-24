import logging
import typing
from os import PathLike

logger = logging.getLogger('propellant')
logger.setLevel(logging.DEBUG)


def init_stream(debug: bool):
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG if debug else logging.INFO)
    logger.addHandler(stream_handler)
    if debug:
        log('Enabled debug log.', logging.INFO)


def init_file(path: typing.Union[str, PathLike]):
    file_handler = logging.FileHandler(path)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter('[%(levelname)s]: %(message)s'))
    logger.addHandler(file_handler)


def log(msg: str, lvl: int):
    # TODO: figure out stylizing text?

    msg = msg.replace('\n', '\n\t')
    logger.log(lvl, msg)
