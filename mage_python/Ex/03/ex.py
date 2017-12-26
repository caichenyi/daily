# encoding: utf-8
# Author: Cai Chenyi

desc = 'My Name is KK'
# print(desc[3])
# print(desc[3:10])
# print(len(desc))

# while True:
#     score = input('输入分数')
#     if not score.isdigit():
#         print('输入有错')
#         continue
#     else:
#         score = int(score)
#     if score >= 90:
#         print('优秀')
#     elif score >= 80:
#         print('良好')
#     elif score >= 60:
#         print('及格')
#     else:
#         print('不及格')

# languages = ['python', 'java', 'python', 'c', 'c++', 'go', 'c#', 'c++', 'lisp', 'c', 'javascript', 'java', 'python', 'matlab', 'python', 'go', 'java']
# languages_dict = {}
#
# for language in languages:
#     if language not in languages_dict:
#         languages_dict[language] = 1
#     else:
#         languages_dict[language] += 1
# print(languages_dict)
# article = 'I was not delivered unto this world in defeat, nor does failure course in my veins. I am not a sheep waiting to be prodded by my shepherd. I am a lion and I refuse to talk, to walk, to sleep with the sheep. I will hear not those who weep and complain, for their disease is contagious. Let them join the sheep. The slaughterhouse of failure is not my destiny.'
# stat = {}

# for i in article:
#     if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
#         if i not in stat:
#             stat[i] = 1
#         else:
#             stat[i] += 1
# print(stat)

# for ch in article:
#     if not ((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')):
#         continue
#     if ch not in stat:
#         stat[ch] = 0
#     stat[ch] += 1
# print(stat)

# languages = ['python', 'java', 'python', 'c', 'c++', 'go', 'c#', 'c++', 'lisp', 'c', 'javascript', 'java', 'python', 'matlab', 'python', 'go', 'java']
# stat_dict = {}
#
# for language in languages:
#     stat_dict[language] = stat_dict.get(language, 0) + 1
# print(stat_dict)

me = {'name': 'kk', 'addr':'shanxi', 'age':30}
print(me.items())
print(list(me.items()))
for e in me.items():
    print(e)