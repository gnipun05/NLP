import nltk
# nltk.download()

tokens = nltk.word_tokenize("Can you pleaase buy me an Arizona Ice Tea? It's $0.99")

print ("Parts of Speech: ", nltk.pos_tag(tokens))