from tkinter import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
import json
from render import *

class Quizzes():
    def __init__(self, quiz_title = None, quiz_category = None,
                 image_location = None, description = None, questions = None):
        self.quiz_title = quiz_title
        self.quiz_category = quiz_category
        self.image_location = image_location
        self.description = description
        self.questions = questions


class Json:
    '''
    All functions to manipulate
    json files (read/wirte)
    '''
    def __init__(self, location, content=None, json_context=None):
        self.content = content
        self.context = json_context
        self.dir = location

    def wirte_json(self):
        f = open(self.dir, 'r')
        
        json_content = json.load(f)

        json_content[self.context].append(self.content)

        with open(self.dir, 'w') as f:
            json.dump(json_content, f, indent=2)

    def read_json(self):
        f = open(self.dir, 'r')
        return json.load(f)



