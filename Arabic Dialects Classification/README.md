
ISL-AAST at NADI 2023 shared task: Enhancing Arabic Dialect Identification in the Era of Globalization and Technological Progress

# Arabic Dialect Identification at NADI 2023 Shared Task

## Abstract

Arabic dialects play a crucial role globally due to their significance and the extensive number of Arabic speakers. 
However, the impact of technological progress and globalization on these dialects introduces challenges for sentiment analysis. 
This study, conducted as part of the Nuanced Arabic Dialect Identification (NADI) shared task competition, categorizes dialects among 18 countries. 
We employ the MARABERT and MARABERT v2 models, utilizing various methodologies, including a feature extraction process. 
The most effective model involves averaging and concatenating the hidden layers of MARABERT v2, followed by feeding the output into convolutional layers.
 The ensemble method further enhances the model's performance, securing the 6th position in the First subtask with an F1 score of 83.73%.

## Paper

The paper associated with this project can be found in the [ACL Anthology](https://aclanthology.org/2023.arabicnlp-1.66/).


## Citation

If you find this work helpful, please consider citing our paper:

```
@inproceedings{adel2023isl,
  title={ISL-AAST at NADI 2023 shared task: Enhancing Arabic Dialect Identification in the Era of Globalization and Technological Progress},
  author={Adel, Shorouk and Elmadany, Noureldin},
  booktitle={Proceedings of ArabicNLP 2023},
  pages={631--636},
  year={2023}
}
```

# Experiments Summary

We conducted a series of experiments to enhance Arabic Dialect Identification using various models and techniques. Here's a summary of the experiments without including specific results:

## Baseline Models

### Exp.1: MARBERT + Adapter (LR=2e-5)
- Applied MARBERT with adapter, using a learning rate of 2e-5.

### Exp.2: MARBERTv2 + Adapter (LR=2e-5)
- Utilized MARBERTv2 with adapter, with a learning rate of 2e-5.

### Exp.3: MARBERT (LR=2e-5)
- Employed MARBERT with a learning rate of 2e-5.

### Exp.4: MARBERTv2 (LR=2e-5)
- Applied MARBERTv2 with a learning rate of 2e-5.

### Exp.5: MARBERT (Last 4 Layers Concatenation) (LR=2e-5)
- Concatenated the output of the last 4 layers of MARBERT with a learning rate of 2e-5.

### Exp.6: MARBERTv2 (Last 4 Layers Concatenation) (LR=2e-5)
- Concatenated the output of the last 4 layers of MARBERTv2 with a learning rate of 2e-5.

### Exp.7: MARBERT (Average Layers 4-7 and Concatenation with Last 4 Layers) (LR=2e-5)
- Averaged layers 4-7 and concatenated the output with the last 4 layers of MARBERT with a learning rate of 2e-5.

### Exp.8: MARBERTv2 (Average Layers 4-7 and Concatenation with Last 4 Layers) (LR=2e-5)
- Averaged layers 4-7 and concatenated the output with the last 4 layers of MARBERTv2 with a learning rate of 2e-5.

## Enhanced Models

### Exp.9: Repeat Exp.7 + Utilizing 1 Conv. Filter (Kernel Size=5) + Max Pooling (LR=2e-5)
- Repeated Exp.7 and added a convolutional filter with a kernel size of 5 and max pooling, using a learning rate of 2e-5.

### Exp.10: Repeat Exp.8 + Utilizing 1 Conv. Filter (Kernel Size=5) + Max Pooling (LR=2e-5)
- Repeated Exp.8 and added a convolutional filter with a kernel size of 5 and max pooling, using a learning rate of 2e-5.

### Exp.11: Repeat Exp.7 + BILSTM as Classifier (LR=2e-5)
- Repeated Exp.7 and replaced the classifier with Bidirectional LSTM (BILSTM), using a learning rate of 2e-5.

### Exp.12: Repeat Exp.7 + BILSTM + 1 Conv. Filter (Kernel Size=5) + Max Pooling (LR=2e-5)
- Repeated Exp.7, added BILSTM, and further included a convolutional filter with a kernel size of 5 and max pooling, using a learning rate of 2e-5.

### Exp.13: Repeat Exp.7 + 3 Conv. Filters (Kernel Sizes 5, 4, 3) + Max Pooling (LR=1e-5)
- Repeated Exp.7 and introduced three convolutional filters with kernel sizes 5, 4, and 3, followed by max pooling, using a learning rate of 1e-5.

### Exp.14: Repeat Exp.7 + 3 Conv. Filters (Kernel Sizes 10, 8, 6) + Max Pooling (LR=1e-5)
- Repeated Exp.7 and included three convolutional filters with kernel sizes 10, 8, and 6, followed by max pooling, using a learning rate of 1e-5.

### Exp.15: Repeat Exp.7 + 3 Conv. Filters (Kernel Sizes 7, 7, 7) + Max Pooling (LR=1e-5)
- Repeated Exp.7 and incorporated three convolutional filters with kernel sizes 7, 7, and 7, followed by max pooling, using a learning rate of 1e-5.

### Exp.16: Repeat Exp.7 + 3 Conv. Filters (Kernel Sizes 12, 10, 8) + Max Pooling (LR=1e-5)
- Repeated Exp.7 and added three convolutional filters with kernel sizes 12, 10, and 8, followed by max pooling, using a learning rate of 1e-5.

## Ensemble Models

### Exp.17: Voting Ensemble (Exp. 3-16)
- Created a voting ensemble using the results from Experiments 3 to 16.

### Exp.18: Average Ensemble (Exp. 3-16)
- Constructed an average ensemble using the results from Experiments 3 to 16.

Please refer to the full paper for detailed results and analysis: [Paper Link](https://aclanthology.org/2023.arabicnlp-1.66/).
