class Question:
	"""docstring for Question"""
	def __init__(self, context, choices, answer):
		self.context = context
		self.choices = choices
		self.answer = answer
	def checkAnswer(self, answer):
		return self.answer == answer


class Quiz:
	"""docstring for Quiz"""
	def __init__(self, questions):
		self.questions = questions
		self.score = 0
		self.questionIndex = 0

	def getQuestion(self):
		return self.questions[self.questionIndex]

	def displayQuestion(self):
		question = self.getQuestion()
		print("Soru ",self.questionIndex+1,": ",question.context)

		for c in question.choices:
			print("-" + c)
		answer = input("Cevabiniz nedir?: ")
		self.quess(answer)
		self.loadQuestion()

	def quess(self,answer):
		question = self.getQuestion()

		if(question.checkAnswer(answer)):
			self.score += 1
		self.questionIndex += 1
		

	def loadQuestion(self):
		if len(self.questions) == self.questionIndex:
			self.showScore()
		else:
			self.displayProgress()
			self.displayQuestion()

	def  showScore(self):
		print("Skorunuz: ",self.score)

	def displayProgress(self):
		totalQuestions = len(self.questions)
		questionNumber = self.questionIndex +1

		if questionNumber > totalQuestions:
			print("Quiz bitti.")
		else:
			print("Toplam ",totalQuestions," sorudan ",questionNumber,". soru")

	'''def getQuestion(self):                                                
		for i in range(0,len(questions)):
			print("Soru",i+1,":",questions[i].context)
			for c in questions[i].choices:
				print("-" + c)
			answer = input("Cevabiniz nedir?: ")
			if(questions[i].checkAnswer(answer)):
				self.score += 1'''



q1 = Question("Bu programin yazildigi programlama dili hangisidir?", ["C","Python","C#","Java"],"Python")
q2 = Question("En populer programlama dili hangisidir?", ["C","Python","C#","Java"],"Java")
q3 = Question("Verilen programlama dillerinden gelistirilme tarihi en eski olan hangisidir?", ["C","Python","C#","Java"],"C")
questions = [q1, q2, q3]

quiz = Quiz(questions)
quiz.loadQuestion()

#print("Skorunuz: ",quiz.score)
