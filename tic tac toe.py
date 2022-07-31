import os
from time import sleep
from colorama import Fore
from random import randint

tic = [[[""], [""], [""]], [[""], [""], [""]], [[""], [""], [""]]]

def validate(lista, l):
	i = []
	for c in lista:
		i.append(c[0])
	lista = i
	
	if lista[:3].count(l) == 3 or lista[3:6].count(l) == 3 or lista[6:9].count(l) == 3:
		return True
		
	elif lista[0:9:3].count(l) == 3 or lista[1:9:3].count(l) == 3 or lista[2:9:3].count(l) == 3:
		return True
		
	elif lista[0:9:4].count(l) == 3 or lista[2:8:2].count(l) == 3:
		return True
		
	else:
		return False
	
def a(vez):
	if vez % 2 == 0:
		print(f"""{Fore.CYAN}{'-='*2}Tic Tac Toe{'=-'*2}\n[ {tic[0][0][0]} ][ {tic[0][1][0]} ][ {tic[0][2][0]} ]
[ {tic[1][0][0]} ][ {tic[1][1][0]} ][ {tic[1][2][0]} ]
[ {tic[2][0][0]} ][ {tic[2][1][0]} ][ {tic[2][2][0]} ]""")
	else:
		print(f"""{Fore.LIGHTGREEN_EX}{'-='*2}Tic Tac Toe{'=-'*2}\n[ {tic[0][0][0]} ][ {tic[0][1][0]} ][ {tic[0][2][0]} ]
[ {tic[1][0][0]} ][ {tic[1][1][0]} ][ {tic[1][2][0]} ]
[ {tic[2][0][0]} ][ {tic[2][1][0]} ][ {tic[2][2][0]} ]""")

ms = int(input(f"{'-='*2}Tic Tac Toe{'=-'*2}\n[ 1 ] 1 Jogador\n[ 2 ] 2 jogadores\n"))

if ms > 2 or ms < 1: raise ValueError("Escolha entre 1 e 2")

if ms == 2 or ms == 1:
	vez = 0 # par = jogador 1
	tac = [[[1], [2], [3]], [[4], [5], [6]], [[7], [8], [9]]]
	while True:
		os.system("cls")
		a(vez)
		
		if ms == 1:
			print(f"\n[X]Jogador 1: Sua vez!\n[O]Computador" if vez % 2 == 0 else f"\n[X]Jogador 1\n[O]Computador: Sua vez!")
		else:
			print(f"\n[X]Jogador 1: Sua vez!\n[O]Jogador 2" if vez % 2 == 0 else f"\n[X]Jogador 1\n[O]Jogador 2: Sua vez!")
			
		print(Fore.RESET)
		print(f"""\nJogadas possíveis\n[ {tac[0][0][0]} ][ {tac[0][1][0]} ][ {tac[0][2][0]} ]
[ {tac[1][0][0]} ][ {tac[1][1][0]} ][ {tac[1][2][0]} ]
[ {tac[2][0][0]} ][ {tac[2][1][0]} ][ {tac[2][2][0]} ]""")
		if ms == 2:
			whe = int(input())
		else:
			if vez % 2 == 0:
				whe = int(input())
			else:
				past = []
				if whe not in past:
					whe = randint(1, 9)
					past.append(whe)
				else:
					whe = randint(1, 9)
					past.append(whe)
		whe -= 1
		if vez % 2 == 0:
			if whe < 3:
				if tac[0][whe][0] != "~":
					tic[0][whe][0] = "X"
					tac[0][whe][0] = "~"
			elif whe < 6 and whe >= 3:
				if tac[1][whe-3][0] != "~":
					tic[1][whe-3][0] = "X"
					tac[1][whe-3][0] = "~"
			elif whe <= 9 and whe >= 6:
				if tac[2][whe-6][0] != "~":
					tic[2][whe-6][0] = "X"
					tac[2][whe-6][0] = "~"
			vez += 1
		else:
			if whe < 3:
				if tac[0][whe][0] != "~":
					tic[0][whe][0] = "O"
					tac[0][whe][0] = "~"
			elif whe < 6 and whe >= 3:
				if tac[1][whe-3][0] != "~":
					tic[1][whe-3][0] = "O"
					tac[1][whe-3][0] = "~"
			elif whe <= 9 and whe >= 6:
				if tac[2][whe-6][0] != "~":
					tic[2][whe-6][0] = "O"
					tac[2][whe-6][0] = "~"
			vez += 1
		final = [x for x in tic[0]] + [x for x in tic[1]] + [x for x in tic[2]]
		
		if validate(final, "X"):
			print(f"{Fore.CYAN}\nJogador 1 venceu!")
			break
		elif validate(final, "O"):
			print(f"{Fore.LIGHTGREEN_EX}\nJogador 2 venceu!")
			break
		
		lista = []
		for c in tac:
			for i in c:
				lista.append(i[0])
		if lista.count("~") == len(lista):
			print(f"{Fore.LIGHTRED_EX}\nEmpate!")
			break

sleep(3)