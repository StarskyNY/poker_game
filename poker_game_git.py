import pandas as pd
import numpy as np
import random

class Cards(object):

	royal = {11:'J',12:'Q',13:'K',14:'A'}
	counter = 0
	number = random.randint(1,14)
	suit = ['Diamonds','Spades','Hearts','Clubs']

	def __init__(self):
		Cards.counter += 1
		self.number = self.number
		self.suit = self.suit
		card = str(self.number) + ":"+ str(self.suit)

	def random_card(self):
		if self.number > 10:
			self.number = self.royal[self.number]
		self.suit = random.choice(self.suit)
		return str(self.number) + ":"+ str(self.suit)


class Deck(Cards):
	deck = [str(number)+"-"+y for number in range(1,14) for y in ['Diamonds','Spades','Hearts','Clubs']]

	def __init__(self):
		Cards.__init__(self)


class Poker(Deck):
	pot = "cheeks"

	def __init__(self):
		Deck.__init__(self)

	def poker_hand(self):
		hand = []
		count = 5
		while count > 0:
			card = random.choice(self.deck)
			self.deck.remove(card)
			hand.append(card)
			count -=1
		print (sorted(hand))
		return hand

	def flop(self):
		flop_cards = []
		count = 3
		while count >0:
			card = random.choice(self.deck)
			self.deck.remove(card)
			flop_cards.append(card)
			count -=1
		print (flop_cards)
		return flop_cards

	def river(self):
		flop_cards = []
		count = 1
		while count >0:
			card = random.choice(self.deck)
			self.deck.remove(card)
			flop_cards.append(card)
			count -=1
		print (flop_cards)
		return flop_cards

	def turn(self):
		flop_cards = []
		count = 1
		while count >0:
			card = random.choice(self.deck)
			self.deck.remove(card)
			flop_cards.append(card)
			count -=1
		print (flop_cards)
		return flop_cards

class Player(Deck):

	def __init__(self,name,chp_count):
		Deck.__init__(self)
		self.name = name
		self.chp_count = chp_count

	def player_hand(self):
		# self.player = player
		hand = []
		count = 5
		while count > 0:
			card = random.choice(self.deck)
			self.deck.remove(card)
			hand.append(card)
			count -=1
		# print (sorted(hand))
		return hand

	def bet(self,bet_amount):
		self.bet_amount = bet_amount 
		answer = self.chp_count - self.bet_amount 
		print (answer)
		return answer

	def raise_bet(self,bet_amount):
		self.bet_amount = bet_amount 
		answer = self.chp_count - self.bet_amount 
		print (answer)
		return answer


def winning_hand(player_list):
	#takes in a list of players + their hands 
	ply1_hand = []
	for player_hands in player_list:
		# print player_hands.player)
		for cards in player_hands:
			# print (cards)
			cards = cards.split("-")
			card_num= int(cards[0])
			ply1_hand.append(card_num)
		# print (ply1_hand)


#--------------------------------------------------------#

star = Player("star",2500)
star_hand = (star.player_hand())
ash = Player("ash",2500)
ash_hand = ash.player_hand()
print (star_hand)
print (ash_hand,star.chp_count)

play_list = [ash_hand,star_hand]















