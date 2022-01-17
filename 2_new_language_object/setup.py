
from setuptools import setup
setup(
    name="clara",
    entry_points={
        "spacy_languages": ["clara = clara:ClassicalArabic"],
    }
)
