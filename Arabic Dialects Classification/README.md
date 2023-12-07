
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

Our experiments aimed to enhance Arabic Dialect Identification through a comprehensive exploration of various models and techniques. We began with baseline models, such as MARBERT and MARBERTv2, each employed with adapters and different learning rates. We experimented with concatenating specific layers and explored averaging layers for both models.
 To enhance these models, we introduced convolutional filters and max pooling, replacing the classifier with Bidirectional LSTM (BILSTM), and combining BILSTM with additional convolutional layers. We extended our exploration with multiple convolutional filters of varying kernel sizes, followed by max pooling. Finally, we created ensemble models using a voting approach and an average ensemble.
 For detailed results and analysis, please refer to the full paper [here](https://aclanthology.org/2023.arabicnlp-1.66/).

