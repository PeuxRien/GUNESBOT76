from datetime import datetime


class Logger:

    @staticmethod
    def _time():

        return datetime.now().strftime("%H:%M:%S")

    @staticmethod
    def info(message: str):

        print(f"[INFO {Logger._time()}] {message}")

    @staticmethod
    def warning(message: str):

        print(f"[WARN {Logger._time()}] {message}")

    @staticmethod
    def error(message: str):

        print(f"[ERROR {Logger._time()}] {message}")

    @staticmethod
    def success(message: str):

        print(f"[ OK  {Logger._time()}] {message}")