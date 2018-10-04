# A Morphology-based Representation Model for LSTM-based Dependency Parsing of Agglutinative Languages


This repository contains an updated version of [LSTM-Parser](https://github.com/clab/lstm-parser) and it is submitted to the CoNLL 2018 UD Shared Task by the BOUN team.

The full description of the updated version of the parser can be found [here](http://universaldependencies.org/conll18/proceedings/pdf/K18-2024.pdf).

You can find the source codes of the lemma-suffix model, the morphological features model and the baseline model under following branches: [lemmaSuffix](https://github.com/CoNLL-UD-2018/BOUN/tree/lemmaSuffix), [wordMorp](https://github.com/CoNLL-UD-2018/BOUN/tree/wordMorp), [baseline](https://github.com/CoNLL-UD-2018/BOUN/tree/baseline).

For the installation of the required software, please follow the instruction in the [LSTM-Parser code repository](https://github.com/clab/lstm-parser/tree/char-based).

After the installation of the required software, please replace the following files and folders with the ones in the [lemmaSuffix](https://github.com/CoNLL-UD-2018/BOUN/tree/lemmaSuffix) branch to experiment with the lemma-suffix model, or the ones in the [wordMorp](https://github.com/CoNLL-UD-2018/BOUN/tree/wordMorp) branch to experiment with the morphological features model:

* cmake folder
* cnn folder
* parser folder
* CMakeLists.txt
* ParserOracleArcStdWithSwap.jar



If you make use of this version of LSTM parser, please make the following citation:

```
@InProceedings{ozates2018conll,
  author    = {{\"{O}}zate{\c{s}}, {\c{S}}aziye Bet{\"{u}}l  and  {\"{O}}zg{\"{u}}r, Arzucan  and  Gungor, Tunga  and  {\"{O}}zt{\"{u}}rk, Balkız},
  title     = {A Morphology-Based Representation Model for {LSTM}-Based Dependency Parsing of Agglutinative Languages},
  booktitle = {Proceedings of the {CoNLL} 2018 Shared Task: Multilingual Parsing from Raw Text to Universal Dependencies},
  month     = {October},
  year      = {2018},
  address   = {Brussels, Belgium},
  publisher = {Association for Computational Linguistics},
  pages     = {238--247},
  url       = {http://www.aclweb.org/anthology/K18-2024}
}
```
