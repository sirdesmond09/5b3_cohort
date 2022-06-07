class Question():
    num_of_questions = 0
    num_of_correct = 0
    
    
    def __init__(self,  question:str, ans:bool):
        self.question = question
        self.ans = ans
        
        Question.num_of_questions +=1  
        
        
    def take_ans(self):
        print("Expected answers should be Y or Yes or No or N\n")
        while True:
            ans = input(self.question +"\n>")
            if ans.lower() == "y" or ans.lower() == "yes":
                return True
            elif ans.lower() == "no" or ans.lower() == "n":
                return False 
            
    def __check_ans(self, ans):
        if ans == self.ans:
            Question.num_of_correct+=1
        
    def ask(self):
        self.__check_ans(self.take_ans())
        
    @classmethod
    def result(cls):
        return f"You got {Question.num_of_correct} out of {Question.num_of_questions}"


questions = [Question("Python was founded in 1998", False),
            Question("Ronaldo is a terrific player?", True),
            Question("Messi has 10 Ballon d'or", False),
            Question("Django is a python framework", True),
            Question("Julia is used for datascience", True)]

for q in questions:
    q.ask()
    
    
print(Question.result())