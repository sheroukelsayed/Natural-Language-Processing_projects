================================================================
                    NADI 2022: The Third Nuanced Arabic Dialect Identification Shared Task

=================================================================
Summary
=================================================================

Arabic has a widely varying collection of dialects. Many of these dialects remain under-studied due to the rarity of resources. The goal of the Nuanced Arabic Dialect Identification (NADI) shared task series is to alleviate this bottleneck by providing datasets and modeling opportunities for participants to carry out dialect identification. Dialect identification is the task of automatically detecting the source variety of a given text or speech segment. In addition to nuanced dialect identification at the country level, NADI 2022 also offers a new subtask focused on country-level sentiment analysis. While we invite participation in either of the two subtasks, we hope that teams will submit systems to both tasks (i.e., participate in the two tasks rather than only one task). By offering two subtasks, we hope to receive systems that exploit diverse machine learning architectures. This could include multi-task learning systems as well as sequence-to-sequence architectures in a single model such as the text-to-text Transformer. Other approaches could also be possible. We introduce the two subtasks next.

=================================================================
NADI 2022 Shared Task
=================================================================

Description of Task:
--------------------

This shared task targets country-level dialects and sentiment identification for dialectical Arabic. The subtasks are:

# Subtask 1: Country-level dialect identification. In this subtask, we provide a Twitter training dataset that covers 18 dialects (total of ~20K tweets, the same as NADI 2021). The final evaluation will be on two new test sets: the first test set (TEST-A) covers 18 country-level dialects, whereas the second test set (TEST-B) covers k country-level dialects, where we keep k unknown. The average score between the two test sets is the subtask score.  

# Subtask 2: Sentiment analysis of country-level Arabic. A total of 5,000 tweets covering ten Arab countries (involving both MSA and dialects) manually labeled with tags from the set {positive, negative, neutral}. The dataset is split into 1,500 tweets for training (TRAIN), 500 tweets for development (DEV), and 3,000 tweets for test (TEST). We intentionally provide a small training dataset to encourage various approaches including `few-shot’.

** Labeled Data **
For subtask 1, we provide Train and Dev data in two tsv files respectively:
(1) ./Subtask_1/NADI2022_Subtask1_TRAIN.tsv
(2) ./Subtask_1/NADI2022_Subtask1_DEV.tsv

For subtask 2, we provide Train and Dev data data are in two tsv files respectively:
(1) ./Subtask_2/NADI2022_Subtask2_TRAIN.tsv
(2) ./Subtask_2/NADI2022_Subtask2_DEV.tsv

These four files have the same structure.

We provide the following information:

