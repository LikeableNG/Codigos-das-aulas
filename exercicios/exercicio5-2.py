horario = input("Digite que horas são (no formato HH:MM): ")
hora = horario[0:2]
hora_int = int(hora)

if hora_int >= 0 and hora_int <= 11:
	print('Bom dia!')

elif hora_int >= 12 and hora_int <= 17:
	print('Boa tarde!')

else:
	print('Boa noite!')