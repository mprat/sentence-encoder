import argparse
from collections import Counter
import re


def counter_dict(sentence):
    sentence = sentence.lower()
    pattern = re.compile('[\W_]+')
    sentence = pattern.sub('', sentence)
    c = Counter(sentence)
    return c


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="letter counter for a sentence")
    parser.add_argument("-s", dest="sentence", type=str, required=True)

    args = parser.parse_args()
    sentence = args.sentence

    counter_dict = counter_dict(sentence)
    print sorted(counter_dict.items())
