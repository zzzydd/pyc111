# 21點作業框架程式
import random

#建立一個card_face串列，用來放所有牌面的花色，以下總共52個項目（每個花色各13個）
card_face = ["Diamond"]*13 + ["Spade"]*13 + ["Heart"] * 13 + ["Club"] * 13
#建立一個card_value串列，用來放所有牌面的點數，以下總共52個項目（每個花色各13個值，分別是1~13）
card_value = [i for i in range(1, 14)] * 4
#把前面兩個串列組合成一個串列deck，用來放所有的撲克牌內容（依照順序放），內容分別是('Diamond', 1), ('Diamond', 2), ..., ('Club', 13)
deck = [item for item in zip(card_face, card_value)]
#把deck串列中的牌順序打亂
random.shuffle(deck)
#建立一個用來存放所有玩家手上的牌的串列player_cards
player_cards = list()
num_players = int(input("請問這次要建立幾個玩家？"))

for i in range(num_players):
    player = list()
    #在這邊為每個人發3張牌，然後放到player_cards中
    player.append(deck.pop())
    player.append(deck.pop())
    player.append(deck.pop())
    player_cards.append(player)

def score(player):
    points = 0
    for card in player:
        if card[1]>10:
            points += 0.5
        else:
            points += card[1]
    for card in player:
        if card[1]==1 and points<=10:
            points += 10
    return points

winner, winner_points = 1, 0
print("---------------------------------")
for i, player in enumerate(player_cards,1):
    #以下要依序計算並顯示每一個玩家的點數
    if score(player)>winner_points and score(player)<=21:
        winner, winner_points = i, score(player)
    if score(player)<=21:
        print("Player #{}'s points is {}".format(i, score(player)))
    else:
        print("Player #{}'s points is bust!")
    print(player)
    print("---------------------------------")
print("Winner is {}, winner's points is {}".format(winner, winner_points))

