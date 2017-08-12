import gensim

# Load Google's pre-trained Word2Vec model.
model = gensim.models.KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin', binary=True, limit=200000) 

# "boy" is to "father" as "girl" is to ...?
model.most_similar(['girl', 'father'], ['boy'], topn=3)
[('mother', 0.61849487), ('wife', 0.57972813), ('daughter', 0.56296098)]
more_examples = ["he his she", "big bigger bad", "going went being"]
for example in more_examples:
    a, b, x = example.split()
    predicted = model.most_modsimilar([x, b], [a])[0][0]
    print("'%s' is to '%s' as '%s' is to '%s'" % (a, b, x, predicted))
#'he' is to 'his' as 'she' is to 'her'
#'big' is to 'bigger' as 'bad' is to 'worse'
#'going' is to 'went' as 'being' is to 'was'