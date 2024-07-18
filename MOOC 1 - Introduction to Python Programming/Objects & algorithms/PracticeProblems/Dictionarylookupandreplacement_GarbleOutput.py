#Write a function called garble_this. This function should
#take two parameters, both strings. The first string is the
#filename of a file to which to write (output_file), and the
#second string is the filename of a file from which to read
#(input_file).
#
#garble_this should copy the contents of input_file into
#output_file, but make the following changes:
#
# - Replace all vowels with the next vowel in order (a -> e,
#   e -> i, i -> o, o -> u.
# - Replace all consonants with the next consonant, b -> c,
#   c -> d, d -> f, etc.) Replace z with b.
# - Leave everything else in the file unchanged.
#
#For example, if these were the contents of input_file (the
#second parameter):
#
# this is some text. woo text yay!
#
#Then garble_this would write this text to output_file (the
#first parameter):
#
# vjot ot tuni viyv. xuu viyv zez!
#
#No other characters should be changed. Note that the file
#to be copied will have multiple lines of text. You may assume
#the input file will be all lower-case.
#
#We've included two files for you to test on: anInputFile.txt
#and anOutputFile.txt. The test code below will copy the text
#from the first file to the second. Feel free to modify the
#first to test different setups.
#
#Hints: 
# - Remember, you can increment a letter by 1 by finding its
#   ordinal, adding one, and converting it back to a letter.
#   If a_char is a character, then chr(ord(a_char) + 1) would
#   give you the next character.
# - You might also use dictionaries to establish what each
#   letter gets replaced by.
# - In ASCII, the character that comes after "z" is "{". You
#   want to replace "z" with "a", though.
# - Consider writing multiple functions! You could (but you
#   do not have to) write a dedicated function called
#   change_letter that handles a single letter, then
#   repeatedly call it to handle the file as a whole.


#Write your function here!
def garble_this(outputfile, inputfile):
    
    # read from inputfile
    try:
        filereader = open(inputfile, "r")
        filecontent = filereader.read()
    except:
        return "Error reading file"
    finally:
        filereader.close()
    print(filecontent)
    print("---------output---------")
   

    # Make modifications
    vowels = {"a": "e", "e": "i", "i": "o", "o": "u", "u": "a"}
    consonants = {"b": "c","c": "d","d": "f","f": "g","g": "h","h": "j","j": "k","k": "l","l": "m","m": "n","n": "p","p": "q", "q": "r","r": "s","s": "t","t": "v","v": "w","w": "x","x": "y", "y": "z","z": "b",}
    new_line = ""
    for char in filecontent:
        if char in vowels:
           new_line += vowels[char]
        elif char in consonants:
            new_line += consonants[char]
        else:
            new_line += char
    print(new_line)    
    # Send to outputfile
    try:
        filewriter = open(outputfile, "w")
        filewriter.write(str(new_line))
    except:
        return "Error writing to file"
    finally:
        filewriter.close()
    
#The code below will test your function. You can find the two
#files it references in the drop-down in the top left. If your
#code works, anOutputFile.txt should have the text:
#ecdfigh
#joklmnp
#uqrstva
#wxyzb.!
#1234567
#890&$%#

garble_this("anOutputFile.txt", "anInputFile.txt")
print("Done running! Check anOutputFile.txt for the result.")

