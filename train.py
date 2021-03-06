from Utils.Models.model import Model
from Utils.DataPipeline.data import DataGen
from Utils import config

VOCAB_SIZE = config.VOCAB_SIZE
EMBEDDING_DIM = config.EMBEDDING_DIM
CSV_PATH = config.CSV_PATH
split_ratio = config.TRAIN_TEST_SPLIT_RATIO
no_of_classes = config.NO_CLASSES
epochs = config.EPOCHS
batch_size = config.BATCH_SIZE
model_dir = config.MODEL_DIR



if __name__=='__main__':
    data_gen = DataGen(csv_path=CSV_PATH, train_test_split=split_ratio)

    X_train, y_train, X_test, y_test = data_gen.get_train_test_seq()   

    print(X_test.shape) 

    model = Model(vocab_size=VOCAB_SIZE, embedding_dim=EMBEDDING_DIM, no_classes=no_of_classes)

    model.fit(
        epochs=epochs, X_train=X_train, y_train=y_train, 
        X_test=X_test, y_test=y_test, batch_size=batch_size,
        model_dir=model_dir    
    )


