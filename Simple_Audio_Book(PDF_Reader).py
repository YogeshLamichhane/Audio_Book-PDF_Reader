#  Simple_Audio_Book(PDF_Reader).py
#  
#  Copyright 2020 Yogesh Lamichhane <yogeshlmc3@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

import pyttsx3
import PyPDF2

engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', 'english+f8') #Use f3 in place of f8 for female voice 
''' You can use 
engine.setProperty('voice', voices[1].id)
in place of 
engine.setProperty('voice', 'english+f8')
and change the voice id number in voices[ ].id for different language.
All the supported languages are listed in bottom.
*Note the pdf and voice language should be same.
'''
rate = engine.getProperty('rate')
engine.setProperty('rate', 120) # Sets speed percent     # Can be more than 100

volume = engine.getProperty('volume')
engine.setProperty('volume', 0.8) # Set volume 0-1

yourpdf = open('/home/yogesh/Documents/aa.pdf', 'rb') #Give path to your pdf file and open in readable binary form
pdfReader = PyPDF2.PdfFileReader(yourpdf) #import your pdf file
pages = pdfReader.numPages #get total number of pages in your pdf
print("Total number of pages is: ")
print(pages)
print("Enter page number to start reading from: ")
userpage = int (input())
if userpage < 1:
    print("Invalid Page Number!")

elif userpage > pages:
    print("Invalid Page Number! Page number exceeded!")

else:
    x = userpage - 1 #Since page is counted from 0 in python 1 is subtracted to make same page number as the use inputs 
    for num in range(x, pages):
        page = pdfReader.getPage(num)
        text = page.extractText()
        engine.say(text)
        engine.runAndWait()
