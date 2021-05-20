import pickle


#Ucitavanje naucenog modela i vectorizer-a
loaded_model = pickle.load(open('nb_model', 'rb'))
loaded_vector = pickle.load(open('count_vector', 'rb'))


#Funkcija za predvidjanje
def predictions(body):
    check = [body]
    data = loaded_vector.transform(check)
    result = loaded_model.predict(data)
    return result
