This folder contains files that were annotated (manually or semi-manually with an annotation program) to train a model for Span Categorization. This folder provides the main source of training data and should be split between training and validation sets.

Format:
- The annotated files are in the CONLL format, i.e. each token is followed by a tab, a label and a new line.
- Text units (like sentences or paragraphs) are separated from each other by two new lines.
- The labels are `B` to mark the beginning of the span, `I` to mark the inner part of the span, and `O` for the tokens that do not belong to the span.
