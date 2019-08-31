#Decklist to HTML
cards = open("inDeck.txt","r")
deck = open("outDeck.txt", "w")
for card in cards:
	if card.find('--')!=-1:
		deck.write("<h3>" + card[2:].strip() + "</h3>\n")
		deck.write("<ul style=\"list-style-type: none;\">\n")
	else:
		deck.write("<li>" + card.strip() + "</li>\n") 
deck.write("</ul>")
cards.close()
deck.close()



"""

file = open("textfile.txt", "w") 
 
file.write("Hello World\n") 
file.write("This is our new text file\n") 
file.write("and this is another line.\n") 
file.write("Why? Because we can.") 
 
file.close() 

file1 = open("textfile.txt", "r")
for line in file1:
	print(line.strip())
"""