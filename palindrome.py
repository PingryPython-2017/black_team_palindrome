def is_palindrome(word):
	''' Takes in an str, checks to see if palindrome, returns bool '''
	
	# Makes sure that the word/phrase is only lowercase
	word = word.lower()
	
	# Terminating cases are if there is no characters or one character in the word 		
	if len(word) == 0:
		return True
	if len(word) == 1:
		return True
		
	# Checks if the first character in the word is different than the last character is the world. If not, then that means the word is not a palindrome. 
	if word[0] != word[len(word) - 1]:
		return False
	
	# This means that the first character is equal to the last character.
	else:
		# Slices the word so that the first character and the last character is cut off. 
		word2 = word[1:-1]
		# Recurses with this new word.
		if is_palindrome(word2) == True:
			return True
		else:
			return False
			
