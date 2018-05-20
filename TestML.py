import nltk
nltk.download('names')
from nltk.corpus import names
print (names.words() [:10])
print (len(names.words()))

from nltk.stem.porter import PorterStemmer
porter_stemmer=PorterStemmer()

porter_stemmer.stem('machines')
porter_stemmer.stem('learning')

nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
lemmatizer.lemmatize('machines')
lemmatizer.lemmatize('learning')
from sklearn.datasets import fetch_20newsgroups

groups = fetch_20newsgroups()
print (groups.keys())
print (groups['target_names'])
print (groups.target)