- The first column (#1_id) contains an ID representing the data point/tweet.

- The second column (#2_content) contains the content of tweet. We convert user mention and hyperlinks to `USER' and `URL' strings, respectively.

- The third column (#3_label) contains gold label of the tweet. 
  - For subtask_1, labels are country-level dialects.
  - For subtask_2, labels are sentiments.

** Unlabeled Data **
Participants will also be provided with an additional 10M unlabeled tweets that can be used in developing their systems for either or both of the subtasks. This is the same unlabeled data as NADI 2021. 

(1) NADI2022-unlabeled_10M.tsv

In the NADI2022-unlabeled_10M.tsv, we only provide the actual ID of tweets. Participants need to use the Twitter API to collect the texts of these tweets. We provide a script for collecting the tweets in the accompanying distribution (described later in this README).

- The first column (#1 tweet_ID) contains ID of tweet.

=================
Sharing NADI Data
=================
Since we are sharing the actual tweets, and as an additional measure to protect Twitter user privacy, we ask that participants not share the distributed data outside their labs nor publish these tweets publicly. Any requests for use of the data outside the shared task can be directed to organizers and will only be accommodated after the shared task submission deadline.

#### File Statistics

Below, we present more details about the contents of the train and development files.

(1) NADI2022_Subtask1_TRAIN.tsv and NADI2022_Subtask1_DEV.tsv contain 20,398 and 4,871 tweets, respectively.

(2) NADI2022_Subtask2_TRAIN.tsv and NADI2022_Subtask2_DEV.tsv contain 1,500 and 500 tweets, respectively.

Shared Task Metrics and Restrictions:
-------------------------------------
- Macro-Averaged F-score will be the official metric for subtask 1 (dialect ID)
- Macro-F1-PN score over the positive and negative classes only while neglecting the neutral class will be the official metric for subtask 2 (sentiment).

The evaluation of shared tasks will be hosted through CODALAB. Teams will be provided with a CODALAB link for each shared task.
CODALAB link for NADI Shared Task Subtask 1: https://codalab.lisn.upsaclay.fr/competitions/6514?secret_key=ce3736d6-03f2-4454-977c-1c88b7ef4d53
CODALAB link for NADI Shared Task Subtask 2: https://codalab.lisn.upsaclay.fr/competitions/6522?secret_key=86ae5871-9b85-4b1c-8e3d-129cd06be118

IMPORTANT: Participants are NOT allowed to use **NADI2022_Subtask1_DEV.tsv** or **NADI2022_Subtask2_DEV.tsv** for training purposes. Participants must report the performance of their best system on both DEV *and* TEST sets in their Shared Task system description paper.

IMPORTANT: Participants can only use the official TRAIN sets provided by NADI-2022.

Participants are NOT allowed to use any additional tweets, nor are they allowed to use outside information.
Specifically -- participants should not use meta data from Twitter about the users or the tweets, e.g., geo-location data.

External manually labelled data sets are *NOT* allowed.

Shared Task Baselines:
----------------------
Baselines for the various sub-tasks will be available on the shared task website after TEST data release.

Please check the website and include the respective baseline for each sub-task in your description paper.

-------------------------------------
NADI2022-Twitter-Corpus-License.txt contains the license for using
this data.

Scoring scripts
-------------------------------------
./Subtask_1/NADI2022-ST1-Scorer.py is a python script for ** Subtask 1 ** that takes in two text files containing true labels and predicted labels and will output accuracy, macro F1 score, precision, and recall. Note that the official metric for subtask 1 is F1 score.

./Subtask_2/NADI2022-ST2-Scorer.py is a python script for ** Subtask 2 ** that takes in two text files containing true labels and predicted labels and will output accuracy, macro F1-PN score, precision, and recall. Note that the official metric for subtask 2 is macro F1-PN score (i.e., F1 score over the positive and negative classes only while neglecting the neutral class).

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
NADI2022-Obtain-Tweets.py:
=================================================================

NADI2022-Obtain-Tweets.py is a python script that will take in
the NADI2021-unlabeled_10M.tsv file and append a column containing
actual tweet texts corresponding to tweet IDs in the file.

VERY-IMPORTANT (1):  Please make sure to have unicodecsv and tweepy
libraries installed. Make the following calls in terminal:

     pip install unicodecsv
     pip install tweepy

VERY-IMPORTANT (2): Use of this script will require a Twitter
developer's account and corresponding authentication credentials.
The authentication credentials have to be provided in lines
81-84 of the code.

Creating a developer's account and obtaining credentials:
To create a Twitter developer's account, login to Twitter and
go to https://developer.twitter.com/en/apply-for-access.html.
After applying for the developer's account, you will have to wait for the
application to be approved. Twitter may contact you for additional
information about your usage. Please make sure to check your email.

Once the developer's account is created, you will need to create an app.
To create an app, go to apps under the dropdown at your username (upper
right corner). You can now click "create an app."

After an app is created, go to your app details and go to the
"keys and tokens" tab. You will be able to generate following
authentication credentials required for the script:

(1) consumer key
(2) consumer secret
(3) access token
(4) access secret


Usage of the script:

    python3 NADI2022-Obtain-Tweets.py  <input_file> <output_file>

    The input file must be in the same format as the
    NADI2022-unlabeled_10M.tsv

    The output file is the name of the file where the obtained tweets
    will be appended. If any tweet is unavailable, it will write
    <UNAVAILABLE> for that tweet.

Example usage:

    python3 NADI2022-Obtain-Tweets.py NADI2021-unlabeled_10M.tsv NADI2022-10M-full-tweets.tsv

Running the following command will produce the file NADI2022-10M-full-tweets.tsv that
contains obtained tweets appended in the last column along with
the tweet IDs from NADI2022-unlabeled_10M.tsv. 

NOTE: NADI2022-unlabeled_10M.tsv contains 10 millions IDs of tweets. 


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
