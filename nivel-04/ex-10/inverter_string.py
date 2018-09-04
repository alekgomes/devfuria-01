# Inverter string 

def inverter(string):
	return string[::-1]     # extended slice
							# string [inicio:fim:step]
							#string[::-1] = string[0:-1:-1]

assert inverter('animal') == 'lamina'