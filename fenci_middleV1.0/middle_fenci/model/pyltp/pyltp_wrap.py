
from pyltp import Segmentor
from pyltp import Postagger
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LTP_DATA_DIR = os.path.join(BASE_DIR,"ltp_data")
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')
pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')
segmentor = Segmentor()

class Pyltp_fenci(object):
    def __init__(self,pyltp_content,*args,**kwargs):
        self.pyltp_content = pyltp_content
        self.separator = kwargs.get("separator")

    def pyltp_fenci(self):
        if self.separator == None:
            segmentor.load(cws_model_path)  # 加载模型
            words = segmentor.segment(self.pyltp_content)  # 分词
            pyltp_result = "  ".join(words)

            segmentor.release()  # 释放模型
            return pyltp_result

        else:
            segmentor.load(cws_model_path)  # 加载模型
            words = segmentor.segment(self.pyltp_content)  # 分词
            pyltp_result = " {} ".format(self.separator).join(words)
            segmentor.release()  # 释放模型
            return pyltp_result

    def pyltp_fenci_list(self):

        segmentor.load(cws_model_path)
        words = segmentor.segment(self.pyltp_content)
        pyltp_result_list=list(words)


        segmentor.release()  # 释放模型
        return pyltp_result_list

    def pyltp_flag(self):
        segmentor.load(cws_model_path)  # 加载模型
        words = segmentor.segment(self.pyltp_content)  # 分词
        pyltp_result = list(words)
        print(pyltp_result)
        segmentor.release()  # 释放模型
        postagger = Postagger()  # 初始化实例
        postagger.load(pos_model_path)  # 加载模型

        postags = postagger.postag(pyltp_result)  # 词性标注
        pyltp_result_flag1 = []
        for postag in postags:
            pyltp_result_flag1.append(postag)
        pyltp_result_flag = []
        for k in range(len(pyltp_result)):
            pyltp_result_flag.append(pyltp_result[k]+"/"+pyltp_result_flag1[k])

        c = " ".join(pyltp_result_flag)
        postagger.release()  # 释放模型
        return c

    def pyltp_flag_list(self):
        segmentor.load(cws_model_path)  # 加载模型
        words = segmentor.segment(self.pyltp_content)  # 分词
        pyltp_result = list(words)
        print(pyltp_result)
        segmentor.release()  # 释放模型
        postagger = Postagger()  # 初始化实例
        postagger.load(pos_model_path)  # 加载模型

        postags = postagger.postag(pyltp_result)  # 词性标注
        pyltp_result_flag1 = []
        for postag in postags:
            pyltp_result_flag1.append(postag)
        pyltp_result_flag_list = []
        for k in range(len(pyltp_result)):
            pyltp_result_flag_list.append(pyltp_result[k]+"/"+pyltp_result_flag1[k])

        postagger.release()  # 释放模型
        return pyltp_result_flag_list
