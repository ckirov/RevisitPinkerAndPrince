# Revisiting Pinker & Prince
This is the companion repository for:

Christo Kirov and and Ryan Cotterell. Recurrent Neural Networks in Linguistic Theory: Revisiting Pinker and Prince (1988) and the Past Tense Debate. TACL. 2018.

DISCLAIMER: The provided data combined with the commands below should produce similar results to the published paper, but they are not guaranteed to be identical. The provided commands may also change depending on your version of OpenNMT, etc. 

# Experiment 1

Create datasets for network training:

```bash
cd experiment_1
python createDatasets.py
cd ..
```

OpenNMT-py commands, assuming OPEN_NMT_DIR is the location of your OpenNMT installation:

```bash
python OPEN_NMT_DIR/preprocess.py -train_src experiment_1/src_train.txt -train_tgt experiment_1/tgt_train.txt -valid_src experiment_1/src_valid.txt -valid_tgt experiment_1/tgt_valid.txt -save_data experiment_1/data

python OPEN_NMT_DIR/train.py -rnn_size 100 -epochs 100 -learning_rate_decay 1.0 -word_vec_size 300 -brnn -brnn_merge concat -optim adadelta -batch_size 20 -data experiment_1/data.train.pt -save_model experiment_1/model

python OPEN_NMT_DIR/translate.py -beam_size 12 -verbose -model experiment_1/MODEL_FILE -src experiment_1/src_test.txt -output experiment_1/test-decoded.txt
```

The Wug portion of the experiment was performed by training on all the original past test data provided by Albright & Hayes (2003). Their original Wugs, converted into network-compatible test data, are provided.

# Experiment 2

Create datasets for network training (this assumes Experiment 1 was already run, in order to compare performance on the same test verbs):

Create datasets for network training:

```bash
cd experiment_2
python createDatasets.py
cd ..
```

OpenNMT-py commands:

```bash
python OPEN_NMT_DIR/preprocess.py -train_src experiment_2/src_train_tagged.txt -train_tgt experiment_2/tgt_train_tagged.txt -valid_src experiment_2/src_valid_tagged.txt -valid_tgt experiment_1/tgt_valid.txt -save_data experiment_2/data

python OPEN_NMT_DIR/train.py -rnn_size 100 -epochs 100 -learning_rate_decay 1.0 -word_vec_size 300 -brnn -brnn_merge concat -optim adadelta -batch_size 20 -data experiment_1/data.train.pt -save_model experiment_1/model

python OPEN_NMT_DIR/translate.py -beam_size 12 -verbose -model experiment_2/MODEL_FILE -src experiment_2/src_test_tagged.txt -output experiment_2/test-decoded.txt
```
