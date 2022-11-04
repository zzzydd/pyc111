import random

card_face = ["Diamond"]*13 + ["Spade"]*13 + ["Heart"] * 13 + ["Club"] * 13
card_value = [i for i in range(1, 14)] * 4
deck = [item for item in zip(card_face, card_value)]
random.shuffle(deck)
player_cards = list()
player_cards.append(deck.pop())
print("Your cards:", player_cards)
answer = input("請問你要補牌嗎？")
while answer != "n" and answer != "N":
    #在這裡面寫把牌加到player_cards串列中的程式
    #同時也要判斷，如果在補完牌之後，玩加的分數爆了，就要立即中斷程式
    pass
#以下要寫，當玩家決定不加牌或是牌分數爆掉之後，要印出玩家的分數，以及他得到的牌
#並詢問玩家是否要再玩一次。

