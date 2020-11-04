'''
Python Script to turn pdf text into an audio (audio book)
Requirements: 
1. pdf with text
2. pip install pyttsx3 
3. pip install pyPDF2

====HOw TO USE====

Enter pdf file path-name
Enter in starting page
Run Code
'''

import pyttsx3
import pyPDF2


BOOK_FILE_NAME = ''
STARTING_PAGE = ''


book = open(BOOK_FILE_NAME, 'rb')

pdfReader = pyPDF2.pdfFileReader
num_pages = pdfReader.numPages

for num in range(STARTING_PAGE, num_pages + 1):
    curr_page = pdfReader.getPage(num)
    text = curr_page.extractText()

    speaker = pyttsx3.init()
    speaker.say(text)
    speaker.runAndWait()
    print("Finished Page ", num)
