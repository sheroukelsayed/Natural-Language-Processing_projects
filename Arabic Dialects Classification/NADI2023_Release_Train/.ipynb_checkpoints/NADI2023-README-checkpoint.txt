 ================================================================
                    NADI 2023: The Fourth Nuanced Arabic Dialect Identification Shared Task

=================================================================
Summary
=================================================================

Arabic is a rich language with a wide collection of dialects. Many of these dialects remain under-studied, primarily due to limited resources (research funding, datasets, etc.). The goal of the Nuanced Arabic Dialect Identification (NADI) shared task series is to alleviate this bottleneck by providing datasets and modeling opportunities for participants to carry out dialect identification, and in general dialect processing. Dialect identification is the task of automatically detecting the source variety of a given text or speech segment. In addition to nuanced dialect identification at the country level, NADI 2022 offered a new subtask focused on country-level sentiment analysis. 

NADI 2023 continues this tradition of extending to tasks beyond dialect identification. Namely, we propose a new open track subtask focused at machine translation (MT) in two directions (i) into Modern Standard Arabic (MSA) from four Arabic dialects and (ii) into any of the four dialects from MSA. In this open track subtask, we allow participants to develop datasets under particular conditions and use them to develop systems. Namely, we allow participants to create datasets mapping MSA into dialectal Arabic (DA) that can be exploited to train their MT systems.

While we invite participation in either of the two subtasks, we hope that teams will submit systems to both tasks (i.e., participate in the two tasks rather than only one task). By offering two subtasks, we hope to receive systems that exploit diverse machine learning architectures. This could include multi-task learning systems as well as sequence-to-sequence architectures in a single model such as the text-to-text Transformers (e.g., mT5, AraT5). Many other approaches could also be possible and we look forward to creative approaches to the subtasks. We introduce the two subtasks next.

=================================================================
NADI 2022 Shared Task
=================================================================

Description of Task:
--------------------

Subtask 1 (Closed Track): Country-level dialect identification. In this subtask, we provide a new Twitter dataset that covers 18 dialects (a total of 23.4K tweets). We spit this dataset into Train (18K), Dev (1.8K), and Test (3.6K). This subtask is a closed track. In other words, participants are not allowed to use any external data to train their systems.

Subtask 2 (Open Track): Sentence-level machine translation in two directions (A) into Modern Standard Arabic (MSA) from four Arabic dialects and (B) into any of the four dialects from MSA. This subtask is an open track where we allow participants to create new parallel datasets to use for training their MT systems. Participants are also allowed to create parallel datasets using automated methods if they so wish. For transparency and wider community benefits, we require researchers participating in the open track subtask to submit the datasets they create along with their Test set submissions.
Our Test datasets for the MT subtask will be in the following four dialects: Egyptian, Emariti, Jordanian, and Palestinian. For each direction (A and B), In total, Test set is 1,000 sentences (250 from each dialect), and we also provide a Dev set that we will release to participants (n=250 sentences, 50 from each of the four dialects). Both our Dev and Test for Subtask 2 in both directions are new datasets that we manually prepare for the shared task. We keep the domain from which these Dev and Test sets unknown.
To summarize, for the open track (Subtask 2; MT), we only release Dev and Test data. For the training data, participants are free to select their own or develop new training datasets. Participants can manually translate Mono-DA and/or Mono-MSA for that purpose, but they can also choose to acquire and translate any other datasets into any of the four dialects listed. Participants should agree to share the full used training dataset they create with the community. We will collect these datasets during submission time and facilitate their distribution from direct download links. Clearly, one objective of this open track shared task is to encourage creation of new datasets for machine translation of Arabic dialects.


** Labeled Data **
For subtask 1, we provide Train and Dev data in two tsv files respectively:
(1) ./Subtask_1/NADI2023_Subtask1_TRAIN.tsv
(2) ./Subtask_1/NADI2023_Subtask1_DEV.tsv

