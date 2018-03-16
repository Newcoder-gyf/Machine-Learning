# coding=UTF-8
import jieba

excludes = {"将军", "却说", "荆州", "二人", "不可", "不能", "如此", "商议", "如何", "主公", "军士", "左右", "军马", "引兵", "次日", "大喜", "天下", "东吴", "于是", "今日", "不敢", "魏兵","人马", "陛下", "一人"}

txt = open("三国演义.txt", "r", encoding="gb18030",errors="ignore").read()


words = jieba.lcut(txt)
counts = {}
for word in words:
   if len(word) == 1:
       continue
   elif word == "诸葛亮" or word == "孔明曰":
       rword = "孔明"
   elif word == "关公" or word == "云长":
       rword = "关羽"
   elif word == "玄德" or word == "玄德曰":
       rword = "刘备"
   elif word == "孟德" or word == "丞相":
       rword = "曹操"
   else:
       rword = word
   counts[rword] = counts.get(rword, 0) + 1
for word in excludes:
   del(counts[word])
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(10):
   word, count=items[i]
   print (word, count)


fo = open("三国人物出场次数.txt", "a")
for i in range(10):
   word, count=items[i]
   word = str(word)
   count = str(count)
   fo.write(word)
   fo.write(' ')
   fo.write(count)
   fo.write('\n')
   print (word, count)
print(items)
fo.close()