'''Module about spam filtering'''
import os
import codecs
import random
import nltk
from nltk import word_tokenize
from nltk import NaiveBayesClassifier, classify
from nltk.text import Text
nltk.download('punkt')


def read_in(path_to_folder:str, base_path:str = "chapter2/enron1") -> list:
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

all_emails = [(email_content, "spam") for email_content in spam_lst]
all_emails += [(email_content, "ham") for email_content in ham_lst]

# all_emails = []
# for email_content in spam_lst:
#     all_emails.append((email_content, "spam"))

random.seed(42)
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
    # word_list = word_tokenize(text.lower())
    # print(word_list2)
    for word in word_list:
        features[word] = True
    return features
#get_features("hi how are you today?")

all_features = [(get_features(email), label) 
                for email, label in all_emails]

#print(get_features("hi how are you?"))
# print(len(all_features))
# print(len(all_features[0][0]))
# print(len(all_features[99][0]))

def train(features, proportion):
    train_size = int(len(features) * proportion)
    train_set = features[:train_size]
    test_set = features[train_size:]
    print(f"Training set size = {str(len(train_set))} emails ")
    print(f"Test set size = {str(len(test_set))} emails ")

    classifier = NaiveBayesClassifier.train(train_set)
    return train_set, test_set, classifier

train_set, test_set, classifier = train(all_features, 0.8)

def evaluate(train_set, test_set, classifier):
    print(f"Accuracy on the training set = {str(classify.accuracy(classifier, train_set))}")
    print(f"Accuracy on the test set = {str(classify.accuracy(classifier, test_set))}")
    classifier.show_most_informative_features(50)

evaluate(train_set, test_set, classifier)

# def concordance (data_list, search_word):
#     for email in data_list:
#         word_list = [word for word in word_tokenize(email.lower())]
#         text_list = Text(word_list)
#         if search_word in word_list:
#             text_list.concordance(search_word)

##################Deploying the spam filter
test_spam_list = ["Claim your gift", "Click here to have an appointment"]
test_ham_list = ["Looking forward too.", "Here is your receipt"]

test_emails = [(email_content, "spam") for email_content in test_spam_list]
test_emails += [(email_content, "ham") for email_content in test_ham_list]

new_test_set = [(get_features(email), label) for (email, label) in test_emails]
evaluate(train_set, new_test_set, classifier)
