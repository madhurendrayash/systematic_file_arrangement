import os
import Tkinter as tk
from Tkinter import *
import shutil
import pyglet
from file_manager import File_Manager
import Tkinter, Tkconstants, tkFileDialog
root = Tk()
root.minsize(300,300)


number_of_folders=input("number_of_folders")


foo=File_Manager(number_of_folders)
foo.folder_name_and_extension()
foo.sort()
