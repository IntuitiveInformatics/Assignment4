# send each file into beautiful soup to parse the html
# get bunch of words from html code
# tokenize words
# create list of unique words 
# create inverted index with words and documents they pertain to
# index will have the words as keys and the values are a list of doc numbers

#  * * * TF-IDF * * * 
# TF = # times a word occurs in a document divided by total # words in doc
# Inverse Document Frequency (IDF) = 
# log ( # of docs divided by number of docs where word occurs)
# TF(t) = (Number of times term t appears in a document) / 
# (Total number of terms in the document).
# IDF(t) = log_e(Total # of documents / # of documents with term t in it).


# * * * Files * * *
# 0 - 74 numbered folders
# each folder has 0 - 499 numbered files
# except folder 74 has 0 - 496
# 37,000 files in folders 0 - 73 plus 
# 497 files in folder 74, total of 37,497 documents

# * * * Dictionary * * * 
# Will contain the string (token) as the key
# The value will contain a token class

# * * * Token Class * * * 
# Has variables: Total Freq, Dict with Key of Doc# and value is #occurances inside, IDF value
# Doc IDs are of 00/000 format, first two digits are folder number, followed by doc number in each folder
import math


class TokenInfo:
   
    def __init__(self):
        self.doc_and_freq = {}  # {'Doc_ID': TF(t),}
        self.IDF = 0
        self.num_docs = 0
        self.url = {}           # {'Doc_ID': 'url',}

    def add_doc(self, doc_id, freq_of_word, total_words, url):
        if doc_id in self.doc_and_freq:         # If the doc_id is already in the array
            print('Error doc id already exists')# Print this
        else:
            self.doc_and_freq[doc_id] = float(freq_of_word)/total_words # tf = frequency of words/total words in doc
            self.url[doc_id] = url              # Link the URL to the document ID

    def generate_IDF(self):
        self.IDF = math.log10(37497 / (1 + float(self.num_docs)))   # How we generate IDF

    def update_num_docs(self):
        self.num_docs = len(self.doc_and_freq)                      # Updating the number of docs they are in

    def to_string(self):
        for doc, tf in self.doc_and_freq.items():   # This is how we are turning each object into a json
            self.update_num_docs()                  # Make sure the num_docs are updated
            self.generate_IDF()                     # Generate the IDF for each word
            tf_idf = round(tf * self.IDF, 4)        # Turn it into TF-IDF
            self.doc_and_freq[doc] = tf_idf         # Replace TF with TF-IDF
        #The code below is how we turn the object into a json
        return {"doc_and_freq": self.doc_and_freq, "num_docs": str(self.num_docs), "doc_and_url": self.url}

# Creating a short test for the code above
def test():
    apple = TokenInfo()
    apple.add_doc("0/100", 200, 10002, "http://nltk.com")
    apple.add_doc("0/203", 2104, 10300, "http://applesauce.com")
    apple.update_num_docs()
    apple.generate_IDF()
    print(apple.to_string())
