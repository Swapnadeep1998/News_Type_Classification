import os

VOCAB_SIZE=5000
EMBEDDING_DIM=64
MAX_LEN=200
NO_CLASSES=5
EPOCHS=10
BATCH_SIZE=16


TRUNC_TYPE='post'
PADDING_TYPE='post'
OOV_TOKEN='<OOV>'
TRAIN_TEST_SPLIT_RATIO=0.8
LABELS=['business', 'entertainment', 'politics', 'sport', 'tech']

TOKEN_FILE_NAME='tokenizer.json'
CSV_FILE_NAME='bbc-text.csv'
MODEL_FILE_NAME='model-v1.h5'
TOKENIZER_JSON_PATH=os.path.join('.', 'Artefacts', TOKEN_FILE_NAME)
CSV_PATH=os.path.join('.', 'Datasets', CSV_FILE_NAME)
MODEL_DIR=os.path.join('.', 'Artefacts', MODEL_FILE_NAME)
