#	Takes user input, then outputs and stores hash of input
#		Created by:   Nicholas P. Wilde
#		Date created: 20180330
#
#	So I started writing this with someone specific in mind.
#	Sometime between starting it and now, I've forgotten what
#	that was. Here is the script anyways.

#Imports hash library I need, asks for user input of data to be
#hashed, sets input variable
import hashlib
print ("Phrase to hash: ")
to_be_hashed = input()

#Writes the user input to a txt file
meme = open('hashlog.txt','a')
meme.write('\n' + to_be_hashed) 
meme.close()

#Disgests the input into a sha512 hash and tells the user the hash
digest = hashlib.sha512((to_be_hashed).encode('utf-8')).hexdigest()
print ("Your hash is " + digest)

#Writes the hash below the input
maymay = open('hashlog.txt','a')
maymay.write('\n' + digest) 
maymay.close()
