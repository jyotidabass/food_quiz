import csv

class User:
    def __init__(self, name, age, year_group):
        self.name = name
        self.age = age
        self.year_group = year_group

    def createAccount(self):
        self.username = self.name[:3] + self.age
        print("Your username:", self.username)
        self.userPass = input("Enter your password: ")
        
    def saveInfo(self):
        with open("info.txt", "r") as file:
            fileReader = csv.reader(file)
            fileInfo = [info for info in fileReader if info != []]
            fileInfo.append([self.username, self.userPass, self.name,
                             self.age, self.year_group])
            print(fileInfo)

        with open("info.txt", "w") as file:
            fileWriter = csv.writer(file)
            for item in fileInfo:
                fileWriter.writerow(item)
    
    def startQuiz(self):
        try:
            userDifficulty = int(input("Pick a difficulty:\n1.Easy\n2.Medium\n3.Hard\nSay: "))
        except:
            userDifficulty = 3
            
        userSubject = input("Pick a subject:\n1. Maths\n2. Computer Science\nSay: ")
        if userSubject == "1":
            userSubject = "Maths"
        else:
            userSubject = "Computer Science"

        quiz = Quiz(userDifficulty, userSubject, self.username)
        quiz.start(), quiz.checkAnswers()

    def createReport(self):

        userReport = input("Pick report:\n1. By username\n2. By highest\n3. By average\nSay: ")
        file = open("scores.txt", "r")
        scoresReader = csv.reader(file)

        for line in scoresReader:
            print(line)
        
        if userReport == "1":

            username = input("Enter the username: ")

            print("%-15s%-15s%-15s%-15s"
                  %("Username", "Subject", "Difficulty", "Grade"))
            
            for line in scoresReader:
                if username in line:
                    print("%-15s%-15s%-15s%-15s"
                          %(line[0], line[1], line[2], line[3]))

        elif userReport == "2":
            highestScore = 0

            for lines in scoresReader:
                print(lines)
                if "Computer Science" in lines:                    
                    if int(lines[2]) > highestScore:
                        highestCSScore = lines[2]
                        studentCSInfo = lines
                else:
                    print("Lines[2]:", lines)
                    if int(lines[2]) > highestScore:
                        highestMathsScore = lines[2]
                        studentMathsInfo = lines

            print("Computer Science:", studentCSInfo), print("Maths:", studentMathsInfo)

class Quiz:
    userAnswers = []
    def __init__(self, difficulty, subject, username):
        self.difficulty = difficulty
        self.subject = subject
        self.fileName = "quiz{}".format(self.difficulty)
        self.username = username
        
    def start(self):
        answers = []
        with open("{}.txt".format(self.fileName), "r") as f:
            quizReader = csv.reader(f)
            for line in quizReader:
                if "{}".format(self.subject) in line:
                    for line in quizReader:
                        
                        if "end {}_quiz".format(self.subject) in line:
                            break
                        if "[end question]" in line:
                            userAnswer = input("Enter an answer: ")
                            self.userAnswers.append([userAnswer.lower()])
                        
                        print(*line)
                        
    def checkAnswers(self):
        score = 0
        answers = []

        with open("{}.txt".format(self.fileName), "r") as f:
            quizReader = csv.reader(f)
            for line in quizReader:
                if "{}_answers".format(self.subject) in line:
                    for line in quizReader:
                        if "end {}_answers".format(self.subject) in line:
                            break
                        answers.append(line)
                        
        for index in range(len(answers)):
            try:
                if answers[index] == self.userAnswers[index]:
                    score += 1
            except:
                continue
                
        self.calcGrade(score)

    def calcGrade(self, score):
        self.percentage = score*100/5
        gradeTable = [50, 60, 70, 80, 90]
        print("You got {}/5".format(score))
        print("You got {}%".format(self.percentage))

        for element in gradeTable:
            done = False
            if self.percentage < element:
                grade = int(element/10)
                print("Your grade: {}".format(element/10))
                done = True
            if done:
                break
        try:
            print(grade)
        except:
            print("Aha")
            
        self.submitScore(grade)

    def submitScore(self, grade):
        with open("scores.txt", "r") as f:
            scoresReader = csv.reader(f)
            scores = [line for line in scoresReader if line != []]

        scores.append([self.username, self.subject, self.difficulty, grade])

        with open("scores.txt", "w") as f:
            scoresWriter = csv.writer(f)
            for info in scores:
                scoresWriter.writerow(info)

def fileClear(file):
    with open("{}.txt".format(file), "w") as f:
        clear = csv.writer(f)
        clear.writerow([])

def main():
    user = User(input("Enter your name: "), input("Enter your age: "),
                input("Enter your year group: "))
    user.createAccount(), user.saveInfo()
    user.startQuiz()

    while True: user.createReport()

    

main()
