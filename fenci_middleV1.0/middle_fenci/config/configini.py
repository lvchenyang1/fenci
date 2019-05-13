import configparser


config = configparser.ConfigParser()
config.read("config.ini")

def get_conf():
    try:
        user_conf_choice = config.get("CLIENT","user_conf")
        if user_conf_choice:
            conf = config.get("OPTIONS", user_conf_choice)
        else:
            conf = "jieba"
        if conf == "jieba":

            return "jieba"
        if conf == "ltp":
            return "ltp"
        if conf == "nlpir":
            return "nlpir"
    except Exception as err:
        return("错误：%s", err)

def get_model():
    try:
        user_get_model = config.options("OPTIONS")
        return user_get_model
    except Exception as err:
        return("错误：%s", err)