#! /usr/bin/env python
import yaml

class Sentence:
    """new sentence object to parse the sentence in the document"""
    # initializer with instance attributes
    def __init__(self, sentence_string, document, line_number, character_length=None, word_length=None):
        self.sentence_string = sentence_string
        self.document = document
        self.line_number = line_number
        
    def __repr__(self):
        return f"Sentence(sentence_string={self.sentence_string}, document={self.document}, line_number={self.line_number}, character_length={self.character_length}, word_length={self.word_length})"
    
    def count_character(self):
        self.character_length = len(self.sentence_string)
        
    def count_words(self):
        self.word_length = len(self.sentence_string.split(" "))
        
    def read(self):
        print (f"sentence_string:{self.sentence_string}document: {self.document} \nline_number: {self.line_number} \ncharacter_length: {self.character_length} \nword_length: {self.word_length}")    
    
    def write(self, file):
        with open(file, 'a') as f:
            f.write("--- ")
            yaml.dump(self, f, sort_keys=False)
            f.write("\n")

def main():    
    for doc in range(995,1000):
        document = str(doc) +'.txtCleaned'
        filepath = "/Users/lucy/SC4S2/week9/cleaned_input/"
        with open(filepath+document, "r") as f:
            num = 0

            while True:
                num +=1
                line = f.readline()

                # if not an empty line
                if len(line.strip())==0:
                    break

                sen = Sentence(line, document, num)
                sen.count_character()
                sen.count_words()
                sen.write('output.yaml')       
    f.close()

if __name__ =="__main__":
    main()
