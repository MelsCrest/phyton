#EJERCICIO JUEGO PIEDRA, PAPEL, TIJERAS, LAGARTO, SPOCK

class Participant:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.choice = ""
    def choose(self):
        self.choice = input("{name}, elige piedra, papel, tijera, lagarto o Spock: ".format(name= self.name))
        print("{name} elige {choice}".format(name=self.name, choice = self.choice))
    def toNumericalChoice(self):
        switcher = {
            "piedra" : 0,
            "papel" : 1,
            "tijera" : 2,
            "lagarto" : 3,
            "Spock" : 4
        }
        return switcher[self.choice]
    def incrementPoint(self):
        self.points += 1

class GameRound:
    def __init__(self, p1, p2):
        self.rules = [
            [0, -1, 1, 1, -1],
            [1, 0, -1, -1, 1],
            [-1, 1, 0, 1, -1],
            [-1, 1, -1, 0, 1],
            [1, -1, 1, -1, 0]
        ]
        p1.choose()
        p2.choose()
        result = self.compareChoices(p1, p2)
        print(f"La ronda ha terminado en {result}")
        if result > 0:
            p1.incrementPoint()
        elif result < 0:
            p2.incrementPoint()
    def compareChoices(self, p1, p2):
        return self.rules[p1.toNumericalChoice()][p2.toNumericalChoice()]
        
    def awardPoints(self):
        print("implement")
    def getResultAsString(self, result):
        res = {
            0 : "empate",
            1 : "ganas",
            -1 : "pierdes"

        }
        return res[result]

class Game:
    def __init__(self):
        self.endGame = False
        self.participant = Participant("Paqui")
        self.secondParticipant = Participant("Loli")
    def start(self):
        while not self.endGame:
            GameRound(self.participant, self.secondParticipant)
            self.checkEndCondition()
        game_round = GameRound(self.participant, self.secondParticipant)
    def checkEndCondition(self):
        answer = input("Continuar juego y/n: ")
        if answer == 'y':
            GameRound(self.participant, self.secondParticipant)
            self.checkEndCondition()
        else:
            print("Juego finalizado, {p1name} tiene {p1points} puntos, y {p2name} tiene {p2points} puntos.".format(p1name = self.participant.name, p1points = self.participant.points, p2name = self.secondParticipant.name, p2points = self.secondParticipant.points))
            self.determineWinner()
            self.endGame = True
    def determineWinner(self):
        resultString = "Es un empate"
        if self.participant.points > self.secondParticipant.points:
            resultString = "El ganador es {name}".format(name = self.participant.name)
        elif self.participant.points < self.secondParticipant.points:
            resultString = "El ganador es {name}".format(name = self.secondParticipant.name)
        print(resultString)

game = Game()
game.start()