# 🌱 Project Language: Classical Arabic or clara

This repository is the central point for documentation and data for our project. You will find here several folders where we  store the data and code used as we create data and train models for Classical Arabic. 

`0_original_texts`: This folder contains the original text files for the project. This is a record of the original state of the texts before any pre-processing and annotation.

`1_lookups_data`: This folder contains the json lookups files for unambiguous lemmata, pos, and feats. This data is used to document the bulk annotation process and is superseded by the manually annotated data from INCEpTION [see the References section at the bottom of the page].

Lookups data have not been used in the current training.

`2_new_language_object`: This folder contains the nlp object folder from either Cadet or the Cadet notebook. This folder is fetched during training to load the new language object.

`3_inception_export`: This folder contains the CoNLL-U data that is exported from the annotation tool INCEpTION [see the Reference section at the bottom of the page] once annotation work is completed. During training, this folder provides the main source of training data and should be split between training and validation sets.

`4_trained_models`: This folder contains the link to the new language models for Classical Arabic which will be stored on Zenodo.

## Language
This project aims at adding Classical Arabic to spaCy NLP pipeline by training a model on Classical Arabic texts. 

## Dataset Summary 
Our training data are extracted from the open-source and open-access corpus OpenITI [see References at the bottom of this page].

## Curation Rationale
We have chosen to work with OpenITI texts because the corpus is open-source, open-access and schoalrly curated.
We selected texts related to our current research and took care of gathering diverse data to avoid over-fitting our models.

NB See the sections on Mission Statement and Collection Development Policy in Jo and Gebru, ["Lessons from Archives"](https://arxiv.org/abs/1912.10389)  
  
## Source Data
The data for this project will be released as soon as our research has been published.  

## Licensing Information
Please refer to the References and Citation section.

## Dataset Curators
Irene Kirchner
Maroussia Bednarkiewicz

## References
`INCEpTION`
Klie, J.-C., Bugert, M., Boullosa, B., Eckart de Castilho, R. and Gurevych, I. (2018): The INCEpTION Platform: Machine-Assisted and Knowledge-Oriented Interactive Annotation. In Proceedings of System Demonstrations of the 27th International Conference on Computational Linguistics (COLING 2018), Santa Fe, New Mexico, USA.
https://inception-project.github.io/

`OpenITI`
Nigst, Lorenz, Romanov, Maxim, Savant, Sarah Bowen, Seydi, Masoumeh, & Verkinderen, Peter. (2022). OpenITI: a Machine-Readable Corpus of Islamicate Texts (2022.1.6) [Data set]. Zenodo.
https://doi.org/10.5281/zenodo.6808108


## Citation Information
- How to cite this project. 
