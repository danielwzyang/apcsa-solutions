# this file is used to convert the .txt files from the ./src folder into .html files in the ./pages folder
# it does this using a template of an html file and adding the text from the .txt file into the .html file
# this also updates the list of links in the homepage

# imports a python module that allows us to read the file system
import os

# lists all the files in the directory ./solutions
files = os.listdir("./solutions")

# opens a template of an html file that i made since we're using it later when we make the new .html files
with open("./template.html", "r") as file:
    template = file.read()

# i'm using this later on to add a list of all the links into the homepage
nameList = []

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

        # adds the name to the list
        nameList.append(name)

        # now we're going to use the template file and insert our code
        content = template
        content = content.replace("[title]", name)
        content = content.replace("[code]", code)

        # creates a new html file in the ./pages directory with our new name
        # if the file already exists it will just open it
        with open("./pages/" + name + ".html", "w+") as newFile:
            # puts the content into the file
            newFile.write(content)

# string to store all the <a> elements
elements = ""

# converts the names into <a> elements for html
for name in nameList:
    elements += f'<a class="w-fit text-base px-3 py-1 border rounded-xl hover:bg-[#2b2b33]" href="pages/{name}.html">{name}</a>'

# using a template again
with open("./indexTemplate.html", "r") as file:
    # inserting our list
    content = file.read()
    content = content.replace("[list]", elements)
    
    # writing the content
    with open("./index.html", "w") as file:
        file.write(content)

