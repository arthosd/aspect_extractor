from spacy.matcher import DependencyMatcher # Dependency matcher to build patterns
from spacy import load # To load docs

from app.nlp.pattern import init_patterns

class Parser :

    def __init__(self, review_text) :
        # Loading English language
        self.__nlp = load("en_core_web_sm") # loading english language analyzer
        # Tokenize review text
        self.__doc = self.__nlp(review_text)
        # Dependency matcher to math with pattern
        self.__dep_matcher = DependencyMatcher(vocab=self.__nlp.vocab)
        # Loading patterns to matcher
        init_patterns(dep_patcher=self.__dep_matcher)
        # Review
        self.__review = review_text

        # Dictionnary that will contain result
        self.__result = []

    def match (self) :
        """
        Match tokenized review with patterns to detect aspect.
        """
        matches = self.__dep_matcher(self.__doc)

        for match in matches :
            # Result of patterns filtering
            result = match[1]

            obj = dict()
            temp_list = []

            obj["review"] = self.__review

            for word in result :
                temp_list.append(self.__doc[word])

            obj["aspect"] = temp_list
            self.__result.append(obj)

    def get_result (self) :
        """
        Return a json object to be written in a file
        """
        return self.__result
