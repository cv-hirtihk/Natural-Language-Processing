# -*- coding: utf-8 -*-
"""
Created on 23-09-2021

@author: Hirtih Kumar C V
"""
import nltk

def read(filename):
    words = []
    for file in filename:
        with open(f'C:\\Users\\cvhir\\Documents\\GitHub\\Natural-Language-Processing\\stylometry-federalist\\data\\federalist_{file}.txt') as f:
            words.append(f.read())
    return ('\n'.join(words))

#Initial driver function
def main():
    #Author's name and index of the file; Index starts from '1'
    paper_files = {
                'Madison':[10, 14, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48],
                'Hamilton':[1, 6, 7, 8, 9, 11, 12, 13, 15, 16, 17, 21, 22, 23, 24, 
                            25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 59, 60,
                            61, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 
                            78, 79, 80, 81, 82, 83, 84, 85],
                'Jay':[2, 3, 4, 5],
                'Shared':[18, 19, 20],
                'Unknown':[49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 62, 63]
                }

    #Dictionary to extract author's name and to read the respective files for analyzing
    key_to_author_file = {}
    
    #List of author's name
    authors = ()
    temp_authors = list(authors)

    #key -> author's name
    #value -> array of numbers reffering to the file's index
    for key, value in paper_files.items():
        key_to_author_file[key] = read(value)
        temp_authors.append(key)
        authors = tuple(temp_authors)
    
    author_tokens = {}
    length_distribution = {}

    for author in authors:
        tokens = nltk.word_tokenize(key_to_author_file[author])

        #Filter only alphabets
        author_tokens[author] = ([token for token in tokens if any(al.isalpha() for al in token)])

        #Find the length of individual word
        token_length = [len(token) for token in author_tokens[author]]

        #Frequency denotes the number of times a word has occured
        length_distribution[authors] = nltk.FreqDist(token_length)

        length_distribution[authors].plot(15, title="Author writing comparision")
    
    
if __name__ == "__main__":
    main()