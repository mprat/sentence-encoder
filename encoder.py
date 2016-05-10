import argparse


def encode(sentence, keyword):
	print "keyword is %s" % keyword
	return sentence


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Encode a sentnce with a keyword.")
	parser.add_argument("-s", dest="sentence", type=str, required=True)
	parser.add_argument("-k", dest="keyword", type=str, required=True)

	args = parser.parse_args()
	print encode(args.sentence, args.keyword)