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
   
    def __inti__(self):
       self.doc_and_freq = {} # {'Doc_ID', TF(t)}
       self.IDF = 0
       self.num_docs = 0

    def add_doc(self, doc_id, freq_of_word, total_words):
        if doc_id in doc_and_freq:
            print('Error doc id already exists')
        else:
            doc_and_freq[doc_id] = freq_of_word/total_words

    def generate_IDF(self):
        self.IDF = math.log10(37497/num_docs)

    def update_num_docs(self):
        self.num_docs = len (doc_and_freq)



