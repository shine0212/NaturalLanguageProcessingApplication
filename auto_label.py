import numpy as np
from utils.utils import convert_to_one_hot, read_glove_vecs, read_csv
from utils.assistant import sentence_level_model, sentences_to_indices
from utils.func2Index import label2Index, idex_and_label
from keras.models import load_model
fromFile    = './zQC_Spec/z_SwT_Data/ExampleLabel_02.csv'
toFile      = "./zQC_Spec/z_SwT_Data/ExampleLabel_0X.csv"
import os

__, index2label = label2Index()
X, Y = read_csv('./zQC_Spec/z_SwT_Data/ExampleLabel_02.csv', xonly= False)

maxLen = 30

cwd = os.getcwd()  # Get the current working directory (cwd)

word_to_index, index_to_word, word_to_vec_map = read_glove_vecs(cwd + '/data/glove_6B_50d.txt', "./Data/NewWords.txt")

X_indices = sentences_to_indices(X, word_to_index, maxLen)

model = load_model("./Models/FunctionModel.h5")

pred = model.predict(X_indices)
preds = np.argmax(pred, axis=1).tolist()
idex_and_label(fromFile, toFile, preds)

