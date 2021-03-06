import pandas as pd
from Utils.Preprocessing.preprocess import remove_stop_words, fit_tokenizer, gen_padded_sequences
from Utils.Preprocessing.preprocess import get_labels

import numpy as np

class DataGen:
    def __init__(self, csv_path:str, train_test_split: float):     
           
        self.dataframe = pd.read_csv(csv_path)
        self.dataframe['text'].map(lambda x: remove_stop_words(x))

        self.articles = self.dataframe['text'].tolist()
        
        self.categories = self.dataframe['category'].tolist()

        train_len = int(len(self.articles)*train_test_split)

        self.train_articles = self.articles[:train_len]
        self.train_labels = self.categories[:train_len]

        fit_tokenizer(self.train_articles)

        self.val_articles = self.articles[train_len:]
        self.val_labels = self.categories[train_len:]
        
        
        

    def get_train_test_seq(self):

        train_seq = np.array(gen_padded_sequences(self.train_articles))
        val_seq = np.array(gen_padded_sequences(self.val_articles))

        train_labels_seq, val_labels_seq = get_labels(self.train_labels, self.val_labels)

        return train_seq, train_labels_seq, val_seq, val_labels_seq

        
        
        