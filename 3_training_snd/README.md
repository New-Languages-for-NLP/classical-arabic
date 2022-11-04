This folder contains files that were annotated (with INCEpTION or Stanza).
This folder provides the main source of training data and should be split between training and validation sets.

# NER
- The annotated files for NER are in the CONLL format.
- The annotated text was divided in three [CL1, CL2, CL3] and each part was annotated by different people.

The filenames ending with C1, C2, and C3 correspond to parts 1, 2 and 3 of the text 0597IbnJawzi.Mawducat.ShamAY0034138-ara1-CL.
- *C1* has 2605 lines, 115211 tokens (words)
- *C2* has 2119 lines, 83410 tokens (words)
- *C3* has 1977 lines, 75386 tokens (words)

## 0597IbnJawzi.Mawducat.ShamAY0034138-ara1-CL.conll
This file contains the concatenated version of C1, C2 and C3.

# Span or Chunk
- The annotated files for Span or Chunk are in the JSON format.
- The filename end with "-snd" for isnad, because each span or chung matches an isnad or chain of transmitters.
