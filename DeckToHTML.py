#Decklist to HTML
cards = open("inDeck.txt","r")
deck = open("outDeck.txt", "w")
for card in cards:
	if card.find('--')!=-1:
		deck.write("<p><b><button onclick=\"hide()\">" + card[2:].strip() + "</button></b> Deck is cool</p>\n")
		deck.write("<script>\n")
		deck.write("function hide() {\n")
		deck.write("var x = document.getElementById(\"" + card[2:].strip() + "\");\n")
		deck.write("  if (x.style.display === \"none\") {\n")
		deck.write("    x.style.display = \"block\";\n")
		deck.write("  } else {\n")
		deck.write("    x.style.display = \"none\";\n")
		deck.write("  }")
		deck.write("}\n")
		deck.write("</script>\n")
		deck.write("<ul id=\"" + card[2:].strip() + "\" style=\"list-style-type: none; display: none\">\n")
	elif card.find('(')!=-1:
		deck.write("<li><h4>" + card.strip() + "</h4></li>\n") 
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