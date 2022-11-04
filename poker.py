import random

#建立一個card_face串列，用來放所有牌面的花色，以下總共52個項目（每個花色各13個）
card_face = ["Diamond"]*13 + ["Spade"]*13 + ["Heart"] * 13 + ["Club"] * 13
#建立一個card_value串列，用來放所有牌面的點數，以下總共52個項目（每個花色各13個值，分別是1~13）
card_value = [i for i in range(1, 14)] * 4
#把前面兩個串列組合成一個串列deck，用來放所有的撲克牌內容（依照順序放），內容分別是('Diamond', 1), ('Diamond', 2), ..., ('Club', 13)
deck = [item for item in zip(card_face, card_value)]
#把deck串列中的牌順序打亂
random.shuffle(deck)
#建立一個用來存放玩家手上的牌的串列player_cards
player_cards = list()
#把deck串列中的最後1張牌pop出來，放到player_cards串列中
player_cards.append(deck.pop())
print("Your cards:", player_cards)
answer = input("請問你要補牌嗎？")
while answer != "n" and answer != "N":
    #在這裡面寫把牌加到player_cards串列中的程式
    #同時也要判斷，如果在補完牌之後，玩加的分數爆了，就要立即中斷程式
    pass
#以下要寫，當玩家決定不加牌或是牌分數爆掉之後，要印出玩家的分數，以及他得到的牌
#並詢問玩家是否要再玩一次。

