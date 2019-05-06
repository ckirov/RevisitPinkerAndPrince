# -*- coding: utf-8 -*-

import codecs
import cPickle
import random
from collections import defaultdict
import pandas as pd

#set up output file
fout_src_train = codecs.open('src_train.txt','wb','utf-8')
fout_tgt_train = codecs.open('tgt_train.txt','wb','utf-8')
fout_src_valid = codecs.open('src_valid.txt','wb','utf-8')
fout_tgt_valid = codecs.open('tgt_valid.txt','wb','utf-8')
fout_src_test = codecs.open('src_test.txt','wb','utf-8')
fout_tgt_test = codecs.open('tgt_test.txt','wb','utf-8')

#read in  data
fin = codecs.open('english_merged.txt','rb','utf-8')

sources = []
targets = []

for line in fin:
	parts = line.strip().split()
	lemma = parts[2]
	form = parts[3]
	sources.append(' '.join(lemma))
	targets.append(' '.join(form))
fin.close()

pairs = zip(sources,targets)
random.shuffle(pairs)

#split into train and test
train = pairs[:int(.8*len(pairs))]
valid = pairs[int(.8*len(pairs)):int(.9*len(pairs))]
test = pairs[int(.9*len(pairs)):]

#write the outputs
for s,t in train:
	fout_src_train.write(s + '\n')
	fout_tgt_train.write(t + '\n')

for s,t in valid:
	fout_src_valid.write(s + '\n')
	fout_tgt_valid.write(t + '\n')

for s,t in test:
	fout_src_test.write(s + '\n')
	fout_tgt_test.write(t + '\n')



fout_src_train.close()
fout_tgt_train.close()
fout_src_valid.close()
fout_tgt_valid.close()
fout_src_test.close()
fout_tgt_test.close()
