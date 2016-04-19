with open(business_restaurants_path) as business_restaurants_file:
    #store the reviews for a particular user-id in a new file named as lex file.
  lex file = select review from reviews where id = "P_alyVIY9y_7XuyM5ZjPnQ"

    #Remove Numbers
    s = '12abcd405'
    result = ''.join([i for i in s if not i.isdigit()])
    result
    'abcd'

    #Remove Punctuation
    import re
    from string import punctuation
    a = "string. With. Punctuation"
    def test_repl(s):  # From S.Lott's solution
        for c in string.punctuation:
            s=s.replace(c,"")
        return s

    test_repl(a)


    def clean_lexicon(lex_input):
    lex_file_l=open(lex_input, "r", encoding = "utf8").readlines()
    
    new_lex_file_l=[]
    for i in lex_file_l:
        i=i.strip()
        #i= i[:-1] # i is a word in the list
        i= re.sub("_", " ", i)
        new_lex_file_l.append(i)
    return new_lex_file_l


    #Remove Stopwords
    from nltk.corpus import stopwords

    cachedStopWords = stopwords.words("english")
    def testFuncNew():
        text = 'hello bye the the hi'
        text = ' '.join([word for word in text.split() if word not in cachedStopWords])
    if __name__ == "__main__":
        for i in xrange(10000):
            testFuncNew()

    
    #Stemmer
    import nltk
    from nltk.stem import PorterStemmer
    stemmer = PorterStemmer()
    stemmer.stem('string')
    
