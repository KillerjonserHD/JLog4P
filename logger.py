from datetime import datetime

class Logger:
    def __init__(self, loglevel=3, timestamps=True):
        if(0<loglevel<=3):
            self.loglevel = loglevel
        else:
            raise Exception("loglevel not supported")
        self.timestamps = timestamps
    
    def print_to_console(self, level, message):
        if(self.timestamps):
            timestamp = datetime.now().strftime("%H:%M:%S")
            print(f"[{level}][{timestamp}] >>> {message}")
            return
        print(f"[{level}] >>> {message}")

    def log_to_file(self, level, message):
        pass #TODO File

    def info(self, message):
        if(self.loglevel < 3):
            return
        self.print_to_console(level="INFO", message=message)
        self.log_to_file(level="INFO", message=message)

    def warning(self, message):
        if(self.loglevel < 2):
            return
        self.print_to_console(level="WARNING", message=message)
        self.log_to_file(level="WARNING", message=message)
    
    def error(self, message):
        if(self.loglevel < 1):
            return
        self.print_to_console(level="ERROR", message=message)
        self.log_to_file(level="ERROR", message=message)

if __name__ == "__main__":
    logger = Logger(0)
    logger.info("Info Message")
    logger.warning("Warning message")
    logger.error("FEHLER")
    