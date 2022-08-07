import fitz
import pandas as pd
import os

def get_path():
    final_path = []
    path1 = input('Enter the Path for AI files: ')
    print('Path Registered Successfully')
    path2 = input('Enter the path for WEB files: ')
    print("Path Registered Successfully")
    final_path.append(path1)
    final_path.append(path2)
    return final_path

def get_final_dataframe(path,flag):
    df = pd.DataFrame(columns=['Text','Label'])
    content = []
    for file in os.listdir(path):
        if file.endswith('.pdf'):
            doc = fitz.open(path+'\\'+file) # doc vanne pdf file ho 
            content_temp = ''
            for page in range(len(doc)): # pdf ma kati ota page xa tyo sab herxa yo loop le
                content_temp = content_temp+doc[page].get_text()
                print(content_temp)
            content.append(content_temp)

    df['Text'] = content
    df['Label'] = flag
    print(df)
    return df

def get_content_of_pdfs(file_path):
    for path in file_path:
        if '\\AI' in path:
            print("Here is AI files")
            print(path)
            df_ai = get_final_dataframe(path,1) # here 1 is flag

        elif '\\WEB' in path:
            print('Here is WEB files')
            print(path)
            df_web = get_final_dataframe(path,0) # here 0 is flag

    df = df_ai.append(df_web)
    print(df)
    return df

def get_content(file_path):
    df = pd.DataFrame(columns = ['Text', 'Label']) # dataframe
    df = get_content_of_pdfs(file_path)
    return df

def dataset_generate():
    file_path = get_path()
    dataset = get_content(file_path)
    print(file_path)
    dataset.to_csv('Dataset.csv')

if __name__=='__main__':
    dataset_generate()