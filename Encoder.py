PDF = '\u202c' #Pop Directional Formatting
RLO = '\u202e' #Right-to-Left Override
LRO = '\u202d' #Left-to-Right Override

def splitText(string, spacing):
    splitString = list() #Create a list to hold the split string
    for pos, char in enumerate(string): 
        if pos % spacing == 0: #If it's the first character or a multiple of the spacing, start a new pair
            if pos > 0: #If it's not the first character
                splitString.append(pair) #Add the finished pair to the list
            pair = char #Start a new pair with the current character
        else:
            pair += char #Add the current character to the pair
    splitString.append(pair) #Add the last pair to the list
    return splitString

def encodeText(string, spacing=2):
    splitString = splitText(string, spacing) #Split the string into pairs
    out =  LRO #Start the output string with a left-to-right override character
    nextChar = RLO #First bidirectional override character is RLO
    for i in range(0,len(splitString)): #Loop through the split string. Variable i is not used, but is needed to loop through the correct number of times
        out += (splitString[0] + nextChar) #For each pair, add the pair and the next bidirectional override character to the output string
        #Toggle the next bidirectional override character.
        if nextChar == RLO:
            nextChar = LRO
        else:
            nextChar = RLO
        del splitString[0] #Remove the first pair from the list so that the next pair is at index 0
        splitString = [i[::-1] for i in splitString[::-1]] #Reverse the order of the remaining pairs and reverse the characters in each pair to maintain the correct order when the bidirectional override characters are applied
    return out + PDF #Add a final PDF to the end of the output string to ensure further text is not affected by the bidirectional override characters


def main():
    text = input('Enter text to encode:\n>>>')
    spacing_input = input('Enter spacing between dir overrides:\n>>>')
    
    spacing = int(spacing_input) 
    
    result = encodeText(text, spacing)
    print(result)
    try:
        import pyperclip
        copy_choice = input('Copy to clipboard? (y/n):\n>>>')
        if copy_choice.lower() == 'y':
            pyperclip.copy(result)
            print('Copied to clipboard!')
    except ImportError:
        print("pyperclip not installed. Install it to enable clipboard functionality.")

if __name__ == '__main__':
    main()
