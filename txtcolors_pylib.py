#******************************************************
 # Dioghenes
 # Polytechnic of Turin
 # 2016
 # txtcolors_pylib v0.2
#******************************************************

_textcolors = {"dgray":"30",\
			  "red":"31",\
			  "green":"32",\
			  "yellow":"33",\
			  "blue":"34",\
			  "purple":"35",\
			  "cyan":"36",\
			  "lgray":"37",\
			  }

_styles = {"":"0",\
		   "normal":"0",\
		   "bold":"1",\
		   "dark":"2",\
		   "corsive":"3",\
		   "underline":"4",\
		   "negative":"7",\
		   "strike":"9"}

_bgcolors = {"red":"41m",\
			"green":"42m",\
			"yellow":"43m",\
			"blue":"44m",\
			"purple":"45m",\
			"cyan":"46m",\
			"gray":"40m",\
			"gray":"47m"}

_escape = '\033['

def hprint(string,col="white",bgcol="black",style="normal",oneLine=True):
	global _textcolors,_styles,_bgcolors,_escape

	head = _escape

	#Set the style
	i = 0
	flag = 0
	while i < len(_styles):
		if style == _styles.keys()[i]:
			head = head + _styles.values()[i]
			flag = 1
			break
		i += 1
	if flag == 0:
		head = head + "0"
	head = head + ";"

	#Set the color of the text
	i = 0
	flag = 0
	while i < len(_textcolors):
		if col == _textcolors.keys()[i]:
			head = head+_textcolors.values()[i]
			flag = 1
			break
		i += 1
	if flag == 0:
		head = head + "38"
	head = head + ";"

	#Set the color of the background
	i = 0
	flag = 0
	while i < len(_bgcolors):
		if bgcol == _bgcolors.keys()[i]:
			head = head+_bgcolors.values()[i]
			flag = 1
			break
		i += 1
	if flag == 0:
		head = head + "48m"
	head = head + " "

	string = head + string

	if oneLine == True:
		foot = "\033[0;m"
		string = string + foot

	return string
