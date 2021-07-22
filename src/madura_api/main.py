import requests
from bs4 import BeautifulSoup
import sqlite3

from requests.api import get

def load_words():
    with open('words.txt', 'r') as word_file:
        valid_words=set(word_file.read().split())
    return valid_words

def translate(word:str)->list:
    translate_response=requests.get(f'https://www.maduraonline.com/?find={word}').text
    translate_soup=BeautifulSoup(translate_response, 'lxml') # send requsts response to beautiful soup

    #Check if there are valid results instead of suggestions
    if (translate_soup.body.findAll(text='Did you mean?')):
        return False
    else:
        table_data=[]
        table=translate_soup.table
        rows = table.find_all('tr')
        for row in rows:
            columns=row.find_all('td')
            columns=[element.text.strip() for element in columns]
            table_data.append([element for element in columns if element])

        # Make a new list while removing empty two lists at the begining ant the end
        table_data=[item for item in table_data if item!=[]]

        return table_data

class Translate:
    def __init__(self, word:str):
        self.word=word

        translate_response=requests.get(f'https://www.maduraonline.com/?find={self.word}').text
        self.translate_soup=BeautifulSoup(translate_response, 'lxml') # send requsts response to beautiful soup

    @property
    def list(self):
        table_data=[]
        table=self.translate_soup.table
        rows = table.find_all('tr')
        for row in rows:
            columns=row.find_all('td')
            columns=[element.text.strip() for element in columns]
            table_data.append([element for element in columns if element])

        # Make a new list while removing empty two lists at the begining ant the end
        table_data=[item for item in table_data if item!=[]]

        # make the list a flat list if it's a suggestion
        if(len(self.translate_soup.body.findAll(text='Did you mean?'))):
            flat_table_data=[item for sublist in table_data for item in sublist]
            return flat_table_data
        else:
            return table_data

    @property
    def is_a_suggestion(self):
        if(len(self.translate_soup.body.findAll(text='Did you mean?'))):
            return True
        else:
            return False

def write(word:str):
    with open('text.txt', 'w') as file:
        for i in translate(word):
            for j in i:
                file.write(j)
            file.write('\n')

def save(word_set:set):
    connection=sqlite3.connect('dictionary.db')
    c=connection.cursor()
    c.execute('''CREATE TABLE english_words(word TEXT UNIQUE, type TEXT)''')
    for word in word_set:
        c.execute('''INSERT INTO english_words(word) VALUES(:word)''', {'word':word})

    c.execute('''SELECT * FROM english_words''')
    print(c.fetchall())
    connection.commit()
    connection.close()

if __name__=='__main__':
    english_words = load_words()
   
    result=Translate('meen')
    print(result.list)

    print(result.is_a_suggestion)


