# DorkDetective
## Ready for use Google Dorks at your fingertips

This code works with placeholders inside a list. It searches a JSON file for all Google dorks that match the input placeholders. It then returns the matching Google dorks with the placeholders filled in, so the dorks can be copied and pasted. The program also includes German explanations for each Dork, which are stored in the JSON file. Dork Detective only returns results where one or any combination of the input placeholders match. It does not display dorks where any of the input placeholders are missing. Despite having under 50 lines of code excluding comments, the Python code is compact yet easy to read.

Adding more placeholders to the list in Python makes this program more versatile. Any new placeholders will automatically add input fields to the GUI, and the search algorithm will include them in its matching.


## Image of the GUI  <br>

![Image of the GUI](https://i.ibb.co/r07Drry/Dork1.png) <br>  

## Copy&Pastable results with explanations  <br>

![Copy&Pastable results with explanations](https://i.ibb.co/X460TJg/Dork4.png) <br>

## The list to add more placeholders**  <br>

![The list to add more placeholders](https://i.ibb.co/vVkjkQw/Dork2.png) <br>

## The JSON strucutre <br> 

![The JSON strucutre](https://i.ibb.co/Bn5V81k/Dork3.png) <br>


The code currently uses German comments and variable names, but an English version is coming soon.

At this early stage, the use cases are limited, but the code has huge potential. With the use of automation (either coded or with tools like Zapier or Make), web scraping (e.g. from the Google Hacking Database), and more, it could become a versatile Google dorks tool. That would make advanced Google searches accessible to anyone.

## Detailed Documentation

### import statements bring in the modules needed:
**tkinter** for building the GUI
**ttkbootstrap** for styled tkinter widgets
**pandas** for reading the JSON file of dork templates

**App class** contains the main application logic
__init__ method:
Sets up the main window - title, icon, etc.
Loads dork template data from a JSON file into a Pandas DataFrame
Defines a list of placeholder strings used in the templates
Creates a tkinter StringVar for each placeholder to store user input
Creates input fields, buttons, text box, etc needed for the GUI
**suche_befehle method**:
Clears previous results
Gets input values for placeholders
Loops through dork templates
Checks if all placeholders are filled for a template
Substitutes placeholders with input values
Inserts customized dork and explanation into results text box
Main window is created and the App class is instantiated

## Background <br>

I created Dork Detective during my studies in Cyber Security Management at Hochschule Niederrhein University in Germany. I developed it for a hackathon course project.


