import re

with open("nlp.txt") as fp:
	for sentence in re.split(r"(?<=[\.;:?!]) (?=[A-Z])", fp.read()):
		print sentence
