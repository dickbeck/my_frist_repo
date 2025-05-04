import webbrowser
import time

urls = [
"https://www.scientificamerican.com/",
"https://www.newscientist.com/",
"https://www.sciencenews.org/",
"https://www.discovermagazine.com/",
"https://www.smithsonianmag.com/science-nature/",
"https://www.bbc.com/future/science-and-technology",
"https://www.nationalgeographic.com/science/",
"https://cosmosmagazine.com/",
"https://physicsworld.com/",
"https://www.americanscientist.org/",
"https://skyandtelescope.org/",
"https://astronomy.com/",
"https://www.quantamagazine.org/",
"https://www.science.org/", # Science Magazine (AAAS)
"https://www.nature.com/", # Nature Magazine
"https://www.pnas.org/" # PNAS
"https://www.google.com",
"https://en.wikipedia.org/wiki/Spallation_Neutron_Source",
"https://www.github.com",
"https://www.python.org",
"https://www.learn-html.org/",
"https://docs.pyscript.net/2025.2.4/"
]

# Display URLs with index numbers
print("Select a URL to open:\n")
print()  # This prints a blank line
for i, url in enumerate(urls):
    print(f"{i+1}. {url}")


while True:
    print()  # This prints a blank line
# Get user input
    choice =  input("Enter a URL list number or type exit to quit: ") 
    if choice.lower() == "exit":  # Allow the user to quit
        print("Exiting program.")
        break 
    try:
        number = int(choice)   #convert choice to an integer
        #Since the url list starts at 0,
        #the value of numbar must be reduced by 1
        number-=1 #this could have been written:number = number - 1
        # Validate choice and open the selected URL
        if 0 <= number < len(urls):
            webbrowser.open(urls[number])
            print()  # This prints a blank line

            print("The link has been opened in your default web browser.")
            break # Exit the loop if valid
        else:
            print()  # This prints a blank line

            print("Invalid choice is not on the list. Please try again.")
           
    except ValueError:
        print("Invalid entry! Please enter a numeric value.")
    
