import configparser


config=configparser.RawConfigParser()
config.read('C:/Users/HP/PycharmProjects/seleniumProject/Hybrid_Framework-OpenCart/Configurations/config.ini')

class ReadConfig:
    @staticmethod
    def getAppURL():
        url=config.get("app url","baseurl")
        return url

    @staticmethod
    def getLoginURL():
        url = config.get("app url", "loginurl")
        return url

    @staticmethod
    def getUserEmail():
        useremail = config.get("user credential", "useremail")
        return useremail

    @staticmethod
    def getPassword():
        password = config.get("user credential", "password")
        return password

    @staticmethod
    def getInvalidUserEmail():
        invalid_userName = config.get("user credential", "invalid_user")
        return invalid_userName