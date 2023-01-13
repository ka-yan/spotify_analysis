"""
Name: Kalyan Khatiwada
Project 10
CS152 B
Date:2022/12/12

This python file main.py uses tkinter and features.py to run a GUI window which allows you to choose the feature that you want to plot and graph and the filename
that you want to use for the analysis and visualization. The file must be in the folder and the full name of the file must be inserted.

To run the file in macOS:
    Terminal: python3 main.py
in windows:
    Command Prompt: python main.py

"""

from tkinter import *
from tkinter import ttk
import features


class Window():
    """Class for the GUI window"""
    def __init__(self):
        #initialize the window
        self.window = Tk()
        self.window.title("Plotting Spotify History")
        self.window.protocol('WM_DELETE_WINDOW', quit)
        self.window.geometry("800x600")
        self.window['highlightbackground'] = "black"
        self.first_page()
        self.window.mainloop()


    def first_page(self):
        """This is the first page of the GUI which is shown when the file is ran."""
        self.intro_text = Label(self.window, text="Welcome to plotting spotify history! If you are sure that you have the files in your folder, please click ready!",
                        font=("Arial", 16))
        self.intro_text.grid(row=0, column=0)
        self.ready = ttk.Frame(self.window, padding = 60)
        self.ready.grid()
        ttk.Button(self.ready, text="Ready!", command = self.readyClicked).grid(row=0, column=1)

    def readyClicked(self):
        """This is the method for when the "Ready" buttom is clicked which leads to the second page"""
        self.ready.grid_remove()
        self.intro_text.grid_remove()
        self.second_page()

    def second_page(self):
        """This is the second page of the GUI which allows you to choose from the features list."""
        self.second_text1 = Label(self.window, text="Which feature of the songs would you like to have visualized? Features that you can choose are:",
                        font=("Arial", 16))
        self.second_text1.grid(row=0, column=0)
        self.feature = ttk.Frame(self.window, padding = 20)
        self.feature.grid()
        ttk.Button(self.feature, text="danceability", command = self.danceabilityclicked).grid(row=0, column=0)
        ttk.Button(self.feature, text="energy", command = self.energyclicked).grid(row=0, column=1)
        ttk.Button(self.feature, text="valence", command = self.valenceclicked).grid(row=0, column=2)
        ttk.Button(self.feature, text="loudness", command = self.loudnessclicked).grid(row=1, column=0)
        ttk.Button(self.feature, text="speechiness", command = self.speechinessclicked).grid(row=1, column=1)
        ttk.Button(self.feature, text="acousticness", command = self.acousticnessclicked).grid(row=1, column=2)
        ttk.Button(self.feature, text="instrumentalness", command = self.instrumentalnessclicked).grid(row=2, column=1)
    
    def danceabilityclicked(self):
        """This is the method for when the button danceability is clicked."""
        self.second_text1.grid_remove()
        self.feature.grid_remove()
        self.second_pageextra(feature="danceability")
    
    def energyclicked(self):
        """This is the method for when the button energy is clicked."""
        self.second_text1.grid_remove()
        self.feature.grid_remove()
        self.second_pageextra(feature= "energy")
    
    def valenceclicked(self):
        """This is the method for when the button valence is clicked."""
        self.second_text1.grid_remove()
        self.feature.grid_remove()
        self.second_pageextra(feature = "valence")
    
    def loudnessclicked(self):
        """This is the method for when the button loudness is clicked."""
        self.second_text1.grid_remove()
        self.feature.grid_remove()
        self.second_pageextra(feature="loudness")
    
    def speechinessclicked(self):
        """This is the method for when the button speechiness is clicked."""
        self.second_text1.grid_remove()
        self.feature.grid_remove()
        self.second_pageextra(feature="speechiness")

    def acousticnessclicked(self):
        """This is the method for when the button acousticness is clicked."""
        self.second_text1.grid_remove()
        self.feature.grid_remove()
        self.second_pageextra(feature="acousticness")
    
    def instrumentalnessclicked(self):
        """This is the method for when the button instrumentalness is clicked."""
        self.second_text1.grid_remove()
        self.feature.grid_remove()
        self.second_pageextra(feature="instrumentalness")
    
    def second_pageextra(self, feature):
        """Thism method is another page which runs when a button for a feature is clicked. This allows you to choose whether you want the mean to mapped or the features of the top 50 songs."""
        self.second_text1 = Label(self.window, text="Do you want the mean of your chosen feature to be mapped over time or do you want the features of top 50 songs of a certain time to be mapped?",
                        font=("Arial", 16))
        self.second_text1.grid(row=0, column=0)
        self.options = ttk.Frame(self.window, padding = 20)
        self.options.grid()
        self.featureVar = feature
        ttk.Button(self.options, text="Mean mapped over time", command = self.meanClicked).grid(row=1, column=0)
        ttk.Button(self.options, text="Features of top 50 songs", command = self.featuresClicked).grid(row=1, column=1)
    
    def meanClicked(self):
        """this method is for when the mean option is clicked."""
        features.plot_mean(self.featureVar)
        self.fourth_page(option123="mean")


    def featuresClicked(self):
        """this is for when the other option to plot the features values of 50 songs is clicked."""
        self.options.grid_remove()
        self.second_text1.grid_remove()
        self.opt = Label(self.window, text="Please insert the file that you want to be analyzed!")
        self.opt.grid(row=8, column=0)
        self.file= Label(self.window, text="File Name").place(x=50, y = 90)
        self.ageVar1= StringVar()
        self.entry= Entry(self.window, textvariable=self.ageVar1).place(x=150, y=90)
        self.submitdata = ttk.Frame(self.window, padding = 20)
        self.submitdata.grid()
        Button(self.submitdata, text="Submit!", command = self.plot).grid(row=1, column=1)
    
    def plot(self):
        """This is to plot the features and when featuresclicked is clicked."""
        features.plot_features(self.ageVar1.get(), self.featureVar)
        self.fourth_page(option123="features")
    
    def fourth_page(self, option123):
        """this is the fourth page where you get to choose whether you want to end the program or restart it again."""
        self.second_text1.grid_remove()
        self.options.grid_remove()
        if option123=="features":
            self.submitdata.grid_remove()
            self.opt.grid_remove()
        self.final = ttk.Frame(self.window, padding= 80 )
        self.final.grid(row=0, column=3)
        self.restar = ttk.Frame(self.window, padding = 100)
        self.restar.grid(row=1, column=2)
        ttk.Button(self.restar, text="Restart", command = self.restart).grid(row=1, column=1)
        self.end = ttk.Frame(self.window, padding = 100)
        self.end.grid(row=2, column=2)
        ttk.Button(self.end, text="Ends", command = self.close).grid(row=1, column=1)
    def close(self):
        """This method closes the window."""
        self.window.destroy()
    
    def restart(self):
        """this method closes the window and restarts it again."""
        self.window.destroy()
        Window()
Window()