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
	encoder_dict = construct_dictionary(keyword)

	return ("".join(map(lambda x: encoder_dict.get(x, x), sentence)), encoder_dict)


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Encode a sentence with a keyword.")
	parser.add_argument("-s", dest="sentence", type=str, required=True)
	parser.add_argument("-k", dest="keyword", type=str, required=True)
	parser.add_argument("--show-dict", required=False, action="store_true")

	args = parser.parse_args()
	sentence = args.sentence.lower()
	keyword = args.keyword.lower()
	show_dict = args.show_dict
	(encoded_sentence, encoder_dict) = encode(sentence, keyword)
	print "Original sentence: %s" % sentence.upper()
	print "Keyword: %s" % keyword.upper()
	print "Encoded sentence: %s" % encoded_sentence.upper()
	if show_dict:
		print "Dictionary: %s" % sorted(encoder_dict.items())
