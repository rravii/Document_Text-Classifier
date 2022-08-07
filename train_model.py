import pandas as pd # features and labels in tabular form ma lana ko lagi 
from sklearn.naive_bayes import MultinomialNB 
from sklearn.feature_extraction.text import CountVectorizer # countvectorizer -> convert to numerical form so ai can undesrtand & count the words repeated
import string
import nltk # natural language processing ko lagi
from nltk.corpus import stopwords # stopwords-> those words that are useless are removed by stopwords
import fitz # helps to read pdf content & convert to images as well
import pickle # model load and dump

nltk.download('stopwords') # stopwords download
vectorizer = CountVectorizer() # words to number-> vectorizer

def pre_process_df(): # remove index from csv file 
    f_df = pd.DataFrame(columns=['Text','Label']) # Text ra label vako Dataframe initialized
    df = pd.read_csv('Dataset.csv')
    f_df['Text'] = df['Text'] # f_df ma df ko Text matra haleko
    f_df['Label'] = df['Label'] # f_df ma df ko Label matra haleko
    # print(f_df)
    return f_df

def input_process(text):
    translator = str.maketrans('','',string.punctuation) # placing empty in place of punctuation
    nopunc = text.translate(translator) # punctuation removed & meaningless words removed
    words = [word for word in nopunc.split() if word.lower() not in stopwords.words('english')] # list comprehension method.........here english is english language
    return ' '.join(words)

def remove_stop_words(input):
    final_input = []
    for line in input:
        line = input_process(line)
        final_input.append(line)
    return final_input

def train_model(df): # stopwords removed like \n, is, am, are and so on
    input = df['Text']
    output = df['Label']
    input = remove_stop_words(input)
    df['Text'] = input
    input = vectorizer.fit_transform(input) # mathematical form ma harek word ko numerical value
    # input = df['Text']
    # print(df)
    nb = MultinomialNB() # initilized new model, here count is needed
    nb.fit(input, output) # mapping and create model
    return nb


if __name__=='__main__':
    df = pre_process_df()
    model = train_model(df)
    pickle.dump(model,open('classifier.model','wb'))
    pickle.dump(vectorizer,open('vectorizer.pickle','wb'))