import os.path
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from collections import Counter
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix

def prepro(train_dir):
    files = [os.path.join(train_dir,f) for f in os.listdir(train_dir)]
    lemm = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    for text in files:
        file = open(text,'r+')
        line = file.read()
        words = line.split()
        new = ""
        file.truncate()
        file.close()
        f_new = open(text,'w')
        for r in words:
            if r.isalpha() == True:
                if not r in stop_words:
                    r = lemm.lemmatize(r)
                    f_new.write(" "+r)
        f_new.close()


def make_Dictionary(train_dir):
    emails = [os.path.join(train_dir,f) for f in os.listdir(train_dir)]    
    all_words = []       
    for mail in emails:
        file = open(mail,'r+')
        line = file.read()
        words = line.split()
        all_words += words
        file.close()
    word_dict = Counter(all_words)
    for item in list(word_dict):
            if len(item) < 3:
                del word_dict[item]
    return word_dict.most_common(3000)

def extract_features(mail_dir):
    emails = [os.path.join(mail_dir,f) for f in os.listdir(mail_dir)]
    features_matrix = np.zeros((len(emails),3000))
    docID = 0;
    for mail in emails:
        file = open(mail,'r+')
        line = file.read()
        words = line.split()
        file.close()
        for word in words:
            wordID = 0
            for i,d in enumerate(dictionary):
                if d[0] == word:
                    wordID = i
                    features_matrix[docID,wordID] = words.count(word)
        docID = docID + 1
    return features_matrix
                    
train_dir = 'C:\\Users\\Aravo\\OneDrive\\Desktop\\FIS projecct\\ling-spam\\train-mails'
test_dir = 'C:\\Users\\Aravo\\OneDrive\\Desktop\\FIS projecct\\ling-spam\\test-mails'
dictionary = make_Dictionary(train_dir)
train_labels = np.zeros(702)
train_labels[351:701] = 1
train_matrix = extract_features(train_dir)
model = MultinomialNB()
model.fit(train_matrix,train_labels)
test_matrix = extract_features(test_dir)
test_labels = np.zeros(260)
test_labels[130:260] = 1
result = model.predict(test_matrix)
c1 = confusion_matrix(test_labels,result)
print("In the HAM mails our model detected\n")
print("Ham detected:",c1[0][0])
print("Spam detected:",c1[0][1])
print("\nIn the Spam mails our model detected\n")
print("Ham detected:",c1[1][0])
print("Spam detected:",c1[1][1])
