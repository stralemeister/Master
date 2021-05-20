import pandas as pd
import string
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import pickle


#Ucitavanje spam.csv i podela na trening i test podatke
df = pd.read_csv("spam.csv")

x = df["EmailText"]
y = df["Label"]

x_train,y_train = x[0:4457],y[0:4457]
x_test,y_test = x[4457:],y[4457:]



#Feature engineering - brojanje reci
count_vector = CountVectorizer()
training_data = count_vector.fit_transform(x_train)



#Treniranje modela uz pomoc Naive-Bayes algoritma 
naive_bayes = MultinomialNB()
naive_bayes.fit(training_data, y_train)

print(naive_bayes)

#Testiranje modela
test_data = count_vector.transform(x_test)
predictions = naive_bayes.predict(test_data)



#dodaj deo za poredjenje, da vidis procenat tacnosti



#Snimanje modela i vectorizer-a
#pickle.dump(naive_bayes, open('nb_model', 'wb'))
#pickle.dump(count_vector, open('count_vector', "wb"))


"""
#Funkcija za predvidjanje; kada se model bude ucitavao u drugu
#skriptu, ona ce se pozivati
def predictions(email):
    x = [email]
    data = count_vector.transform(x)
    pitanje = naive_bayes.predict(data)
    print(pitanje)
"""

"""
#Primer mejla koji se proverava
email2 = "Hello, how are you?"
predictions(email2)
"""
