# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import tensorflow as tf
import pickle
import warnings
import re
import nltk
stemmer = nltk.SnowballStemmer("english")
from nltk.corpus import stopwords
import string
stopword=set(stopwords.words('english'))

warnings.filterwarnings('ignore')

model = tf.keras.models.load_model("HOLD_Mark3_OF_2.h5")
pad_seq_file = open('pad_seq-Mark3_2.pkl', 'rb')
pad_sequences = pickle.load(pad_seq_file)
tok_file = open('HOLD-Mark3_tokenizer_2.pkl', 'rb')
tokenizer = pickle.load(tok_file)


def clean(text):
    text = str(text).lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = [word for word in text.split(' ') if word not in stopword]
    text=" ".join(text)
    text = [stemmer.stem(word) for word in text.split(' ')]
    text=" ".join(text)
    return text

def classify_HOLD(msg):
    msg[0] = clean(msg[0])
    msg_seq = tokenizer.texts_to_sequences(msg)
    padded_seq = pad_sequences(msg_seq, maxlen=26)
    print(padded_seq)
    return ((model.predict(padded_seq))*100)

def main(string):
    msg = []
    msg.append(string)

    res = classify_HOLD(msg)[0][0]
    print("The Model is " + str(res) + " % sure that this is a Hate Speech")
    return res
# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
