import spacy
from spacy.tokens import DocBin
from sklearn.model_selection import train_test_split
import click
from spacy.util import get_lang_class

@click.command()
@click.option('--infiles',  "-i", multiple=True)
@click.option('--train_ratio',  "-r", type=float, default=.8)
def hello(infiles, train_ratio):

    merged = DocBin()
    for infile in infiles:
        merged.merge(
            DocBin().from_disk(infile)
        )
    
    nlp = get_lang_class('xx')()
    docs = list(merged.get_docs(nlp.vocab))

    train_docs, test_docs = train_test_split(docs, train_size=train_ratio)

    train_db = DocBin()
    test_db = DocBin()

    for doc in train_docs:
        train_db.add(doc)

    for doc in test_docs:
        test_db.add(doc)

    train_db.to_disk("corpus/train.spacy")    
    test_db.to_disk("corpus/test.spacy")    

if __name__ == '__main__':
    hello()