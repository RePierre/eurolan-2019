# This script merges the manually annotated corpus with the rest of the corpus used for training.

from bs4 import BeautifulSoup as bs
from argparse import ArgumentParser


def merge_corpora(args):
    f = open(args.manually_annotated, "r", encoding="utf-8")
    xml1 = bs(f.read(), 'xml')
    f = open(args.training_corpus, "r", encoding="utf-8")
    xml2 = bs(f.read(), 'xml')

    for sent in xml2.find_all("sentence"):
        xml1.treebank.append(sent)

    f = open(args.output_corpus, "w", encoding="utf-8")
    f.write(str(xml1))


def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument('--manually-annotated',
                        required=True,
                        help='The manually annotated corpus.')
    parser.add_argument('--training-corpus',
                        required=True,
                        help='The rest of the corpus used for training.')
    parser.add_argument('--output-corpus',
                        required=False,
                        default='train.xml',
                        help='The name of the merged corpus.')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    merge_corpora(args)
