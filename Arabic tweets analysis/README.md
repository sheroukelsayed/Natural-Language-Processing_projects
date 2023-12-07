# Arabic tweets for emotion classification: positive, negative, neutral
NLP projects competation provided by NADIshared task 2022
Sentiment analysis of country-level Arabic. A total of 5,000 tweets covering ten Arab countries (involving both MSA and dialects) manually labeled with tags from the set {positive, negative, neutral}. The dataset is split into 1,500 tweets for training (TRAIN), 500 tweets for development (DEV), and 3,000 tweets for test (TEST). We intentionally provide a small training dataset to encourage various approaches including `few-shot
My_team (ISL-aast) acheive 7 ISL_AAST f1_score of (70.55%) accuracy of( 64.97%) 

 1) Pre-processing steps: 

The provided code is a Python script for preprocessing Arabic text data and performing sentiment analysis. Below are the high-level steps and the types of data preprocessing performed:

1. Mount Google Drive:
   - The script mounts Google Drive to the Colab environment, allowing access to files stored in Google Drive.

2. Install Required Libraries:
   - The script installs the `ktrain` library using the `!pip3 install ktrain` and the `pillow` library using `!pip install pillow` commands.

3. Import Libraries:
   - Import necessary Python libraries, including TensorFlow, Keras, pandas, NLTK, and others.

4. Define Functions:
   - Several functions are defined, such as `remove_diacritics`, `convert_emoji`, `clean_text`, and `process_text`. These functions handle tasks like removing diacritics, converting emojis to Arabic meanings, and cleaning and processing text.

5. Download NLTK Resources:
   - Download Arabic stopwords and punkt resources from NLTK.

6. Define Arabic Punctuations:
   - Define a list of Arabic punctuations.

7. Read Data:
   - Read training, development (DEV), and test data from TSV files into Pandas DataFrames.

8. Data Preprocessing:
   - Handle diacritics removal, emoji conversion, and text cleaning using the defined functions.
   - Apply preprocessing steps to the tweet content in the training, DEV, and test datasets.
   - Remove stopwords from the text.
   - Map string labels ('neg', 'neut', 'pos') to numerical symbols (0, 1, 2).
   - Split the training data into training and testing sets using the `train_test_split` function.
   - Compute class weights for imbalanced classes using the `compute_class_weight` function.

9. Save Processed Data:
   - Save the preprocessed data into CSV files for further use.

For training: 
The provided code incorporates Transformer adapters, a powerful mechanism for enhancing pre-trained models with task-specific knowledge. Two specific types of adapter compositions, Fusion and Stack, are employed to enrich the transformer models:

Adapter in Transformers:
An adapter in a Transformer model serves as a modular extension that can be added to pre-trained models to enable them to perform new tasks without extensive retraining. Adapters provide a flexible way to augment a model's capabilities for various downstream tasks by adding task-specific parameters and weights. They allow the model to adapt to specific domains or languages without forgetting its original pre-training.

Used Adapter Compositions:

1. Fusion Adapters:
   - Fusion adapters, illustrated by the `ac.Fuse` operation, combine information from multiple pre-trained adapters, such as "multinli," "qqp," "qnli," and "dialect-arabic." This fusion approach enables the model to integrate knowledge from diverse sources, making it more adept at handling a variety of tasks simultaneously.

2. Stacked Adapters:
   - Stacked adapters, demonstrated by the `ac.Stack` operation, involve combining multiple adapters in a layered manner. In the code, stacking is applied to model2, where three adapters, "cls-arabic_marabert1," "cls-arabic_marabert2," and "cls-arabic_marabert3," are stacked together. Stacking allows the model to capture hierarchical and composite features from different adapter representations, enhancing its ability to understand complex patterns.

These adapter compositions showcase the flexibility and versatility of the transformer model. By incorporating Fusion and Stack adapters, the model gains the capacity to leverage knowledge from various sources and capture intricate patterns in the data, making it adaptable and robust across a spectrum of tasks and domains.

### Part 1: Adapter Implementation and Training

1. Mount Google Drive:
   - Mount Google Drive to access files in the Colab environment.

2. Install Dependencies:
   - Install necessary packages such as `adapter-transformers`, `datasets`, and other required libraries.

3. Load Datasets:
   - Load training datasets (`traindataset1`, `traindataset2`, `traindataset3`) using the `datasets` library.
   - Load development dataset (`DEVdataset`) and split it into three subsets (`DEVdataset1`, `DEVdataset2`, `DEVdataset3`).

4. Tokenization:
   - Use different pre-trained tokenizers (`tokenizer`, `tokenizer2`, `tokenizer3`, `tokenizer4`) for encoding text data.

5. Define Encoding Functions:
   - Create functions (`encode`, `encode2`, `encode3`, `encode4`) to encode text examples using corresponding tokenizers.

6. Map Encoding Functions to Datasets:
   - Apply the encoding functions to the datasets (`traindataset1`, `traindataset2`, `traindataset3`, `DEVdataset1`, `DEVdataset2`, `DEVdataset3`).

7. Adapter Configuration and Training:
   - Configure adapter models (`model1`, `model2`, `model3`, `model4`) with different adapter configurations.
   - Add adapters to the models and train them using the `AdapterTrainer`.
   - Evaluate the trained models on development datasets.

8. Save Trained Adapters:
   - Save the trained adapters to specific directories for future use.

### Part 2: Ensemble and Evaluation

1. Combine Predictions:
   - Use the trained models to make predictions on development (`DEVdataset1`, `DEVdataset2`, `DEVdataset3`) and test datasets (`testdataset1`).
   - Combine predictions from multiple models (`output1`, `output2`, `output3`, `output_test1`, `output_test2`, `output_test3`).

2. Ensemble Prediction:
   - Sum or aggregate predictions from different models to create ensemble predictions.

3. Extract Labels and Save Ensemble Predictions:
   - Extract labels from the ensemble predictions.
   - Save the ensemble predictions to a text file or any desired output format.

4. Final Evaluation and Save Results:
   - Evaluate the ensemble predictions on the development dataset.
   - Save the results, such as accuracy, in a file or print them for analysis.

If anyone want use this dataset please cite:
@inproceedings{abdul-mageed-etal-2022-nadi,
    title = "{NADI} 2022: The Third Nuanced {A}rabic Dialect Identification Shared Task",
    author = "Abdul-Mageed, Muhammad  and
      Zhang, Chiyu  and
      Elmadany, AbdelRahim  and
      Bouamor, Houda  and
      Habash, Nizar",
    editor = "Bouamor, Houda  and
      Al-Khalifa, Hend  and
      Darwish, Kareem  and
      Rambow, Owen  and
      Bougares, Fethi  and
      Abdelali, Ahmed  and
      Tomeh, Nadi  and
      Khalifa, Salam  and
      Zaghouani, Wajdi",
    booktitle = "Proceedings of the The Seventh Arabic Natural Language Processing Workshop (WANLP)",
    month = dec,
    year = "2022",
    address = "Abu Dhabi, United Arab Emirates (Hybrid)",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.wanlp-1.9",
    doi = "10.18653/v1/2022.wanlp-1.9",
    pages = "85--97",
    abstract = "We describe the findings of the third Nuanced Arabic Dialect Identification Shared Task (NADI 2022). NADI aims at advancing state-of-the-art Arabic NLP, including Arabic dialects. It does so by affording diverse datasets and modeling opportunities in a standardized context where meaningful comparisons between models and approaches are possible. NADI 2022 targeted both dialect identification (Subtask 1) and dialectal sentiment analysis (Subtask 2) at the country level. A total of 41 unique teams registered for the shared task, of whom 21 teams have participated (with 105 valid submissions). Among these, 19 teams participated in Subtask 1, and 10 participated in Subtask 2. The winning team achieved F1=27.06 on Subtask 1 and F1=75.16 on Subtask 2, reflecting that both subtasks remain challenging and motivating future work in this area. We describe the methods employed by the participating teams and offer an outlook for NADI.",
}
