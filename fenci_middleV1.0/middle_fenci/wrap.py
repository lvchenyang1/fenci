from .model.jieba import jieba_wrap
from .model.pyltp import pyltp_wrap
from .model.pynlpir import pynlpir_wrap
from .config import configini
import chardet
import docx
import os
#对不用方式的分词 使用同一的方法进行封装

userConf = configini.get_conf()


#整体进行分词处理
class All_model_fenci(object):
    '''
    对内容进行分词处理
    :param 文件绝对路径/字符串，模型，输出类型(1字符串，2列表)，分隔符
    :return list or str
    '''
    def __init__(self,contents_dir,model,types,*args,**kwargs):
        self.contents_dir = contents_dir
        self.model = model
        self.types = types
        self.separator = kwargs.get("separator")
        self.flag = kwargs.get("flag")
        print(self.separator)
        #对第一个参数进行判断
        if os.path.isfile(self.contents_dir):
            extension = os.path.splitext(self.contents_dir)[1]


            if extension == ".docx" or ".doc":

                try:
                    document = docx.Document(self.contents_dir)
                    full = []
                    for paragraph in document.paragraphs:
                        full.append(paragraph.text)
                    self.contents = "".join(full)


                except Exception as err:
                    print("   ")
            if extension == ".txt" or ".text":
                try:
                    with open(self.contents_dir, "rb") as r_contents:
                        r_content = r_contents.read()
                    cc = chardet.detect(r_content)
                    encoding_content = cc.get("encoding")
                    with open(self.contents_dir, encoding=encoding_content) as file_object:
                        self.contents = file_object.read()
                except Exception as err:
                    print("   ")
        else:
            self.contents = self.contents_dir

    def fenci(self):
        #判断模型
        if self.model == "jieba":
            #判断是否添加词性
            if self.flag == "yes":
                if self.types == "str":
                    jiebafenci = jieba_wrap.Jieba_fenci(self.contents,separator = self.separator,flag = self.flag)
                    jieba_result = jiebafenci.jieba_flag()
                    return jieba_result
                if self.types == "list":
                    jiebafenci = jieba_wrap.Jieba_fenci(self.contents,flag = self.flag)
                    jieba_list_result = jiebafenci.jieba_flag_list()
                    return jieba_list_result
            else:
                if self.types == "str":
                    jiebafenci = jieba_wrap.Jieba_fenci(self.contents,separator = self.separator,flag = self.flag)
                    jieba_result = jiebafenci.jieba_quan()
                    return jieba_result
                if self.types == "list":
                    jiebafenci = jieba_wrap.Jieba_fenci(self.contents,flag = self.flag)
                    jieba_list_result = jiebafenci.jieba_quan_list()
                    return jieba_list_result
        #判断为pyltp
        if self.model == "ltp":
            if self.flag == "yes":
                if self.types == "str":
                    pyltpfenci = pyltp_wrap.Pyltp_fenci(self.contents,separator = self.separator,flag = self.flag)
                    pyltp_flag_result = pyltpfenci.pyltp_flag()
                    return pyltp_flag_result
                if self.types == "list":
                    pyltpfenci = pyltp_wrap.Pyltp_fenci(self.contents,flag = self.flag)
                    pyltp__flag_list_result = pyltpfenci.pyltp_flag_list()
                    return  pyltp__flag_list_result
            else:
                if self.types == "str":
                    pyltpfenci = pyltp_wrap.Pyltp_fenci(self.contents,separator = self.separator,flag = self.flag)
                    pyltp_result = pyltpfenci.pyltp_fenci()
                    return pyltp_result
                if self.types == "list":
                    pyltpfenci = pyltp_wrap.Pyltp_fenci(self.contents,flag = self.flag)
                    pyltp_list_result = pyltpfenci.pyltp_fenci_list()
                    return  pyltp_list_result

        if self.model == "nlpir":
            if self.flag == "yes":
                if self.types == "str":
                    pynlpirfenci = pynlpir_wrap.Pynlpir_fenci(self.contents, separator=self.separator, flag=self.flag)
                    pynlpir_result = pynlpirfenci.pynlpir_fenci_flag()
                    return pynlpir_result
                if self.types == "list":
                    pynlpirfenci = pynlpir_wrap.Pynlpir_fenci(self.contents, separator=self.separator, flag=self.flag)
                    pynlpir_result = pynlpirfenci.pynlpir_fenci_flag_list()
                    return pynlpir_result
            else:
                if self.types == "str":
                    pynlpirfenci = pynlpir_wrap.Pynlpir_fenci(self.contents,separator = self.separator,flag = self.flag)
                    pynlpir_result = pynlpirfenci.pynlpir_fenci()
                    return pynlpir_result
                if self.types == "list":
                    pynlpirfenci = pynlpir_wrap.Pynlpir_fenci(self.contents, separator=self.separator, flag=self.flag)
                    pynlpir_result = pynlpirfenci.pynlpir_fenci_list()
                    return pynlpir_result
        if self.model == "4":
            jiebafenci = jieba_wrap.Jieba_fenci(self.contents)
            result = jiebafenci.jieba_quan_list()
            return result

#整体加载字典,自动加载public_dict中的路径 默认需要
class All_model_loadDict(object):

    def loadDict(self):
        userLoadDict = jieba_wrap.Jieba_LoadDict()

        c = userLoadDict.jieba_loadD()

        return c





