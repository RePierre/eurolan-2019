# This script merges the manually annotated corpus with the GOLD corpus for training.
# Author: Cristian Pădurariu
from bs4 import BeautifulSoup as bs
import sys

args = sys.argv
filepath1 = args[1]
filepath2 = args[2]

f = open(filepath1, "r", encoding="utf-8")
xml1 = bs(f.read(), 'xml')
f = open(filepath2, "r", encoding="utf-8")
xml2 = bs(f.read(), 'xml')

for sent in xml2.find_all("sentence"):
    xml1.treebank.append(sent)

f = open("train.xml", "w", encoding="utf-8")
f.write(str(xml1))
