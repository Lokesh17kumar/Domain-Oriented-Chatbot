""" College Model & Mail Model """

## MODULES
import tflearn
import tensorflow as tf
import pickle as pk
import warnings
import random as rand
import nltk as nlp
from nltk.stem.lancaster import LancasterStemmer
import json
import numpy as np

# ignore warnings
warnings.filterwarnings("ignore")

class CollegeModel(object):

    def __init__(self, *args, **kwargs):

        """ method to initialize the model """

        self.data = pk.load(open(r"C:\Users\LOKI99\Desktop\python_clg_ project\ChatBot_APP\Chatbot_development_phase\Chatbot_phase_3\pickle_file_1\training_data", "rb")) # load the pickle data

        self.words = self.data["words"] # list of words

        self.labels = self.data["classes"] # list of classes

        self.train_x = self.data["train_x"] # input data - words

        self.train_y = self.data["train_y"] # output data - labels

        # reading data from college json file
        with open(r'C:\Users\LOKI99\Desktop\python_clg_ project\ChatBot_APP\Chatbot_development_phase\Chatbot_phase_3\college_json_data_file\college_data.json') as json_data:

            self.intents = json.load(json_data)

        self.stemmer = LancasterStemmer() # stemming model

        self.thres_val = 0.25 # threshold value for classifying the sentence

        self.neural_network_model()


    def sentence_stem(self, sentence):

        """ method to tokenize the sentence and stem the words """

        sent_words = nlp.word_tokenize(sentence) # tokenize the sentence

        sent_words = [self.stemmer.stem(word.lower()) for word in sent_words] # stem tokenized words
            
        return sent_words


    def bag_of_words(self, sentence):

        """ method to return bag of words : 0 - other words (or) 1 - present word/word to be found """

        sent_words = self.sentence_stem(sentence) # stemmed words

        # bag of words
        bag = [0] * len(self.words)

        for s in sent_words : # loop through stemmed words

            for i,w in enumerate(self.words):

                if w == s : # if stemmed words & words are matched

                    bag[i] = 1

        return (np.array(bag))


    def neural_network_model(self):

        """ method to build the neural network model """

        # reset underlying graph data
        tf.reset_default_graph()
        
        # Build neural network
        net = tflearn.input_data(shape=[None, len(self.train_x[0])]) # input layer 

        net = tflearn.fully_connected(net, 8) # hidden layer - 1
        
        net = tflearn.fully_connected(net, 8) # hidden layer - 2
        
        net = tflearn.fully_connected(net, len(self.train_y[0]), activation='softmax') # output layer

        net = tflearn.regression(net) # regression based network
        
        # defining the model
        self.model = tflearn.DNN(net, tensorboard_dir="tflearn_logs")

        #load the machine learning model
        self.model.load(r"C:\Users\LOKI99\Desktop\python_clg_ project\ChatBot_APP\Chatbot_development_phase\Chatbot_phase_3\college_model_file\softmax_model\college_softmax_model.tflearn")

 
    def  classify(self, sentence):

        """ method to classify sentence with appropriate label """

        # generate probabilities from the model
        results = self.model.predict([self.bag_of_words(sentence)])[0]

        # filter out predictions below threshold value
        results = [[i,r] for i,r in enumerate(results) if r > self.thres_val]

        # sort by strength of probability
        results.sort(key = lambda x: x[1], reverse=True)

        ret_list = []

        for r in results:

            ret_list.append((self.labels[r[0]], r[1]))

        return ret_list # return tuple of intent & probability


    def  response(self, sentence):

        """ method to retrieve appropriate response to the query """

        results = self.classify(sentence) # classify sentence

        # if we have a classification, then find the matching intent tag/class
        if results:

            # loop as long as there are matches
            while results:

                for i in self.intents["intents"]:

                    # find a tag matching the 1st result
                    if i["tag"] == results[0][0]:

                        return rand.choice(i["responses"])

                results.pop(0)                    


class MailModel(object):


    def __init__(self, *args, **kwargs):
    
        """ method to initialize the model """
    
        self.data = pk.load(open(r"C:\Users\LOKI99\Desktop\python_clg_ project\ChatBot_APP\Chatbot_development_phase\Chatbot_phase_3\pickle_file_2\training_data", "rb")) # load the pickle data
    
        self.words = self.data["words"] # list of words
    
        self.labels = self.data["classes"] # list of classes
    
        self.train_x = self.data["train_x"] # input data - words
    
        self.train_y = self.data["train_y"] # output data - labels
    
        # reading data from college json file
        with open(r'C:\Users\LOKI99\Desktop\python_clg_ project\ChatBot_APP\Chatbot_development_phase\Chatbot_phase_3\mail_json_data_file\mail_intents.json') as json_data:
    
            self.intents = json.load(json_data)
    
        self.stemmer = LancasterStemmer() # stemming model
    
        self.thres_val = 0.25 # threshold value for classifying the sentence
    
        self.neural_network_model()
    
    
    def sentence_stem(self, sentence):

        """ method to tokenize the sentence and stem the words """

        sent_words = nlp.word_tokenize(sentence) # tokenize the sentence

        sent_words = [self.stemmer.stem(word.lower()) for word in sent_words] # stem tokenized words
            
        return sent_words


    def bag_of_words(self, sentence):

        """ method to return bag of words : 0 - other words (or) 1 - present word/word to be found """

        sent_words = self.sentence_stem(sentence) # stemmed words

        # bag of words
        bag = [0] * len(self.words)

        for s in sent_words : # loop through stemmed words

            for i,w in enumerate(self.words):

                if w == s : # if stemmed words & words are matched

                    bag[i] = 1

        return (np.array(bag))


    def neural_network_model(self):

        """ method to build the neural network model """

        # reset underlying graph data
        tf.reset_default_graph()
        
        # Build neural network
        net = tflearn.input_data(shape=[None, len(self.train_x[0])]) # input layer

        net = tflearn.fully_connected(net, 8) # hidden layer - 1
        
        net = tflearn.fully_connected(net, 8) # hidden layer - 2
        
        net = tflearn.fully_connected(net, len(self.train_y[0]), activation='softmax') # output layer

        net = tflearn.regression(net) # regression based model        
        
        # defining the model
        self.model = tflearn.DNN(net, tensorboard_dir="tflearn_logs")

        #load the machine learning model
        self.model.load(r"C:\Users\LOKI99\Desktop\python_clg_ project\ChatBot_APP\Chatbot_development_phase\Chatbot_phase_3\mail_model_file\softmax_model\mail_softmax_model.tflearn")


    def  classify(self, sentence):

        """ method to classify sentence with appropriate label """

        # generate probabilities from the model
        results = self.model.predict([self.bag_of_words(sentence)])[0]

        # filter out predictions below threshold value
        results = [[i,r] for i,r in enumerate(results) if r > self.thres_val]

        # sort by strength of probability
        results.sort(key = lambda x: x[1], reverse=True)

        ret_list = []

        for r in results:

            ret_list.append((self.labels[r[0]], r[1]))

        return ret_list # return tuple of intent & probability


    def response(self, sentence):

        """ method to retrieve appropriate response to the query """

        results = self.classify(sentence) # classify sentence

        # if we have a classification, then find the matching intent tag/class
        if results:

            # loop as long as there are matches
            while results:

                for i in self.intents["intents"]:

                    # find a tag matching the 1st result
                    if i["tag"] == results[0][0]:

                        return rand.choice(i["responses"])

                results.pop(0)          
