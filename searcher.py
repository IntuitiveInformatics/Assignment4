from collections import defaultdict
import json, re
from nltk.stem import PorterStemmer

# Get User Input
# Tokenize Input
# If exists in Master Dict
# Then display results by doing:stepping into the dictionary and
# find the token class pertaining to the input token
# go to tokenclass.doc_and_freq and use this as dict


def tokenize(text):
    stemmer = PorterStemmer()                       # This is the stemmer
    words = (re.sub('[\W_]', ' ', text).lower())    # This gets rid of any non-alphanumerics
    token_list = words.split()                      # This splits the words at any white-space
    wordlist = defaultdict(int)                     # Creating a defaultDictionary
    num_words = 0
    for token in token_list:                        # For every token in the query
        stemmed = stemmer.stem(token)               # Stem it
        wordlist[stemmed] += 1                      # add it to the defaultDictionary
        num_words += 1
    return num_words, wordlist

    """
    words = (re.sub('[\W_]', ' ', text).lower())
    token_list = words.split()
    wordlist = {}
    for token in token_list:
        if token not in wordlist:
            wordlist[token] = 0
        wordlist[token] += 1
    #order(wordlist)
    return wordlist
    """

with open("tokens.json", "r") as a:
    wordList = json.load(a)     # Open the Json
    print(len(wordList))        # Print how many unique words there are in the dictionary
    with open("WEBPAGES_RAW/bookkeeping.json", "r") as urls:# Open the Bookeeping file(Not needed anymore since we have it in the Json)
        doc_list = json.load(urls)                          # Load the Bookeeping file into the memory (Not needed)
        variable = input("Search for something!: ")         # How we are going to be getting the query until we write a GUI
        query_length, words = tokenize(variable)            # This counts the query length and holds the words that were tokenized/stemmed
        print(words)                                        # This prints the query list
        for word in words.keys():                           # For every word in the query
            word_object = wordList[word]                    # Grab the TokenInfo for the word
            print(word_object)                              # Print the TokenInfo class
            documents = word_object["doc_and_freq"]         # Grab the docs that contain the word
            num = 0                                         # Keep track of how many you have looked through
            for k, v in sorted(documents.items(), key=lambda x: -x[1]): # Search that shit
                if num > 9:                                             # Stop after 10 results
                    break
                webpage_url = doc_list[k]                   # Find the URL (Won't be needed since we can just ask for the value associated with the DocID as the key
                print(str(v) + "\t" + k + "\t" +  webpage_url)  # Print that shit
                num += 1                                    # Increment






