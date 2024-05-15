import logging
#
# class logGen:
#
#     @staticmethod
#     def logger():
#
#         logger = logging.getLogger("piyush")
#         logger.setLevel(logging.DEBUG)
#         formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
#         filehandler = logging.FileHandler(r"C:\Users\ASUS\PycharmProjects\rahulshettycodes\Logs\Generate.log")
#         filehandler.setLevel(logging.INFO)
#         filehandler.setFormatter(formatter)
#         logger.addHandler(filehandler)
#
#         return logger

import logging
class logGen:
    @staticmethod
    def logger():
        logger = logging.getLogger("piyush")
        if not logger.handlers:  # Check if a FileHandler has already been added
            logger.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            filehandler = logging.FileHandler(r"C:\Users\ASUS\PycharmProjects\rahulshettycodes\Logs\Generate.log")
            filehandler.setLevel(logging.INFO)
            filehandler.setFormatter(formatter)
            logger.addHandler(filehandler)
        return logger

