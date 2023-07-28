import os
import codecs
import nltk
from nltk import word_tokenize
nltk.download('punkt')


#Dictionary for documents
def read_documents():
    f = open("chapter3/cisi/CISI.ALL")
    merged = ""
#Results of merging the field identifier with its content.

#Modifying the format for a better representation of the articles in the dataset.
    for a_line in f.readlines():
        #Return all lines in the file, as a list where each line is an item in the list object.
        if a_line.startswith("."):
            merged += "\n" + a_line.strip()
        else:
            merged += " " + a_line.strip()

    documents = {}

    content = ""
    doc_id = ""

    for a_line in merged.split("\n"):
        #Getting the articles id if written next to I.
        if a_line.startswith(".I"):
            doc_id = a_line.split(" ")[1].strip()
        #Getting the article's content accordance with the article's id
        elif a_line.startswith(".X"):
            documents[doc_id] = content
            content = ""
            doc_id = ""
        else:
            content += a_line.strip()[3:] + " "
    f.close()
    return documents

#Dictionary for queries
def read_queries():
    f = open("chapter3/cisi/CISI.QRY")
    merged = ""

    for a_line in f.readlines():
        if a_line.startswith("."):
            merged += "\n" + a_line.strip()
        else:
            merged += " " + a_line.strip()

    queries = {}

    content = ""
    qry_id = ""

    for a_line in merged.split("\n"):
        if a_line.startswith(".I"):
            if not content == "":
                queries[qry_id] = content
                content = ""
                qry_id = ""
            qry_id = a_line.split(" ")[1].strip()
        elif a_line.startswith(".W") or a_line.startswith(".T"):
            content += a_line.strip()[3:] + " "
    queries[qry_id] = content
    
    f.close()
    return queries

#Dictionary for mappings
#Which queries correspond to which documents.
def read_mappings():
    f = open("chapter3/cisi/CISI.REL")

    mappings = {}

    for a_line in f.readlines():
        voc = a_line.strip().split()
        key = voc[0].strip()
        current_value = voc[1].strip()
        value = []
        if key in mappings.keys():
            value = mappings.get(key)
            value.append(current_value)
            mappings[key] = value

    f.close
    return mappings

#Checking the size and the content
# documents = read_documents()
# print(len(documents))
# print(documents.get("1"))

#Preprocessing the data in documents and queries
def get_words(text):
    word_list = [word for word in word_tokenize(text.lower())]
    return word_list

documents = read_documents()
queries = read_queries()

doc_words = {}
qry_words = {}
for doc_id in documents.keys():
    doc_words[doc_id] = get_words(documents.get(doc_id))
for qry_id in queries.keys():
    qry_words[qry_id] = get_words(queries.get(qry_id))

# print(len(doc_words))
# print(doc_words.get("1"))
# print(len(doc_words.get("1")))
# print(len(qry_words))
# print(qry_words.get("1"))
# print(len(qry_words.get("1")))


#Simple boolean search algorithm
def retrieve_documents(doc_words, query):
    docs = []
    for doc_id in doc_words.keys():
        found = False
        i = 0
        while i < len(query) and not found:
            word = query[i]
            if word in doc_words.get(doc_id):
                docs.append(doc_id)
                found = True
            else:
                i +=1
    return docs


