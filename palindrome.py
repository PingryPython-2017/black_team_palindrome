def is_palindrome(word):
	''' Takes in a phrase, checks to see if palindrome, returns bool '''
	
	if len(word) == 0:
		return True
	if len(word) == 1:
		return True
	if word[0] != word[len(word) - 1]:
		return False
	
	
	else:
		word2 = word[1:-1]
		if is_palindrome(word2) == True:
			return True
		else:
			return False
			
