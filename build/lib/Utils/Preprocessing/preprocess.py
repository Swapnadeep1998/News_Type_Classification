from Utils import config
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from tensorflow.keras.preprocessing.text import Tokenizer, tokenizer_from_json
from tensorflow.keras.preprocessing.sequence import pad_sequences
from nltk.corpus import stopwords
import io
import json
import numpy as np

VOCAB_SIZE = config.VOCAB_SIZE
OOV_TOKEN = config.OOV_TOKEN
TOKENIZER_PATH=config.TOKENIZER_JSON_PATH
PADDING_TYPE=config.PADDING_TYPE
TRUNC_TYPE=config.TRUNC_TYPE
MAX_LENGTH=config.MAX_LEN


def remove_stop_words(text: str):

    """
    Remove words 
    which don't contribute 
    much in classification
    """

    Stopwords = set(stopwords.words('english'))
    for word in Stopwords:
        token = ' ' + word + ' '
        text = text.replace(token,' ')
    return text

def fit_tokenizer(texts: list):

    """
    Tokenize sentences 
    into words and create
    numerical representations
    """

    tokenizer = Tokenizer(num_words=VOCAB_SIZE, oov_token=OOV_TOKEN)
    tokenizer.fit_on_texts(texts)   
    tokenizer_json = tokenizer.to_json()

    with io.open(TOKENIZER_PATH, 'w', encoding='utf-8') as f:
        f.write(json.dumps(tokenizer_json, ensure_ascii=False))


def gen_padded_sequences(texts: list, tokenizer_path=TOKENIZER_PATH):

    """
    Load the trained tokenizers,
    create sequence of tokens,
    and pad to have equal length
    of sequences
    """

    with open(tokenizer_path) as f:
        data = json.load(f)
        tokenizer = tokenizer_from_json(data)

    sequences = tokenizer.texts_to_sequences(texts)
    padded_seq = pad_sequences(sequences, 
                               maxlen=MAX_LENGTH,
                               padding=PADDING_TYPE, 
                               truncating=TRUNC_TYPE)

    return padded_seq
    

def get_labels(train_labels:list, val_labels:list):

    """
    Generating tokens 
    for the labels, also known
    as label binarizer
    """

    label_tokenizer = Tokenizer()
    label_tokenizer.fit_on_texts(train_labels)

    train_label_seq = np.array(label_tokenizer.texts_to_sequences(train_labels))
    val_label_seq = np.array(label_tokenizer.texts_to_sequences(val_labels))

    return train_label_seq, val_label_seq













