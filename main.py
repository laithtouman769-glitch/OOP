class TreasureChest:
    def __init__(self,question,answer,points):
        self._answer2 = None
        self._question = question #String
        self._answer = answer #Integer
        self._points = points #Integer

    def getQuestion(self):
        return self._question

    def checkAnswer(self,answer2):
        self._answer2 = answer2
        if self._answer2 == self._answer:
            return True
        else:
            return False
    def getPoints(self,no_attempts):
        return self._points

