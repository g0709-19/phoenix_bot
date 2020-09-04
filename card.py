import time, random
import keyboard

class Setting:
    CARDS = [
        '여행', '음식', '파티', '배달', '사진',
        '고양이', '코로나', '범죄', '친구', '국방부',
        '기록', '과제', '게임', '유튜브', '모임',
        '집', '카페', '동물', '일정', '일기'
    ]
    MAX_CHOOSE = 3
    WAIT_SECOND = 1

class CardManager:
    def setCards(self, format):
        Setting.CARDS = format.split(',')

    def addCard(self, text):
        Setting.CARDS.append(text)

    def delCard(self, index):
        del Setting.CARDS[index]

    def getCards(self):
        return Setting.CARDS
        # for card in Setting.CARDS:
        #     print(f'[{Setting.CARDS.index(card)}] {card}')
        # print('')

# manager = CardManager()
# manager.showCards()
# manager.addCard('안')
# manager.addCard('녕')
# manager.showCards()
# manager.delCard(0)
# manager.showCards()

class Card:
    def countDeleted(self):
        count = 0
        for card in self.cards:
            if card == None:
                count += 1
        return count

    def addChooseCount(self):
        self.choose_count += 1

    def canChoose(self):
        return self.choose_count < Setting.MAX_CHOOSE

    def isAlreadyChoosed(self, index):
        return self.cards[index] == None

    def deleteCard(self, index):
        self.cards[index] = None

    def printCard(self, index):
        return f'`{self.cards[index]}` 를 뽑았습니다!'

    def shuffleCard(self):
        random.shuffle(self.cards)
        time.sleep(Setting.WAIT_SECOND)
        return '카드를 섞었습니다!'

    def play(self, choose):
        choose -= 1
        
        if choose > len(self.cards) or len(self.cards) < 0:
            return f'1 이상 {len(self.cards)} 이하 숫자를 입력해주세요!'
        if self.isAlreadyChoosed(choose):
            return '이미 뽑은 카드입니다!'
        else:
            message = self.printCard(choose)
            self.deleteCard(choose)
            self.addChooseCount()
            return message

    def __init__(self):
        self.cards = Setting.CARDS.copy()
        self.choose_count = 0
        print('카드 생성')

# card = Card()
# card.shuffleCard()
# while card.canChoose():
#     if keyboard.is_pressed('q'):
#         card.play()