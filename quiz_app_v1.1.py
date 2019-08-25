from tkinter import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
import json
from render import *
from utils import *


Login = LogginWindow()
Login.render()



'''
for quizzes in quiz['quiz']:
    print("{} Quiz".format(quizzes["Title"]))
    for questions in quizzes['questions']:
        print(questions['question'])
        print("1. {}\n2. {}\n3. {}".format(questions['answers'][0],
                                           questions['answers'][1],
                                           questions['answers'][2]))
        answer = int(input('1/2/3: ')) - 1
        if answer == questions['answer']:
            print('Correct')
        else:
            print('Wrong')

'''

        




