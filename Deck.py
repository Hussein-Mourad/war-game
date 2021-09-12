import random


class Deck:
    cards = []
    player1Cards = []
    player2Cards = []

    def __init__(self):
        for i in range(1, 14):
            for j in range(4):
                self.cards.append(i)

        random.shuffle(self.cards)

        for i in range(26):
            self.player1Cards.append(self.cards.pop())
            self.player2Cards.append(self.cards.pop())

    def drawCard(self):
        if len(self.player1Cards) == 0:
            print("Player 2 wins")
            return True
        elif len(self.player2Cards) == 0:
            print("Player 1 wins")
            return True

        card1 = self.player1Cards.pop()
        card2 = self.player2Cards.pop()

        if card1 > card2:
            self.player1Cards.append(card1)
            self.player1Cards.append(card2)
        elif card2 > card1:
            self.player2Cards.append(card1)
            self.player2Cards.append(card2)
        else:
            return self.war()

    def war(self):
        if len(self.player1Cards) < 10:
            print("Player 2 wins")
            return True

        if len(self.player2Cards) < 10:
            print("Player 1 wins")
            return True

        if len(self.player1Cards) == 0:
            print("Player 2 wins")
            return True
        if len(self.player2Cards) == 0:
            print("Player 1 wins")
            return True

        cards1 = [self.player1Cards.pop() for i in range(10)]
        cards2 = [self.player2Cards.pop() for i in range(10)]

        if cards1[9] > cards2[9]:
            self.player1Cards += cards1
            self.player1Cards += cards2
        elif cards2[9] > cards1[9]:
            self.player2Cards += cards1
            self.player2Cards += cards2
        else:
            self.war()
