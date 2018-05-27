import math

#Tokenize two words entered
#Find results from both
#Create two dict with top 10 results from each
#Find if any Doc IDs intersect
#List docs with intersections first + high TF-IDFs
#If < 10 intersections found list first word results

class TokenInfo:
   
    def __init__(self):
       self.doc_and_freq = {} # {'Doc_ID', TF(t)}
       self.IDF = 0
       self.num_docs = 0

    def add_doc(self, doc_id, freq_of_word, total_words):
        if doc_id in self.doc_and_freq:
            print('Error doc id already exists')
        else:
            self.doc_and_freq[doc_id] = float(freq_of_word)/total_words
            self.update_num_docs()
            self.generate_IDF()

    def generate_IDF(self):
        self.IDF = math.log10(37497/float(self.num_docs))

    def update_num_docs(self):
        self.num_docs = len(self.doc_and_freq)

    def to_string(self):
        string_doc = "{"
        n = 0
        for doc, tf in self.doc_and_freq.items():
            if n != 0:
                string_doc += ", \"" + doc + "\": " + str(tf)
            else:
                string_doc += "\"" + doc + "\": " + str(tf)
            n += 1
        string_doc += "}"
        return {"doc_and_freq": self.doc_and_freq, "IDF": str(self.IDF), "num_docs": str(self.num_docs)}



one = TokenInfo() # First entered word
two = TokenInfo() # Second word entered
    
# Add some random shiet to them tokens, some in common some not
one.add_doc('1234',10,1000)
one.add_doc('12345',101,1000)
one.add_doc('12342',210,1000)
one.add_doc('12343',110,1000)
one.add_doc('12344',10,1000)
one.add_doc('12346',120,1000)
one.add_doc('12347',10,1000)
one.add_doc('12348',150,1000)
one.add_doc('12349',210,1000)
one.add_doc('12340',610,1000)
one.add_doc('01234',110,1000)

two.add_doc('1234',10,1000)
two.add_doc('123411',150,1000)
two.add_doc('12345',10,1000)
two.add_doc('12348',130,1000)
two.add_doc('12341',10,1000)
two.add_doc('12349',160,1000)
two.add_doc('12340',10,1000)
two.add_doc('12342',510,1000)
two.add_doc('12343',210,1000)
two.add_doc('12344',310,1000)
two.add_doc('12347',10,1000)
    
one.generate_IDF() # Generate the IDF shit
one.update_num_docs() # Count docs of the shit
two.generate_IDF() # Generate the IDF shit
two.update_num_docs() # Count docs of the shit
a_list = {} # create a list(dicked) to collect doc ids of top 10
counter = 0 # only need top ten of them shits, so this keeps track
for key,value in one.doc_and_freq.items(): # Run loop through 1st word entered to find intersections with 2nd word
    if(key in two.doc_and_freq): # Looking for intersections of two key words
        a_list[key] = value # If so then add it to the dicked list, might need to modify for URL copying shit
        counter += 1 # Pythons dumb ass way to increment a counter
    if(counter > 9): # If we got enough shit in dicked then we good niggah, bail
        break

if(counter < 9): # If somehow we didnt get enough in the dicked then grab rest from first key word
    for key,value in one.doc_and_freq.items(): # Find other relevant docs
        if(key not in a_list.keys()): # Make sure they already not in the dicked
            a_listed[key] = value # Add to dicked
            counter += 1 # Increment counter
        if(counter > 9): # If we already got a full dicked, bail
            break
        
    
for k, v in sorted(a_list.items(), key=lambda x: -x[1]): # Display them dicked items from best to worst
    print(str(v) + '\t' + k) 
        