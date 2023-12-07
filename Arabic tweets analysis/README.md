# Arabic tweets for emotion classification: positive, negative, neutral
NLP projects 

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
