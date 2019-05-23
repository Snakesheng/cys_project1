import re

# s = "Levi:1994, Sunny:1993"
# pattern = r"(\w+):(\d+)"

# 　re模块调用
# l = re.findall(pattern, s)
# print(l)

#  compile对象调用
# regex = re.compile(pattern)
# l = regex.findall(s, 0, 11)
# print(l)

#　　切割字符串
# s = "hello world how are  you  L-body"
# # l = re.split(r'[^\w]+', s)
# l = re.split(r'\W+', s)
# print(l)

#　　替换字符串
s = "时间 : 2019/05/17"
# ns = re.sub(r'/', '-', s)
# ns = re.sub(r'/', '-', s, 1)
#  返回多个替换个数　
# ns = re.subn(r'/', '-', s)
ns = re.subn(r'\d+', '00', s)
print(ns)











