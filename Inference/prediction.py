import tensorflow as tf
import numpy as np
from Utils.Preprocessing.preprocess import remove_stop_words, gen_padded_sequences
from Utils import config

class Classifier:
    def __init__(self, model_dir:str):
        self.model = tf.keras.models.load_model(model_dir)

    def predict(self, texts:list):
        texts = list(map(remove_stop_words, texts))
        sequence = np.array(gen_padded_sequences(texts))
        predictions = self.model.predict(sequence)
        return predictions




