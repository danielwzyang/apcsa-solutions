# this file is used to convert the .java files from the ./src folder into .html files in the ./solutions folder
# it does this using a template of an html file and adding the text from the .java file into the .html file

# imports a python module that allows us to read the file system
import os

# lists all the files in the directory ./src
files = os.listdir("./java")

# opens a template of an html file that i made since we're using it later when we make the new .html files
with open("./template.html", "r") as file:
    template = file.read()

# i'm using this later on to add a list of all the links into the homepage
nameList = []

# goes through every file in the ./src directory
for path in files:
    # opens the java file by going to its location
    with open("./java/" + path, "r") as file:
        # reads the file and saves the text
        # strip() just removes empty spaces in the beginning and the end
        code = file.read().strip()

        # gets the name of the file and removes the .java ending so it becomes just the name
        # ex: Test.java -> Test
        name = path.replace(".java", "")

        # adds the name to the list
        nameList.append(name)

        # now we're going to use the template file and insert our code
        content = template
        content = content.replace("[title]", name)
        content = content.replace("[code]", code)

        # creates a new html file in the ./solutions directory with our new name
        # if the file already exists it will just open it
        with open("./solutions/" + name + ".html", "w+") as newFile:
            # puts the content into the file
            newFile.write(content)

# string to store all the <li> elements
elements = ""

# converts the names into <li> elements for html
for name in nameList:
    elements += f'<li><a href="solutions/{name}.html">{name}</a></li>'

# using a template again
with open("./indexTemplate.html", "r") as file:
    # inserting our list
    content = file.read()
    content = content.replace("[list]", elements)
    
    # writing the content
    with open("./index.html", "w") as file:
        file.write(content)

