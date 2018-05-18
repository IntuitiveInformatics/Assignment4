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
# Doc IDs are of 00-000 format, first two digits are folder number, followed by doc number in each folder




