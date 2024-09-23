# Chinese Clinical Depression Detecting Models
[IEEEDataport Competition Link](https://ieee-dataport.org/competitions/ieee-biocas2024-grand-challenge-depression-detection) 

[Official Kaggle Competition Link](https://www.kaggle.com/competitions/biocas2024-depression-detection-grand-challenge)

These models were built as part of the BioCAS 2024 Chinese Clinical Depression Detecting Challenge: a challenge aimed at creating models to detect depression in clinical interviews done in a psychiatric hopsital in China. The train and test datasets include MP3 audio files as well as transcription files in JSON (which were later converted into CSV with the help of a script). 



We chose to build two independent models within Kaggle using their TPU VM v3-8 to address each aspect of the challenge, one for the text transcriptions and the other for audio. For the text portion we fine-tuned the [BERT model](https://github.com/google-research/bert) to our dataset. The audio portion was done by an image classifying CNN. More details are provided below. 

A future extension could be to create an ensemble model by combining both models.

# Models

## BERT 
Fine-tuned Chinese [BERT](https://github.com/google-research/bert) model. Only the transcription of the patient dialogue from the doctor and patient interviews are used (*patient_txt_files* directory). The transcript is tokenized before being fed into BERT, producing a vector representation of the entire phrase. These vectors are classified using the sigmoid output function, which indicates the probability that the patient is depressed.

## Image CNN
Classifies Mel-spectrogram representations of audio data. Each audio file is first split into 5-second segments, where each segment is converted into a Mel-spectrogram. The Mel-spectrograms and the labels are fed into a CNN, which performs sentiment analysis on each segment. The predictions for the segments of each audio file are aggregated to produce a final prediction for the entire audio file.

## Relevant papers
[Analysis of Automated Clinical Depression Diagnosis in a Chinese Corpus](https://doi.org/10.1109/TBCAS.2023.3291554) (intro paper to the challenge)

[Prediction of Depression Severity Based on the
Prosodic and Semantic Features With
Bidirectional LSTM and Time Distributed CNN](https://doi.org/10.1109/TAFFC.2022.3154332) (related paper that builds a model for the DAIC-WOZ dataset)