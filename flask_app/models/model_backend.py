import pickle
from typeguard import typechecked
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
import spacy
import pandas as pd
import json



class TextPreProcessing:
    @typechecked
    def __init__(self, sentences:str):
        self.sentences = sentences

    def RemoveSmallWords(self, Series):
        t = Series.str.split(expand=True).stack()
        return t.loc[t.str.len() >= 4].groupby(level=0).apply(' '.join)

    def TextPreProcessing(self):
        a_lemmas = []
        nlp = spacy.load('en_core_web_md')
        corpus = nlp(self.sentences)
        lemmas = [token.lemma_ for token in corpus]
        a_lemmas.append(pd.Series([lemma for lemma in lemmas if (lemma.isalpha() and nlp.vocab[lemma].is_stop==False)]))
        a_lemmas = self.RemoveSmallWords(a_lemmas[0]) 
        a_lemmas.reset_index(inplace = True, drop = True)
        a_lemmas = ' '.join(a_lemmas)
        return a_lemmas    


class ModelPrediction:
    @typechecked
    def __init__(self, original_sentences: str, preprocessed_sentence:str):
        self.original_sentences = original_sentences 
        self.preprocessed_sentence = preprocessed_sentence 


    def Prediction(self):
        tfidf_vectorizer = pickle.load(open('./machine_leaning_models/tfidf.pickle',"rb"))
        svm_clf = pickle.load(open('./machine_leaning_models/svm_clf.pickle',"rb"))

        response = {}
        response["response"] = {
            "input_sentence":self.original_sentences,
            "sentence_preprocessed":self.preprocessed_sentence,
            "model_prediction":  int(svm_clf.predict(tfidf_vectorizer.transform([self.preprocessed_sentence]))[0])
        }
        
        return response 






    