For TRAIN and DEV files, we provide the following information:
- The first column (#1_id) contains an ID representing the data point/tweet.
- The second column (#2_content) contains the content of tweet. We convert user mention and hyperlinks to `USER' and `URL' strings, respectively.
- The third column (#3_label) contains gold label of the tweet at country-level. 

For subtask 2, we only provide Dev data data are in tsv files:
(1) Subtask 2-A: MSA to dialect translation:
    ./Subtask_2A/NADI2023_Subtask2A_DEV.tsv

For DEV file, we provide the following information:
- The first column (#1_id) contains an ID representing the data point/tweet.
- The second column (#2_dialect_id) contains the dialect of the target text at country-level. 
- The third column (#3_source_msa) contains the source text (MSA).
- The fourth column (#4_target_dialect) contains the target dialect text.

(2) Subtask 2-B: Dialect to MSA translation:
    ./Subtask_2B/NADI2023_Subtask2B_DEV.tsv

For DEV file, we provide the following information:
- The first column (#1_id) contains an ID representing the data point/tweet.
- The second column (#2_dialect_id) contains the dialect of the source text at country-level. 
- The third column (#3_dialect_msa) contains the source dialect text.
- The fourth column (#4_target_msa) contains the target text (MSA).

Addational resources for Subtask2-A and Subtask2-B:
---------------------------------------------------
We provide Monolingual dialect and MSA data as follows:
(1) NADI2023_Subtask2_MONO_DA.tsv, which a part of Subtask1 TRAIN data:
- The first column (#1_id) contains an ID representing the data point/tweet.
- The second column (#2_content) contains the content of tweet. We convert user mention and hyperlinks to `USER' and `URL' strings, respectively.
- The third column (#3_label) contains gold label of the tweet at country-level. 
(2) NADI2023_Subtask2_MONO_MSA.tsv:
- The first column (#1_id) contains an ID representing the data point.
- The second column (#2_sourcs_ar) contains the MSA text. 

=================
Sharing NADI Data
=================
Since we are sharing the actual tweets, and as an additional measure to protect Twitter user privacy, we ask that participants not share the distributed data outside their labs nor publish these tweets publicly. Any requests for use of the data outside the shared task can be directed to organizers and will only be accommodated after the shared task submission deadline.

#### File Statistics

Below, we present more details about the contents of the train and development files.

(1) NADI2023_Subtask1_TRAIN.tsv and NADI2023_Subtask1_DEV.tsv contain 18,000 and 1,800 tweets, respectively.

(2) NADI2023_Subtask2A_DEV.tsv and NADI2023_Subtask2B_DEV.tsv contain 200 data point for each one.

(3) NADI2023_Subtask2_MONO_DA.tsv and NADI2023_Subtask2_MONO_MSA.tsv contain  4,000 and 20,029 data point respectively. 


Shared Task Metrics and Restrictions:
-------------------------------------
- Macro-Averaged F-score will be the official metric for subtask 1 (dialect ID)
- Bleu score will be the official metric for subtask 2A and 2B (MT).

The evaluation of shared tasks will be hosted through CODALAB. Teams will be provided with a CODALAB link for each shared task.
CODALAB link for NADI Shared Task Subtask 1: https://codalab.lisn.upsaclay.fr/competitions/14449
CODALAB link for NADI Shared Task Subtask 2A: https://codalab.lisn.upsaclay.fr/competitions/14450
CODALAB link for NADI Shared Task Subtask 2B: https://codalab.lisn.upsaclay.fr/competitions/14451

IMPORTANT: Participants are NOT allowed to use **NADI2023_Subtask1_DEV.tsv**, **NADI2022_Subtask2A_DEV.tsv** or **NADI2022_Subtask2B_DEV.tsv** for training purposes. Participants must report the performance of their best system on both DEV *and* TEST sets in their Shared Task system description paper.

IMPORTANT: Participants can only use the official TRAIN sets provided by NADI-2023.

Participants are NOT allowed to use any additional tweets, nor are they allowed to use outside information.
Specifically -- participants should not use meta data from Twitter about the users or the tweets, e.g., geo-location data.

External manually labelled data sets are *NOT* allowed.

Shared Task Baselines:
----------------------
Baselines for the various sub-tasks will be available on the shared task website after TEST data release.

Please check the website and include the respective baseline for each sub-task in your description paper.

-------------------------------------
NADI2023-Twitter-Corpus-License.txt contains the license for using
this data.

Scoring scripts
-------------------------------------
./Subtask_1/NADI2022-ST1-Scorer.py is a python script for ** Subtask 1 ** that takes in two text files containing true labels and predicted labels and will output accuracy, macro F1 score, precision, and recall. Note that the official metric for subtask 1 is F1 score.

./Subtask_2/NADI2022-ST2-Scorer.py is a python script for ** Subtask 2A and 2B ** that takes in two text files containing GOLD target text and generated text and will output bleu scores for represented dialect and overall score. 

Please read more descriptions of NADI2021-ST1-Scorer.py and NADI2022-ST2-Scorer.py below.

=================================================================
./Subtask_1/NADI2022-ST1-Scorer.py and Submission samples
=================================================================
We provide a sample of gold file and a submission sample file for Subtask 1. 

For example:
`./Subtask_1/subtask1_dev_GOLD.txt' is the gold label file of Dev set of subtask 1. 

The file `./Subtask_1/UBC_subtask1_dev_1.zip' is the zip file of my first submission.
This zip file contains only one txt file: `UBC_subtask1_dev_1.txt'. 
Unzipping `UBC_subtask1_dev_1.zip', you can get `UBC_subtask1_dev_1.txt' where each line is a label string. 

`subtask1_dev_GOLD.txt' and `UBC_subtask1_dev_1.txt' can be used with the NADI2022-ST1-Scorer.py.
NADI2022-ST1-Scorer.py evaluate the performance of submssion. 

Please make sure to have scikit-learn library installed.

Usage of the scorer:

    python3 NADI2021-ST1-Scorer.py  <gold-file> <pred-file>


In the dataset directory, there are example gold and prediction files. If they are used with the scorer, they should produce the following results:

python3 ./Subtask1/NADI2022-ST1-Scorer.py ./Subtask1/subtask1_dev_GOLD.txt ./Subtask1/UBC_subtask1_dev_1.txt 

OVERALL SCORES:
MACRO AVERAGE PRECISION SCORE: 5.46 %
MACRO AVERAGE RECALL SCORE: 5.46 %
MACRO AVERAGE F1 SCORE: 5.46 %
OVERALL ACCURACY: 10.98 %

=================================================================
./Subtask_2/NADI2022-ST2-Scorer.py and Submission samples
=================================================================
We provide a sample of gold file and a submission sample file for Subtask 2. 

For example:
`./Subtask_2/subtask2_dev_GOLD.txt' is the gold label file of Dev set of subtask 2. 

The file `./Subtask_2/UBC_subtask2_dev_1.zip' is the zip file of my first submission.
This zip file contains only one txt file: `UBC_subtask2_dev_1.txt'. 
Unzipping `UBC_subtask2_dev_1.zip', you can get `UBC_subtask2_dev_1.txt' where each line is a label string. 

`subtask2_dev_GOLD.txt' and `UBC_subtask2_dev_1.txt' can be used with the NADI2022-ST2-Scorer.py.
NADI2022-ST2-Scorer.py evaluate the performance of submssion. 

Usage of the scorer:

    python3 NADI2022-ST1-Scorer.py  <gold-file> <pred-file>


In the dataset directory, there are example gold and prediction files. If they are used with the scorer, they should produce the following results:

python3 ./Subtask2/NADI2022-ST2-Scorer.py ./Subtask2/subtask2_dev_GOLD.txt ./Subtask2/UBC_subtask2_dev_1.txt 

OVERALL SCORES:
MACRO AVERAGE PRECISION SCORE: 36.91 %
MACRO AVERAGE RECALL SCORE: 36.91 %
MACRO F1-PN SCORE: 42.09 %
OVERALL ACCURACY: 38.60 %


=================================================================
Acknowledgements
=================================================================
The scoring script is borrowed from the MADAR 2019 Shared Task (Bouamor et al., 2019). The current README and the release package also follows and borrows from the MADAR Shared Task and NADI 2020, 2021, and 2022 releases. 

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
Copyright (c) 2023 The University of British Columbia, Canada; 
Carnegie Mellon University Qatar; New York University Abu Dhabi.
All rights reserved.
================================================================
