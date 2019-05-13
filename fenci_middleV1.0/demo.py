from middle_fenci import wrap

#加载字典方法，调用
d = wrap.All_model_loadDict()
d.loadDict()
"""
中间件的使用，将中间件嵌套在程序中
需要传递五个参数，其中contents_dir分析内容，model模型以及types输出类型必须传入，
separator分隔符和flag是否选择词性可以选择不传入。
"""
#设置需要进行分析的内容，可以为字符串或者文件的绝对路径，若为文件路径必须加上“r”避免转义。
user_contents_dir=r"E:\fenci_middleV1.0\test\111.txt"
#选择模型，目前只支持jieba,ltp,nlpir
user_model = "jieba"
#选择输出类型，有str字符串以及list列表
user_type = "list"
#设置分隔符，默认为“ ”空格
user_separator = " "
#设置是否显示词性，默认为False否
user_flag = False
#对中间件中的分词类进行实例化，并调用分词方法
c = wrap.All_model_fenci(contents_dir=user_contents_dir,model=user_model,types=user_type,separator=user_separator,flag=user_flag)
result_fenci = c.fenci()
print(result_fenci)


