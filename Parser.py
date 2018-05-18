from collections import defaultdict
import re, sys, time


class MainClass:
    """
    A class to be able to read in a file or two, take out everything but spaces and letters, tokenize the input,
    analyze the tokens to find how often words come up, then compare what words the inputs have in common if two files
    are given
    """

    def __init__(self, inputString):
        self.unprocessedText = inputString
        self.text = ""

    def analyze(self):
        self.text = (re.sub('[\W_]', ' ', self.unprocessedText).lower())
        words = self.text.split()
        wordlist = defaultdict(int)
        for word in words:
            wordlist[word] += 1
        self.order(wordlist)

    def analyzeFile(self, fileName):
        myFile = open(fileName, 'r')
        text = myFile.read()
        analyzer.unprocessedText = text
        analyzer.text = ""
        self.text = (re.sub('[\W_]', ' ', self.unprocessedText).lower())
        words = self.text.split()
        wordlist = defaultdict(int)
        for word in words:
            wordlist[word] += 1
        self.order(wordlist)

    def order(self, defdict):
        ordered = []
        orderednumbers = []
        for k, v in sorted(defdict.items(), key=lambda x: (-x[1], x[0])):
            ordered.append(k)
            orderednumbers.append(v)
            print k + " - " + str(v)



def time_mod():
    startTime = time.time()
    filename = sys.argv[1]


filename = "mary.txt"
myFile = open(filename, 'r')
text = myFile.read()
analyzer = MainClass(text)
analyzer.analyze()
analyzer.analyzeFile("hack.txt")
analyzer.analyzeFile("sample1.txt")
myFile.close()
