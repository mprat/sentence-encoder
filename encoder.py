import argparse
import string


def construct_dictionary(keyword):
	keyword_letters = set(list(keyword))
	if len(keyword_letters) != len(keyword):
		raise ValueError("Keyword should have unique letters")

	lowercase_letters = list(string.ascii_lowercase)
	for letter in keyword_letters:
		lowercase_letters.remove(letter)
	lowercase_letters.reverse()
	final_string = keyword + "".join(lowercase_letters)
	return dict(zip(string.ascii_lowercase, final_string))

def encode(sentence, keyword):
	print "keyword is %s" % keyword
	return sentence


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Encode a sentnce with a keyword.")
	parser.add_argument("-s", dest="sentence", type=str, required=True)
	parser.add_argument("-k", dest="keyword", type=str, required=True)

	args = parser.parse_args()
	print encode(args.sentence, args.keyword)