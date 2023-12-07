 ================================================================
                     NADI 2023: The Fourth Nuanced Arabic Dialect Identification Shared Task
                        
=================================================================
                            TEST Phase
=================================================================

=================================================================
Description of Task
=================================================================

This shared task targets country-level dialect ID (Subtask 1) and dialect to MSA machine translation (Subtasks 2 and 3). The subtasks are:

Subtask 1 (Closed Country-level Dialect ID): In this subtask, we provide a new Twitter dataset (NADI-2023-TWT) that covers 18 dialects (a total of 23.4K tweets). We split this dataset into Train (18K), Dev (1.8K), and Test (3.6K). In addation, we provide external data from NADI 2020 (Abdul-Mageed et al., 2020), NADI 2021 (Abdul-Mageed et al., 2021), and MADAR (Bouamor et al., 2018) train datasets. We refer to these additional datasets as NADI-2020-TWT, NADI-2021-TWT, and MADAR-2018, respectively. This subtask is a closed track. In other words, participants are not allowed to use any other external data except the ones we provide to train their systems.

Subtask 2 (Closed Dialect to MSA MT): Sentence-level machine translation from four dialects to MSA. This subtask is a closed track where participants are allowed to use only our provided training data (i.e., MADAR-parallel-corpus). Our new Test datasets for this subtask will be in the following four dialects: Egyptian, Emirati, Jordanian, and Palestinian. In total, Test set is 2,000 sentences (500 from each dialect), and we also provide a Dev set that we will release to participants (n=400 sentences, 100 from each of the four dialects). Both our Dev and Test for Subtask 2 are new datasets that we manually prepare for the shared task. We keep the domain from which these Dev and Test sets unknown.
For training, we restrict this subtask to the MADAR parallel dataset. The MADAR dataset is available for acquisition directly from authors at MADAR-parallel-corpus (https://camel.abudhabi.nyu.edu/madar-parallel-corpus/). The dataset is described as follows: "The MADAR corpus is a collection of parallel sentences covering the dialects of 25 cities from the Arab World, in addition to English, French, and MSA. The corpus is created by translating selected sentences from the Basic Traveling Expression Corpus (BTEC) (Takezawa et al., 2007) to the different dialects. The exact details on the translation process and source and target languages are described in Bouamor et al. (2018)." Participants will be allowed to use only the Train split of MADAR parallel data for this subtask, and report on Dev and Test sets we provide. In other words, use of MADAR Dev and Test sets will not be allowed for this subtask.

Subtask 3 (Open Dialect to MSA MT): Sentence-level machine translation from four dialects to MSA.
This is the same as Subtask 2, but allows participants to train their systems on any additional datasets so long as these additional training datasets are public at the time of submission. For example, participants are allowed to manually create new parallel datasets. For transparency and wider community benefits, we require researchers participating in the open track subtask to submit the datasets they create along with their Test set submissions. We will collect all new datasets developed by participants and facilitate their distribution from direct download links. All new datasets will be distributed with appropriate credit to their authors. Clearly, one objective of this open track shared task is to encourage the creation of new datasets for machine translation of Arabic dialects.

=================================================================
Description of TEST Data
=================================================================
** Unlabeled TEST Data **

For subtask 1, we provide a unlabeled TEST dataset in a tsv file:
(1) ./Subtask_1/NADI2023_Subtask1_TEST_Unlabeled.tsv

For subtask 2, we provide a unlabeled TEST dataset is in a tsv file:
(1) ./Subtask_2/NADI2023_Subtask2_TEST_Unlabeled.tsv

For subtask 3, we provide a unlabeled TEST dataset is in a tsv file:
(1) ./Subtask_2/NADI2023_Subtask3_TEST_Unlabeled.tsv

We provide the following information:

For subtask 1:
- The first column (#1_id) contains an ID representing the data point/tweet.
- The second column (#2_content) contains the content of tweet. We convert user mention and hyperlinks to `USER' and `URL' strings, respectively.

For subtask 2 and 3:
- The first column (#1_id) contains an ID representing the data point/tweet.
- The second column (#2_dialect_id) contains a name of the source country-level dialect. 
- The third column (#3_source_dialect) contains a source dialect text.

** File Statistics **

Below, we present more details about the contents of the unlabeled TEST files.

(1) NADI2023_Subtask1_TEST_Unlabeled.tsv 3600 samples.

(2) NADI2023_Subtask2_TEST_Unlabeled.tsv and NADI2023_Subtask3_TEST_Unlabeled.tsv contains 2000 samples, respectively.

=================================================================
Instruction of TEST Submission  
=================================================================

The evaluation of shared tasks will be hosted through CODALAB. Teams will be provided with a CODALAB link for each shared task.
CODALAB link for NADI Shared Task Subtask 1: https://codalab.lisn.upsaclay.fr/competitions/14449
CODALAB link for NADI Shared Task Subtask 2: https://codalab.lisn.upsaclay.fr/competitions/14643
CODALAB link for NADI Shared Task Subtask 3: https://codalab.lisn.upsaclay.fr/competitions/14648

(1) Subtask 1 Test: To submit your prediction labels on the TEST set of subtask 1. Each team is allowed a maximum of 3 submissions. Note: The name of your submission should be 'teamname_subtask1_test_numberOFsubmission.zip' that includes a text file of your predictions (e.g., A submission 'ubc_subtask1_test_1.zip' that is the zip file of my prediction, 'ubc_subtask1_test_1.txt'.)

(2) Subtask 2 Test: To submit your prediction labels on the TEST set of subtask 2. Each team is allowed a maximum of 3 submissions. Note: The name of your submission should be 'teamname_subtask2_test_numberOFsubmission.zip' that includes a text file of your predictions (e.g., A submission 'UBC_subtask2_test_1.zip' that is the zip file of my prediction, 'UBC_subtask2_test_1.txt'.)

(3) Subtask 3 Test: To submit your prediction labels on the TEST set of subtask 3. Each team is allowed a maximum of 3 submissions. Note: The name of your submission should be 'teamname_subtask3_test_numberOFsubmission.zip' that includes a text file of your predictions (e.g., A submission 'UBC_subtask3_test_1.zip' that is the zip file of my prediction, 'UBC_subtask3_test_1.txt'.)

You can test your prediction on DEV set (we released before) submitting to the Development phase from the corresponding "development" Codalab tab (accessible when you click the links above).

Then, you should submit your final predictions on the TEST set to the corresponding Test phase by the deadline. 

**The deadline of all the subtasks are 2023-August-20 23:59:59 (Anywhere in the Earth)**
In the Test phase, each team can submit up to **three system** results for **each subtask**.

=================================================================
Shared Task Metrics and Restrictions:
=================================================================
- Macro-Averaged F-score will be the official metric for subtask 1 (dialect ID)
- Bleu score will be the official metric for subtask 2 and 3 (MT).

-------------------------------------
IMPORTANT: Participants are NOT allowed to use **NADI2023_Subtask1_DEV.tsv**, **NADI2023_Subtask2_DEV.tsv** or **NADI2023_Subtask3_DEV.tsv** for training purposes. Participants must report the performance of their best system on both DEV *and* TEST sets in their Shared Task system description paper.

-------------------------------------
For Subtask 1:
IMPORTANT: Participants can only use the official TRAIN sets provided by NADI-2023 (including NADI2023_Subtask1_TRAIN.tsv, NADI-2020-TWT.tsv, NADI-2021-TWT.tsv, and MADAR-2018.tsv).
Participants are NOT allowed to use any additional tweets, nor are they allowed to use outside information.
Specifically -- participants should not use meta data from Twitter about the users or the tweets, e.g., geo-location data.
External manually labelled data sets are *NOT* allowed.

-------------------------------------
For Subtask 2:
IMPORTANT: Participants can only use the official TRAIN sets provided by MADAR-parallel-corpus at (https://camel.abudhabi.nyu.edu/madar-parallel-corpus/). 
* You can only use the splits of Corpus-6-train and Corpus-6-test-corpus-26-train to train your model. 

Participants are NOT allowed to use any additional tweets, nor are they allowed to use outside information.
Specifically -- participants should not use meta data from Twitter about the users or the tweets, e.g., geo-location data.
External manually labelled data sets are *NOT* allowed.

-------------------------------------
For Subtask 3:
IMPORTANT: Participants are free to select their own or develop new training datasets for training. 
Participants can manually translate Mono-DA and/or Mono-MSA for that purpose, but they can also choose to acquire and translate any other datasets into any of the four dialects listed.

IMPORTANT: Participants should agree to share the full used training dataset they create with the community. We will collect these datasets during submission time and facilitate their distribution from direct download links. 

-------------------------------------
NADI2023-Twitter-Corpus-License.txt contains the license for using
this data.

================
Scoring scripts
================
./Subtask_1/NADI2023-ST1-Scorer.py is a python script for ** Subtask 1 ** that takes in two text files containing true labels and predicted labels and will output accuracy, macro F1 score, precision, and recall. Note that the official metric for subtask 1 is F1 score.

./Subtask_2/NADI2023-ST2-Scorer.py is a python script for ** Subtask 2 ** that takes in two text files containing GOLD target text and generated text and will output bleu scores for represented dialect and overall score. 

./Subtask_3/NADI2023-ST3-Scorer.py is as same as ./Subtask_2/NADI2023-ST2-Scorer.py. It is a python script for ** Subtask 3 ** that takes in two text files containing GOLD target text and generated text and will output bleu scores for represented dialect and overall score. 

Please read more descriptions of NADI2023-ST1-Scorer.py and NADI2023-ST2-Scorer.py below.

=================================================================
./Subtask_1/NADI2023-ST1-Scorer.py and Submission samples
=================================================================
We provide a sample of gold file and a submission sample file for Subtask 1. 

For example:
`./Subtask_1/subtask1_dev_GOLD.txt' is the gold label file of Dev set of subtask 1. 

The file `./Subtask_1/ubc_subtask1_dev_1.zip' is the zip file of my first submission.
This zip file contains only one txt file: `ubc_subtask1_dev_1.txt'. 
Unzipping `ubc_subtask1_dev_1.zip', you can get `ubc_subtask1_dev_1.txt' where each line is a label string. 

`subtask1_dev_GOLD.txt' and `UBC_subtask1_dev_1.txt' can be used with the NADI2023-ST1-Scorer.py.
NADI2023-ST1-Scorer.py evaluate the performance of submssion. 

Please make sure to have scikit-learn library installed.

-------------------------------------
Usage of the scorer:

    python3 NADI2023-ST1-Scorer.py  <gold-file> <pred-file>


In the dataset directory, there are example gold and prediction files. If they are used with the scorer, they should produce the following results:

python3 ./Subtask1/NADI2023-ST1-Scorer.py ./Subtask1/subtask1_dev_GOLD.txt ./Subtask1/UBC_subtask1_dev_1.txt 

OVERALL SCORES:
MACRO AVERAGE PRECISION SCORE: 5.39 %
MACRO AVERAGE RECALL SCORE: 5.38 %
MACRO AVERAGE F1 SCORE: 5.37 %
OVERALL ACCURACY: 6.28 %

=================================================================
(Subtask_2/NADI2023-ST2-Scorer.py) / (Subtask_3/NADI2023-ST3-Scorer.py)  and Submission samples
=================================================================
We provide a sample of gold file and a submission sample file for Subtask 2 and 3. 
Please make sure to have evaluate library installed.

For example:
`./Subtask_2/subtask2_dev_GOLD.txt' is the gold target text file of Dev set of subtask 2. 
`./Subtask_3/subtask3_dev_GOLD.txt' is the gold target text file of Dev set of subtask 3. 

The file `./Subtask_2/UBC_subtask2_dev_1.zip' is the zip file of my first submission.
This zip file contains only one txt file: `UBC_subtask2_dev_1.txt'. 
Unzipping `UBC_subtask2_dev_1.zip', you can get `UBC_subtask2_dev_1.txt' where each line is a label string. 

`subtask2_dev_GOLD.txt' and `UBC_subtask2_dev_1.txt' can be used with the NADI2023-ST2-Scorer.py.
NADI2022-ST2-Scorer.py evaluate the performance of submssion. 

-------------------------------------
Usage of the scorer:

    python3 NADI2023-ST2-Scorer.py  <gold-file> <pred-file>


In the dataset directory, there are example gold and prediction files. If they are used with the scorer, they should produce the following results:

python3 ./Subtask2/NADI2023-ST2-Scorer.py ./Subtask2/subtask2_dev_GOLD.txt ./Subtask2/ubc_subtask2_dev_1.txt 

Scores:
{'Overall': 86.30458125097962, 'Egyptain': 100.0, 'Emirati': 100.0, 'Jordanian': 100.0, 'Palestinian': 51.60840302349632}


=================================================================
Acknowledgements
=================================================================
The scoring script is borrowed from the MADAR 2019 Shared Task (Bouamor et al., 2019). The current README and the release package also follows and borrows from the MADAR Shared Task and NADI2021 releases. 

=================================================================
References
=================================================================

@article{zaidan2014arabic,
  title={Arabic dialect identification},
  author={Zaidan, Omar F and Callison-Burch, Chris},
  journal={Computational Linguistics},
  volume={40},
  number={1},
  pages={171--202},
  year={2014},
  publisher={MIT Press}
}

@inproceedings{bouamor2019madar,
  title={The MADAR shared task on Arabic fine-grained dialect identification},
  author={Bouamor, Houda and Hassan, Sabit and Habash, Nizar},
  booktitle={Proceedings of the Fourth Arabic Natural Language Processing Workshop},
  pages={199--207},
  year={2019}
}

@inproceedings{elfardy2013sentence,
  title={Sentence level dialect identification in Arabic},
  author={Elfardy, Heba and Diab, Mona},
  booktitle={Proceedings of the 51st Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},
  pages={456--461},
  year={2013}
}


@inproceedings{bouamor2018madar,
  title={The MADAR Arabic dialect corpus and lexicon},
  author={Bouamor, Houda and Habash, Nizar and Salameh, Mohammad and Zaghouani, Wajdi and Rambow, Owen and Abdulrahim, Dana and Obeid, Ossama and Khalifa, Salam and Eryani, Fadhl and Erdmann, Alexander and others},
  booktitle={Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC 2018)},
  year={2018}
}


@inproceedings{zhang2019no,
  title={No army, no navy: Bert semi-supervised learning of arabic dialects},
  author={Zhang, Chiyu and Abdul-Mageed, Muhammad},
  booktitle={Proceedings of the Fourth Arabic Natural Language Processing Workshop},
  pages={279--284},
  year={2019}
}

@inproceedings{abdul2018you,
  title={You tweet what you speak: A city-level dataset of arabic dialects},
  author={Abdul-Mageed, Muhammad and Alhuzali, Hassan and Elaraby, Mohamed},
  booktitle={Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC 2018)},
  year={2018}
}

@inproceedings{elaraby2018deep,
  title={Deep models for arabic dialect identification on benchmarked data},
  author={Elaraby, Mohamed and Abdul-Mageed, Muhammad},
  booktitle={Proceedings of the Fifth Workshop on NLP for Similar Languages, Varieties and Dialects (VarDial 2018)},
  pages={263--274},
  year={2018}
}

@inproceedings{mageed-etal-2020-nadi,
    title ={{NADI 2020: The First Nuanced Arabic Dialect Identification Shared Task}},
    author = {Abdul-Mageed, Muhammad and Zhang, Chiyu and Bouamor, Houda and Habash, Nizar},
    booktitle ={{Proceedings of the Fifth Arabic Natural Language Processing Workshop (WANLP 2020)}},
    year = {2020},
    address = {Barcelona, Spain}
}

@inproceedings{abdul-mageed-etal-2020-toward,
    title = "Toward Micro-Dialect Identification in Diaglossic and Code-Switched Environments",
    author = "Abdul-Mageed, Muhammad  and
      Zhang, Chiyu  and
      Elmadany, AbdelRahim  and
      Ungar, Lyle",
    booktitle = "Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    pages = "5855--5876",
}

@inproceedings{abdul-mageed-etal-2021-nadi,
    title = "{NADI} 2021: The Second Nuanced {A}rabic Dialect Identification Shared Task",
    author = "Abdul-Mageed, Muhammad  and
      Zhang, Chiyu  and
      Elmadany, AbdelRahim  and
      Bouamor, Houda  and
      Habash, Nizar",
    booktitle = "Proceedings of the Sixth Arabic Natural Language Processing Workshop",
    month = apr,
    year = "2021",
    address = "Kyiv, Ukraine (Virtual)",
    pages = "244--259",
}

================================================================
Copyright (c) 2022 The University of British Columbia, Canada; 
Carnegie Mellon University Qatar; New York University Abu Dhabi.
All rights reserved.
================================================================
