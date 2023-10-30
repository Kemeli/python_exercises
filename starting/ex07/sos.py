def get_morse_dict():
	morse_code_dict = {
		'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
		'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
		'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
		'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
		'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
		'Z': '--..',
		'1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
		'6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
		' ': '/ '
	}
	return morse_code_dict


def sos(string):
	morse_code = ""
	morse_code_dict = get_morse_dict()
	for char in string:
		if char.upper() not in morse_code_dict:
			return ("String argument should only contain alphanumeric characters")
		else:
			morse_code += morse_code_dict[char.upper()]
	return(morse_code)
