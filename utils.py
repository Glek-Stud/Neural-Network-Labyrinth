from colorama import init as init_colorama
from colorama import Fore as colFore
from colorama import Back as colBack
from colorama import Style as colStyle

import logging


class Utils:

    def __init__(self):
        init_colorama(True)
        logging.basicConfig(level=logging.INFO,
                            format=f"[%(asctime)s]:[%(levelname)s]:[%(name)s]: %(message)s")

    @staticmethod
    def test():
        logging.info("Перевірка")
        logging.error("Помилка")
        print(colFore.RED + 'some red text')
        print(colBack.GREEN + 'and with a green background')
        print(colStyle.BRIGHT + 'and in dim text')
        print(colStyle.RESET_ALL)
        print('back to normal now')


def set_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter("[%(asctime)s]:[%(levelname)s]:[%(name)s]: %(message)s")

    file_handler = logging.FileHandler('allFile.log', "a")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger


if __name__ == '__main__':
    Utils().test()
    log2D = set_logger("GUI 2D")
    logLogic = set_logger("Logic")
    log2D.info("Перевірка")
    logLogic.info("Перевірка 2")
    log2D.info("Перевірка 3")
