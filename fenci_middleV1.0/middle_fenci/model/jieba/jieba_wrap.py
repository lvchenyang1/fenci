# -*- coding: UTF-8 -*-
import jieba
import os
import jieba.posseg as pseg
import chardet
# jieba.cut 方法接受三个输入参数: 需要分词的字符串；cut_all 参数用来控制是否采用全模式；HMM 参数用来控制是否使用 HMM 模型
# jieba.cut_for_search 方法接受两个参数：需要分词的字符串；是否使用 HMM 模型。该方法适合用于搜索引擎构建倒排索引的分词，粒度比较细

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class Jieba_fenci(object):
    '''
    :param 分词内容 字符串分隔符
    :return 字符串或列表
    '''
    def __init__(self,fenci_message,*args,**kwargs):
        self.message = fenci_message
        self.separator = kwargs.get("separator")
        self.flag= kwargs.get("flag")
    def jieba_quan(self):
        list0 = jieba.cut(self.message, cut_all=True)  # 全模式
        if self.separator == None:
            jieba_result = " ".join(list0)
            return jieba_result
        else:
            jieba_result = "{}".format(self.separator).join(list0)
        return jieba_result

    def jieba_quan_list(self):
        list_content = jieba.lcut(self.message, cut_all=True)#全模式列表
        return list_content
    def jieba_jingque(self):

        jieba.cut(self.message,cut_all=False)#精确模式

    def jieba_search(self):#搜索模式
        jieba.cut_for_search(self.message)

    """词性标注"""
    def jieba_flag(self):
        words = pseg.cut(self.message)
        if self.separator ==None:
            result_content = "".join('%s' % id for id in words)

        else:
            result_content =" {}".format(self.separator).join('%s' % id for id in words)
        return result_content

        # jieba_result = " ".join(words)
        # return jieba_result

    def jieba_flag_list(self):
        words = pseg.cut(self.message)
        result_list = []
        for word in words:
            dd = r'{}'.format(word)
            result_list.append(dd)
        return(result_list)

class Jieba_LoadDict(object):

    def jieba_loadD(self):#词典格式和 dict.txt 一样，一个词占一行；每一行分三部分：词语、词频（可省略）、词性（可省略），用空格隔开，顺序不可颠倒。file_name 若为路径或二进制方式打开的文件，则文件必须为 UTF-8 编码。
        # file_name 为文件类对象或自定义词典的路径
        #获取当前绝对路径

        dir_path = os.path.join(BASE_DIR,"public_dict")

        for root, dirs, files in os.walk(dir_path):
            for f in files:
                user_file_name =os.path.join(dir_path,f)

                with open(user_file_name, "rb") as r_contents:
                    r_content = r_contents.read()
                cc = chardet.detect(r_content)
                encoding_content = cc.get("encoding")
                with open(user_file_name, encoding=encoding_content) as file_object_r:
                    txt_content = file_object_r.read()
                with open(user_file_name,"w", encoding="UTF-8") as file_object_w:
                    file_object_w.write(txt_content)
                jieba.load_userdict(user_file_name)

        return ("加载成功")

