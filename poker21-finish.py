import random

card_face = ["Diamond"]*13 + ["Spade"]*13 + ["Heart"] * 13 + ["Club"] * 13
card_value = [i for i in range(1, 14)] * 4
deck = [item for item in zip(card_face, card_value)]
random.shuffle(deck)
player_cards = list()
num_players = int(input("問請這次要建立幾個玩家？"))

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
            points += 10
        else:
            points += card[1]
    for card in player:
        if card[1]==1 and points<=11:
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
        print("Player #{}'s points is bust!".format(i))
    print(player)
    print("---------------------------------")
print("Winner is {}, winner's points is {}".format(winner, winner_points))

