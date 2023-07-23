'''Module about spam filtering'''
import os
import codecs
import random
import nltk
from nltk import word_tokenize
nltk.download('punkt')


def read_in(path_to_folder:str, base_path:str = "enron1") -> list:
    full_path = base_path + "/" + path_to_folder
    print(f'This is the full path: {full_path}')
    files = os.listdir(full_path)
    a_list = []
    for a_file in files:
        if not a_file.startswith("."):
            f = codecs.open((full_path + a_file), mode ="r", encoding = "ISO-8859-1", errors="ignore")
            a_list.append(f.read())
            f.close()
    return a_list

spam_lst = read_in('spam/')
ham_lst = read_in('ham/')

all_emails = [(email_content, "spam", i) for i, email_content in enumerate(spam_lst)]
all_emails += [(email_content, "ham", j) for j, email_content in enumerate(ham_lst)]

# all_emails = []
# for email_content in spam_lst:
#     all_emails.append((email_content, "spam"))

random.seed(40)
random.shuffle(all_emails)

#checking the size of the dataset
# print (f"Dataset size = {str(len(all_emails))} emails")

# def tokenize(input):
#     word_list = []
#     for word in word_tokenize(input):
#         word_list.append(word)
#     return word_list

# # input = "hi how are you are you allright?"
# # print(tokenize(input))

def get_features(text):
    features = {}
    word_list = [word for word in word_tokenize(text.lower())]
    # print(word_list)
    # word_list2 = word_tokenize(text.lower())
    # print(word_list2)
    for word in word_list:
        features[word] = True
    return features
#get_features("hi how are you today?")

all_features = [(get_features(email), label) for (email, label) in all_emails]
   

