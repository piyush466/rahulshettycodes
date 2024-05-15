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

    # MyInfo Locators
    @staticmethod
    def myinfo_btn_xpath():
        myinfo_xpath = config.get("MyInfo Locators","myinfo_btn_xpath")
        return myinfo_xpath

    @staticmethod
    def enter_name():
        enter_name = config.get("MyInfo Locators", "enter_name")
        return enter_name

    @staticmethod
    def save_btn_xpath():
        save_btn_xpath = config.get("MyInfo Locators", "save_btn_xpath")
        return save_btn_xpath

