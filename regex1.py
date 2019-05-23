import re

s = "2019年,建国70周年"
pattern = r"\d+"

#　　返回包含结果的迭代器
it = re.finditer(pattern, s)

# print(dir(next(it)))
# for i in it:
#     print(i)

# for i in it:
#     print(i.group())



#  完全匹配
# m = re.fullmatch(r'\w+', "hello1973")
# m = re.fullmatch(r'[0-9A-Za-z]+', "asdasd32323")
# print(m.group())

#  匹配开始位置　
# m = re.match(r'[A-Z]\w*', "Hello World")
# print(m.group())

#  匹配第一处
m = re.search(r'\S+', "好\n嗨 呦")
print(m.group())














