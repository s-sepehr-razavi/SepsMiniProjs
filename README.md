### Bengio2003

**Objective**: To implement the language model described in Yoshua Bengio's 2003 paper using a simple Multi-Layer Perceptron (MLP) architecture.  
**Details**: The model is trained on a dataset of Persian names, operating at the character level. The goal is to generate new names by predicting the next character in a sequence.

### Wavenet

**Objective**: To improve upon the Bengio2003 model by implementing the WaveNet architecture for character-level language modeling.  
**Details**: This project continues the focus on Persian name generation, using the more advanced WaveNet structure to produce names with more complex patterns and variations.

### Skipgram

**Objective**: To implement the Word2Vec Skip-gram model and train it on Persian poetry to learn meaningful word embeddings.  
**Details**: The model is trained on Saeb Tabrizi's Ghazals, capturing the semantic relationships between words in Persian literature. The resulting embeddings can be used to explore the meaning and context of words within the poetic corpus.

### PoetGPT

**Objective**: To implement a character-level language model with attention mechanisms, trained on Persian poetry.  
**Details**: Inspired by the "Attention Is All You Need" paper, this model is trained on Saeb Tabrizi's Ghazals to generate poetic text in Persian, emulating the style and structure of the original works.

### ByteBPE

**Objective**: To implement a byte-level Byte Pair Encoding (BPE) tokenizer for efficient tokenization of text at the byte level.  
**Details**: Inspired by subword tokenization techniques, this tokenizer operates on raw byte sequences, splitting input text into smaller, more manageable subword units. The BPE algorithm merges frequently occurring byte pairs in the corpus, iteratively building a vocabulary. The model is designed to handle diverse character sets and languages, making it highly versatile for tasks like language modeling and machine translation, where managing rare tokens efficiently is crucial.

### ALittleFuzzy

A small module for performing fuzzy inference with its journal.
