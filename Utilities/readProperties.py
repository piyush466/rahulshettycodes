import configparser

config = configparser.RawConfigParser()

config.read(r"C:\Users\ASUS\PycharmProjects\rahulshettycodes\Configuration\config.ini")

class ReadProperties:

    @staticmethod
    def userfname():
        name = config.get("common info","name")
        return name

    @staticmethod
    def usermname():
        mname = config.get("common info", "mname")
        return mname

    @staticmethod
    def userlnamee():
        lname = config.get("common info", "lname")
        return lname

    @staticmethod
    def username_of_myinfo():
        username = config.get("MyInfo page", "usernmae")
        return username
