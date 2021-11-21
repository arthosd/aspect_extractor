import pandas as pd
from app.nlp.Parser import Parser

import json

class Handler :

    def __init__(self, file_path) :
        # File name
        self.__file_path = file_path
        # Read json file containing filepath
        self._reviews_df = pd.read_json(file_path, lines=True)
        # Will contain result of each parser
        self.__parsers = []

    def extract_aspect_from_reviews (self) :
        """
        Iterate thru all the dataframe.
        """
        reviews = self._reviews_df["reviewText"]

        for review in reviews :
            
            # Loading reviews to Parser
            parser = Parser (review)
            # Match reviwes with patterns
            parser.match()
            self.__parsers.append(parser)

    def export_all_aspect (self) :
        """
        get all the result of all parser and export it to json file
        """
        final_result = []

        for parser in self.__parsers :
            final_result.append(parser.get_result())

        son_format = json.dumps(final_result)
        
        with open(self.__file_path+".result.json","w") as file:
            file.write(son_format)
        
