from collections import defaultdict
import re, sys, time, json, nltk
from bs4 import BeautifulSoup
from tester import TokenInfo
from nltk.stem import PorterStemmer

def tokenize(text, stemmer):
    words = (re.sub('[\W_]', ' ', text).lower())    # Get rid of the non-alphanumeric and uppercases
    token_list = words.split()                      # Split the words based on a " " regex
    wordlist = defaultdict(int)                     # Create a defaultDictionary for the words
    for token in token_list:                        # Token by token
        stemmed = stemmer.stem(token)               # stem the word
        wordlist[stemmed] += 1                      # add it to the defaultDictionary if not there and inc. if there
    return len(token_list), wordlist                # Return the wordlist and how many tokens were in the text


def get_text(temp_file):
    with open(temp_file, "r") as file:
        text = ""
        base = BeautifulSoup(file, "lxml")
        title = ""
        if base.title is not None:
            try:
                title = base.title.contents[0]
            except IndexError:
                title = ""
        tags = []
        # Grab all tags separately to be able to modify the weight of them
        tags.append(base.find_all('a'))
        tags.append(base.find_all('p'))
        tags.append(base.find_all('b'))
        tags.append(base.find_all('i'))
        tags.append(base.find_all('h1'))
        tags.append(base.find_all('h2'))
        tags.append(base.find_all('h3'))
        tags.append(base.find_all('h4'))
        tags.append(base.find_all('h5'))
        tags.append(base.find_all('h6'))
        text += " " + title + " "

        # Go through each list of tags for each tag type
        for list in tags:
            # For every tag in the list of tags
            for tag in list:
                # If the tag has text
                if tag.string is not None:
                    # Add the text to the total string
                    text += " " + tag.string + " "

    file.close()
    return text

def run_parser():
    stemmer = PorterStemmer()       # Have a stemmer open, that way the object only has to be created once
    with open("tokens.json", "r+") as token_list:   # Open the token list
        search_dictionary = json.load(token_list)   # Load the json
        with open("WEBPAGES_RAW/bookkeeping.json", "r") as a:   # Open the bookkeeping json
            addresses = json.load(a)                # Load the json
            number = 0                              # Start a counter to keep track of how many docs we parsed
            for k in addresses.keys():              # Go through all of the
                print("now parsing document: " + k) # Print what document it's on
                print(str(number) + " Out of " + str(37497))    # Visualize the progess of the parser
                page = get_text("WEBPAGES_RAW/" + k)    # Go to the document in the WEBPAGES_RAW folder

                length, tokens = tokenize(page, stemmer)    # Get the length of the dictionary from each doc and the doc

                for key, value in tokens.items():           # For every word that was in the parsed document
                    if key not in search_dictionary:        # If the token is not in the current dictionary
                        search_dictionary[key] = TokenInfo()# Add the token to the dictionary
                    search_dictionary[key].add_doc(k, value, length, addresses[k]) # Add the document to the list of doc
                number += 1                         # Increment the number of docs that have been searched
            for key, token_info in search_dictionary.items():   # After done parsing, turn the token_info class into a json
                search_dictionary[key] = token_info.to_string() # replace the tokenInfo class with the json for each
        a.close()
        token_list.close()

        with open("tokens.json", "w") as final_list:    # Open the tokens.json
            json.dump(search_dictionary, final_list)    # Write the finished dictionary to the file
        final_list.close()


run_parser()
