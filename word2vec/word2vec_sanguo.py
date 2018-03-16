# -*- coding: utf-8 -*-：

import sys
import jieba
from gensim.models import word2vec
import logging

reload(sys)
sys.setdefaultencoding('utf8')



f1 = open("三国演义.txt")
f2 = open("三国演义_result.txt", 'a')
lines = f1.readlines()
for line in lines:
    line.replace('\t', '').replace('\n', '').replace(' ', '')
    seg_list = jieba.cut(line, cut_all=False)
    f2.write(" ".join(seg_list))

f1.close()
f2.close()


logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', level=logging.INFO)
sentences = word2vec.Text8Corpus(u"三国演义_result.txt")
model = word2vec.Word2Vec(sentences, size=200)

print (model)
try:
    y1 = model.similarity(u"曹操", u"曹丞相")
except KeyError:
    y1 = 0
print( "similarity：", y1)

y2 = model.most_similar(u"刘备", topn=20)
print ("liubei：\n")
for item in y2:
    print (item[0], item[1])
print("\n")

print("y3")
y3 =model.most_similar([u'刘备', u'关羽'], [u'张飞'], topn=3)
for item in y3:
    print (item[0], item[1])
print("\n")

