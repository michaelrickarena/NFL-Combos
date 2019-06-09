import itertools
import csv

def comb1(k, available, used):
	if len(used)==k: #hits the required number of units in a combo
		yield tuple(used)
	elif len(available)==0: # went through all avaliable and has none left over
		pass
	else:
		head=available.pop(0) #if head is used in tuple, remove it from list and append the item.
		used.append(head)
		for c in comb1(k, available[:], used[:]):
			yield c
		used.pop()
		for c in comb1(k, available[:], used[:]):
			yield c

def comb_wrapper(k,s,n):
	for c in comb1(k,list(s),[]):
		if sum(s[i]['cost'] for i in c) == n:
			yield c

s={'Matt Ryan (11853797)': {'cost': 9600, 'position': 'QB', 'team': 'ATL'}, 'Ben Roethlisberger (11853793)': {'cost': 9500, 'position': 'QB', 'team': 'PIT'}, 'Patrick Mahomes (11853792)': {'cost': 9400, 'position': 'QB', 'team': 'KC'}, 'Carson Wentz (11853813)': {'cost': 9300, 'position': 'QB', 'team': 'PHI'}, 'Josh Johnson (11853817)': {'cost': 9200, 'position': 'QB', 'team': 'WAS'}, 'Drew Brees (11853795)': {'cost': 9100, 'position': 'QB', 'team': 'NO'}, 'Philip Rivers (11853796)': {'cost': 9000, 'position': 'QB', 'team': 'LAC'}, 'Jared Goff (11853799)': {'cost': 8900, 'position': 'QB', 'team': 'LAR'}, 'Blake Bortles (11853833)': {'cost': 8800, 'position': 'QB', 'team': 'JAX'}, 'Jameis Winston (11853800)': {'cost': 8700, 'position': 'QB', 'team': 'TB'}, 'Eli Manning (11853814)': {'cost': 8600, 'position': 'QB', 'team': 'NYG'}, 'Derek Carr (11853812)': {'cost': 8500, 'position': 'QB', 'team': 'OAK'}, 'Aaron Rodgers (11853798)': {'cost': 8400, 'position': 'QB', 'team': 'GB'}, 'Dak Prescott (11853805)': {'cost': 8300, 'position': 'QB', 'team': 'DAL'}, 'Tom Brady (11853803)': {'cost': 8200, 'position': 'QB', 'team': 'NE'}, 'Russell Wilson (11853801)': {'cost': 8100, 'position': 'QB', 'team': 'SEA'}, 'Nick Foles (11853804)': {'cost': 8000, 'position': 'QB', 'team': 'PHI'}, 'Kirk Cousins (11853808)': {'cost': 7900, 'position': 'QB', 'team': 'MIN'}, 'Mitchell Trubisky (11853806)': {'cost': 7800, 'position': 'QB', 'team': 'CHI'}, 'Nick Mullens (11853819)': {'cost': 7700, 'position': 'QB', 'team': 'SF'}, 'Deshaun Watson (11853794)': {'cost': 7600, 'position': 'QB', 'team': 'HOU'}, 'Sam Darnold (11853810)': {'cost': 7500, 'position': 'QB', 'team': 'NYJ'}, 'Baker Mayfield (11853809)': {'cost': 7400, 'position': 'QB', 'team': 'CLE'}, 'Case Keenum (11853816)': {'cost': 7300, 'position': 'QB', 'team': 'DEN'}, 'Matthew Stafford (11853811)': {'cost': 7200, 'position': 'QB', 'team': 'DET'}, 'Josh Allen (11853802)': {'cost': 7100, 'position': 'QB', 'team': 'BUF'}, 'Chris Carson (11853890)': {'cost': 7000, 'position': 'RB', 'team': 'SEA'}, 'C.J. Anderson (11853922)': {'cost': 6900, 'position': 'RB', 'team': 'LAR'}, 'Jordan Howard (11853954)': {'cost': 6800, 'position': 'RB', 'team': 'CHI'}, "D'Onta Foreman (11853960)": {'cost': 6700, 'position': 'RB', 'team': 'HOU'}, 'Gus Edwards (11853936)': {'cost': 6600, 'position': 'RB', 'team': 'BAL'}, 'Aaron Jones (11853904)': {'cost': 6500, 'position': 'RB', 'team': 'GB'}}
k=6
mycombs=list(comb_wrapper(k, s, 49800))

print(mycombs)