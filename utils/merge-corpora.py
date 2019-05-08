# This script merges the manually annotated corpus with the rest of the corpus used for training.

from argparse import ArgumentParser
import xml.etree.ElementTree as ET


def is_annotated(sentence, fully_annotated=True):
    for word in sentence.findall('word'):
        if not word.get('deprel') and fully_annotated:
            return False
    return True


def merge_corpora(args):
    team_corpus = ET.parse(args.team_corpus)
    train_corpus = ET.parse(args.training_corpus)
    corpus_root = train_corpus.getroot()
    sentences = [
        sentence for sentence in team_corpus.findall('sentence')
        if is_annotated(sentence, not args.allow_incomplete)
    ]
    for sentence in sentences:
        text = [word.get('form') for word in sentence.findall('word')]
        text = ' '.join(text)
        print('Appending sentence [{}] to corpus.'.format(text))
        corpus_root.append(sentence)
    train_corpus.write(args.output_corpus, encoding='utf-8')


def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument(
        '--team-corpus',
        required=True,
        help='The corpus which was manually annotated by the team.')
    parser.add_argument('--training-corpus',
                        required=True,
                        help='The rest of the corpus used for training.')
    parser.add_argument(
        '--allow-incomplete',
        help='If specified, the merge will include incomplete sentences.',
        action='store_true')
    parser.add_argument('--output-corpus',
                        required=False,
                        default='train.xml',
                        help='The name of the merged corpus.')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    merge_corpora(args)
