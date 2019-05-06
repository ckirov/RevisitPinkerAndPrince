# -*- coding: utf-8 -*-
"""Match train/test split from experiment 1, by lemma."""
import codecs
import cPickle
import random
from collections import defaultdict
import pandas as pd

#set up output file
fout_src_train = codecs.open('src_train_tagged.txt','wb','utf-8')
fout_tgt_train = codecs.open('tgt_train_tagged.txt','wb','utf-8')
fout_src_valid = codecs.open('src_valid_tagged.txt','wb','utf-8')
fout_src_test = codecs.open('src_test_tagged.txt','wb','utf-8')

#modify every line in the current valid data
fin = codecs.open('../experiment_1/src_valid.txt','rb','utf-8')
for line in fin:
	fout_src_valid.write('<V;PST> ' + line)
fin.close()
#modify every line in the current test data
fin = codecs.open('../experiment_1/src_test.txt','rb','utf-8')
for line in fin:
	fout_src_test.write('<V;PST> ' + line)
fin.close()

#read in a set of valid lemmas from the current train data
ok_lemmas = set()
fin =  codecs.open('../experiment_1/src_train.txt','rb','utf-8')
for line in fin:
	ok_lemmas.add(line.strip())
fin.close()

#read in  data
fin = codecs.open('english_merged.txt','rb','utf-8')

sources = []
targets = []

for line in fin:
	parts = line.strip().split()
	lemma = parts[3]
	form = parts[4]
	vec = '<' + parts[2] + '> '
	if vec != 'V;NFIN' and ' '.join(lemma) in ok_lemmas:
		sources.append(vec + ' '.join(lemma))
		targets.append(' '.join(form))	
fin.close()

pairs = zip(sources,targets)
random.shuffle(pairs)

#split into train and test
train = pairs

#write the outputs
for s,t in train:
	fout_src_train.write(s + '\n')
	fout_tgt_train.write(t + '\n')

fout_src_train.close()
fout_tgt_train.close()
fout_src_valid.close()
fout_src_test.close()
