#EJERCICIO JUEGO PIEDRA, PAPEL, TIJERAS
# "Piedra, papel, tijeras" es un juego con dos participantes. El juego consta de rondas. En cada ronda, un participante elige un símbolo entre piedra, papel o tijeras, y el otro participante hace lo mismo. Después, para determinar el ganador de la ronda, se comparan los símbolos elegidos. Las reglas del juego determinan que la piedra gana a las tijeras, las tijeras ganan al papel (lo cortan) y el papel gana a la piedra (la envuelve). Al ganador de la ronda se le concede un punto. El juego continúa durante tantas rondas como los participantes acuerden. El ganador es el participante con más puntos.

class Participant:
    def __init__(self):
        self.points = 0
        self.choice = ""

class Gameround:

class Game:
    def __init__(self):
        self.endGame = False
        self.participant = Participant()
        self.secondParticipant = Participant()
