### **Document Classifier using Multinomial Naive Bayes:**

💦 **Introduction:**
            
           This project classify whether the provided pdf file or text is of web development or about AI. 
           The dataset used in this project are of two types i.e. AI document and WEB document. 

💦 **Packages:**

           💧	sklearn
           💧	nltk
           💧	pandas
           💧	PyMuPDF

💦 **Dataset Handling Introduction:**

            The documents of AI and WEB were created in ..._AI.pdf and ..._WEB.pdf format which is classified
            and separated into folders of AI and WEB using following code in cmd.

> **Dataset**>python

>	import os

>	import shutil

>	for file in os.listdir(os.getcwd()):

>	print(file)

>	for file in os.listdir(os.getcwd()):

>	if file.endswith("_AI.pdf"):

>	print(file)

>	os.mkdir("AI")

>	os.mkdir('WEB')

>	for file in os.listdir(os.getcwd()):

> if file.endswith("_AI.pdf"):

> shutil.copy(file,'AI/'+file)

> else:

> shutil.copy(file,'WEB/'+file)

>for file in os.listdir(os.getcwd()):

> if file.endswith(".pdf")

> os.remove(file)

💦 **Processes to run the code:**

        💧 Run Generate_Dataset.py file to create Dataset.csv file of dataset.
        💧 Run train_model.py file to create model i.e. classifier.model and vectorizer.pickle
        💧 Finally, run classifier.py file to test the model to classify AI or WEB file.

💦 **Output:**

        💧 Taking input as text:

![text](https://raw.githubusercontent.com/rravii/Document_Text-Classifier/master/Screenshots/text.JPG)

        💧 Taking input as pdf:

![pdf](https://raw.githubusercontent.com/rravii/Document_Text-Classifier/master/Screenshots/path.JPG)
