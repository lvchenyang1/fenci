import pynlpir


class Pynlpir_fenci(object):
    def __init__(self,content,**kwargs):
        self.pynlpir_content = content
        self.separator = kwargs.get("separator")
        self.flag = kwargs.get("flag")

    def pynlpir_fenci(self):
        if self.separator:
            pynlpir.open()
            s = self.pynlpir_content
            str = s.encode('utf-8')

            wordslist1 = pynlpir.segment(str)
            # wordlist1中列表包含分词和它的词性
            result_list = []
            for con in wordslist1:
                result_list.append(con[0])
            result = " {}".format(self.separator).join(result_list)
            pynlpir.close()
            return result
        else:
            pynlpir.open()
            s = self.pynlpir_content
            str = s.encode('utf-8')

            wordslist1 = pynlpir.segment(str)
            # wordlist1中列表包含分词和它的词性
            result_list = []
            for con in wordslist1:
                result_list.append(con[0])
            result = " ".join(result_list)
            pynlpir.close()
            return result

    def pynlpir_fenci_list(self):
        pynlpir.open()
        s = self.pynlpir_content
        str = s.encode('utf-8')

        wordslist1 = pynlpir.segment(str)
        # wordlist1中列表包含分词和它的词性
        result_list = []
        for con in wordslist1:
            result_list.append(con[0])

        pynlpir.close()
        return result_list

    def pynlpir_fenci_flag(self):
        pynlpir.open()
        s = self.pynlpir_content
        str = s.encode('utf-8')

        wordslist1 = pynlpir.segment(str)
        # wordlist1中列表包含分词和它的词性

        list1 = []
        list2 = []
        result_flag_list = []
        for con in wordslist1:
            list1.append(con[0])
        for con in wordslist1:
            list2.append(con[1])
        for k in range(len(list1)):
            result_flag_list.append(list1[k] + "/" + list2[k])

        result_flag = " ".join(result_flag_list)

        return result_flag

    def pynlpir_fenci_flag_list(self):
        pynlpir.open()
        s = self.pynlpir_content
        str = s.encode('utf-8')

        wordslist1 = pynlpir.segment(str)
        # wordlist1中列表包含分词和它的词性

        list1 = []
        list2 = []
        result_flag_list = []
        for con in wordslist1:
            list1.append(con[0])
        for con in wordslist1:
            list2.append(con[1])
        for k in range(len(list1)):
            result_flag_list.append(list1[k] + "/" + list2[k])

        return result_flag_list



#得到他的词性
class Pynlpir_partofspeech(object):
    def __init__(self, content, **kwargs):
        self.pynlpir_content = content
        self.separator = kwargs.get("separator")

    def pynlpir_fenci(self):

        pynlpir.open()
        s = self.pynlpir_content
        str = s.encode('utf-8')

        wordslist1 = pynlpir.segment(str)
        # wordlist1中列表包含分词和它的词性
        return wordslist1


