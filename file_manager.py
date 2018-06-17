import os
import Tkinter as tk
from Tkinter import *
import shutil
import pyglet
import Tkinter, Tkconstants, tkFileDialog


class File_Manager:
    
    def __init__(self,number_of_folders_to_be_made):
        self.number_of_folders_to_be_made=number_of_folders_to_be_made
    
    def folder_name_and_extension(self):
        self.temp=[]
        self.folder_details={}
        self.name=[]
        self.extension=[]
        for i in range(0,(self.number_of_folders_to_be_made)):
            self.temp=[]
            self.temp=raw_input(" example  audio mp3 name of the folder and the extensio without . ").split(" ")
            self.name.append(self.temp[0])
            self.extension.append(self.temp[1])


    
    def sort(self):
        directory = tkFileDialog.askdirectory()
        os.chdir(directory)
        current_directory = os.getcwd()
        for i in range(0,len(self.name)):
            a=str(self.name[i])
            b=str(self.extension[i])
            self.end_name = "final_directory_"+"a"
            self.end_name = os.path.join(current_directory,str(self.name[i]))
            if not os.path.exists(self.end_name):
                os.makedirs(self.end_name)
        for self.files in os.listdir(directory):
            if self.files.endswith(b):
                shutil.move(self.files,self.end_name)

