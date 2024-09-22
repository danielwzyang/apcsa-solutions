# this file is used to convert the .txt files from the ./solutions folder into .html files in the ./pages folder
# it does this using a template of an html file and adding the text from the .txt file into the .html file
# this also updates the list of links tp use for the homepage

# imports a python module that allows us to read the file system
import os

# imports a python module that allows us to edit json files
import json

# lists all the files in the directory ./solutions
files = os.listdir("./solutions")
# i have a directory on my local inside of the solutions directory called new
# this stores the problems whose due date hasn't passed yet
# im filtering out the directory so i'm only left with the old problems
files = [file for file in files if file !="new"]

# opens a template of an html file that i made since we're using it later when we make the new .html files
with open("./template.html", "r") as file:
    template = file.read()

# im using this to store a list of names to dump into a json file
names = []

# i'm using this to store links for the homepage
elements = ""

# goes through every file in the ./src directory
for path in files:
    # opens the txt file by going to its location
    with open("./solutions/" + path, "r") as file:
        # reads the file and saves the text
        # strip() just removes empty spaces in the beginning and the end
        code = file.read().strip()

        # gets the name of the file and removes the .txt ending so it becomes just the name
        # ex: Test.txt -> Test
        name = path.replace(".txt", "")
        
        # adding the name to our list
        names.append(name)

        '''
        # adds the link to the homepage list
        elements += f'<a class="w-fit text-base px-3 py-1 border rounded-xl hover:bg-[#2b2b33]" href="pages/{name}.html">{name}</a>'
        '''

        # now we're going to use the template file and insert our code
        content = template
        content = content.replace("[title]", name)
        content = content.replace("[code]", code)

        # creates a new html file in the ./pages directory with our new name
        # if the file already exists it will just open it
        with open("./pages/" + name + ".html", "w+") as newFile:
            # puts the content into the file
            newFile.write(content)

# dumps the list of names into a json file that i'm using in the homepage
with open("./solutions.json", "w") as file:
    json.dump(names, file)