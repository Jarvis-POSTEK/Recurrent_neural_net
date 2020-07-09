import numpy
import re
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils

# load ascii text and covert to lowercase
filename = "tester_text.txt"
raw_text = open(filename, 'r', encoding='utf-8').read()
raw_text = raw_text.lower()
raw_text = re.split(", |"" |\\n|!| |;|,", raw_text)
raw_text = [i for i in raw_text if i != '']
raw_text = [i for i in raw_text if i != ',']
# create mapping of unique chars to integers
chars = sorted(list(set(raw_text)))
char_to_int = dict((c, i) for i, c in enumerate(chars))

n_chars = len(raw_text)
n_vocab = len(chars)
print ("Total Characters: ", n_chars)
print ("Total Vocab: ", n_vocab)


print(raw_text)
print(chars)
# prepare the dataset of input to output pairs encoded as integers
seq_length = 100
dataX = []
dataY = []
for i in range(0, n_chars - seq_length, 1):
    seq_in = raw_text[i:i + seq_length]
    seq_out = raw_text[i + seq_length]
    for char in seq_in:
        if char is not "\\n":
            dataX.append(char_to_int[char])
    dataY.append(char_to_int[seq_out])
n_patterns = len(dataX)

print ("Total Patterns: ", n_patterns)