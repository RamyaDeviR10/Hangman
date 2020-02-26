import random

class Hangman():
	def __init__(self):
		self.words=['time','person','year','wage','daylight','things','manly','world','life','hangover','program','morning','python','government','company','problem','woman','dream','vanished','notify']
		self.word=list(self.words[random.randint(0,len(self.words)-1)])		
		self.word_index={}
		self.result=['_']*len(self.word)
		self.hangman=7
		self.count=len(self.word)

	def chooseword(self):
		print(self.word)
		for index,char in enumerate(self.word):
			if char in self.word_index:
				self.word_index[char].append(index)
			else:
				self.word_index[char]=[index]		
		print(*self.result,end=" ")
		print()

	
	def playgame(self):
		input_set=set()
		while(self.count !=0 and self.hangman!=0):
			print()
			print("Input a letter:",end=" ")
			val=input().lower()
			if val in input_set:
				print('You have already entered the character')

			elif val in self.word_index:
				for ind in self.word_index[val]:
					self.result[ind]=self.word[ind]
					self.count-=1
			else:
				self.hangman-=1

			print(*self.result,end=" ")
			print()			
			input_set.add(val)
		return self.count

	

def main():
	game=Hangman()
	word= game.chooseword()
	res=game.playgame()
	if res==0:
		print("Survived")
	else:
		print("Hanged")


if __name__ == '__main__':
	main()