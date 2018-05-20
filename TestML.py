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

import numpy as np
print (np.unique(groups.target))
print (groups.data[0])
print (groups.target[0])
print ( groups.target_names[groups.target[0]])
print (len(groups.data[0]))
print (len(groups.data[1]))

import seaborn as sns
sns.distplot(groups.target)
import matplotlib.pyplot as plt
plt.show()

from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_20newsgroups
cv = CountVectorizer(stop_words="english", max_features=500)
groups = fetch_20newsgroups()
transformed = cv.fit_transform(groups.data)
print(cv.get_feature_names())
sns.distplot(np.log(transformed.toarray().sum(axis=0)))
plt.xlabel('Log Count')
plt.ylabel('Frequency')
plt.title('Distribution Plot of 500 Word Counts')
plt.show()



from sklearn.feature_extraction.text import CountVectorizer
from sklearn.datasets import fetch_20newsgroups
from nltk.corpus import names
from nltk.stem import WordNetLemmatizer
def letters_only(astr):
    return astr.isalpha()
cv = CountVectorizer(stop_words="english", max_features=500)
groups = fetch_20newsgroups()
cleaned = []
all_names = set(names.words())
lemmatizer = WordNetLemmatizer()
for post in groups.data:
    cleaned.append(' '.join([lemmatizer.lemmatize(word.lower()
    for word in post.split()
    if letters_only(word)
    and word not in all_names)]))

transformed = cv.fit_transform(cleaned)
print(cv.get_feature_names())

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.datasets import fetch_20newsgroups
from nltk.corpus import names
from nltk.stem import WordNetLemmatizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
def letters_only(astr):
    return astr.isalpha()
cv = CountVectorizer(stop_words="english", max_features=500)
groups = fetch_20newsgroups()
cleaned = []
all_names = set(names.words())
lemmatizer = WordNetLemmatizer()
for post in groups.data:
    cleaned.append(' '.join([lemmatizer.lemmatize(word.lower()) for word in post.split() if letters_only(word) and word not in all_names]))
transformed = cv.fit_transform(cleaned)
km = KMeans(n_clusters=20)
km.fit(transformed)
labels = groups.target
plt.scatter(labels, km.labels_)
plt.xlabel('Newsgroup')
plt.ylabel('Cluster')
plt.show()

