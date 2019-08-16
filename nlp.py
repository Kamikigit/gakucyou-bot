import sys
import MeCab
m = MeCab.Tagger("-Ochasen")
print(m.parse("軽部征夫"))
