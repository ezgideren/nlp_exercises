import os
import codecs

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
        if a_line.startswith(".I"):
            doc_id = a_line.split(" ")[1].strip()
        elif a_line.startswith(".X"):
            documents[doc_id] = content
            content = ""
            doc_id = ""
        else:
            content += a_line.strip()[3:] + " "

    f.close()
    return documents

documents = read_documents()
print(len(documents))
print(documents.get("1"))