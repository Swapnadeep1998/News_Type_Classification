import tensorflow as tf
import numpy as np


class Model:
    def __init__(self,vocab_size:int, embedding_dim:int, no_classes:int):
        
        self.model = tf.keras.Sequential([
            tf.keras.layers.Embedding(vocab_size, embedding_dim),
            tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(embedding_dim)),           
            tf.keras.layers.Dense(embedding_dim, activation='relu'),
            tf.keras.layers.Dense(no_classes, activation='softmax')
            ])
    
        self.model.compile(loss='sparse_categorical_crossentropy', 
                           optimizer='adam', metrics=['accuracy'])

    def summary(self):
        return self.model.summary()

    def fit(self, epochs:int, X_train:np.array,
            y_train:np.array, X_test:np.array,
            y_test:np.array, batch_size:int,
            model_dir:str 
            ):
        
        callbacks=tf.keras.callbacks.ModelCheckpoint(
            model_dir,            
            save_best_only=True
        )

        self.model.fit(X_train, y_train, epochs=epochs, 
                    batch_size=batch_size,
                    steps_per_epoch=len(X_train)//batch_size,
                    validation_data=(X_test, y_test),
                    validation_steps=len(X_test)//batch_size,
                    callbacks=[callbacks])



