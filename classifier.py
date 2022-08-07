import sklearn
import nltk
import pickle
import fitz 
from sklearn.feature_extraction.text import CountVectorizer
from train_model import input_process

def load_model_and_vectorizer():
    model = pickle.load(open("classifier.model","rb"))
    vectorizer = pickle.load(open("vectorizer.pickle","rb"))
    return model, vectorizer

# classify whether the provided file is AI or WEB
# if __name__=="__main__":
#     model,vectorizer = load_model_and_vectorizer()
#     path = input("\nEnter path of file: \n")
#     doc = fitz.open(path)
#     content = ''
#     for page in range(len(doc)):
#         content = content + doc[page].get_text()

#     content = input_process(content)
#     content = vectorizer.transform([content])
#     pred = model.predict(content)
#     if pred[0]==1:
#         print('\nOutput:\n Provided document is about AI')
#     else:
#         print('\nOutput:\n Provided document is about Web')

# classify whether the provided input line is about AI or WEB
if __name__=="__main__":
    model,vectorizer = load_model_and_vectorizer()
    input_text = input("\nEnter the text of either AI or WEB:\n ")
    content = input_process(input_text)
    content = vectorizer.transform([content])
    pred = model.predict(content)
    if pred[0]==1:
        print('\nOutput:\n Provided text is about AI')
    else:
        print('\nOutput:\n Provided Text is about Web')
