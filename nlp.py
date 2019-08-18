import sys
import MeCab
import re
from collections import Counter

with open("column.txt") as f:
    data = f.read()

mecab = MeCab.Tagger()
parse = mecab.parse(data)
lines = parse.split('\n')
items = [re.split('[\t,]', line) for line in lines]
words = [item[0]
         for item in items 
         if item[0] not in ('ESO', '')]

counter = Counter(words)
for word, cnt in counter.most_common():
    with open("mustache.txt", "a") as f:
        f.write(f"{word}:{cnt}")


 
