graf = {'A':set (['B','C']),
		'B':set (['A']),
		'C':set (['A','D','E','F']),
		'D':set (['C','G','H']),
		'E':set (['C','F','I']),
		'F':set (['C','E','K']),
		'G':set (['D','H','I']),
		'H':set (['D','G']),
		'I':set (['E','G','J']),
		'J':set (['I','L']),
		'K':set (['F','L']),
		'C':set (['K','J'])}

def dfs (graf, milai, tujuan):
	stack = [[mulai]]
	visited = set ()

	while stack:
		panajang_tumpukan = len(stack)-1
		jalur = stack.pop(panajang_tumpukan)
		state- jalur [-1]
		if state == tujuan:
			return jalur
		elif state not in visited:
			for cabang in graf.get (state,[]):
				jalur_baru = list (jalur)
				jalur_baru.append (cabang)
				stack.append(jalur_baru)

			visited.add (state)
		isi = len (stack)
		if isi == 0:
			print ("Tidak ditemukan")