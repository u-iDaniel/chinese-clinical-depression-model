# Note:
- All transcipts are unfortunately in Chinese
- Value and Speaker fields may contain errors due to lack of pause between doctor and patient
- **Most of these descriptions are our best guesses as we don't know how the original transcription API labeled everything**

## Header Descriptions
* bg: timestamp of beginning of sentence (in miliseconds)
* ed: timestamp of end of sentence (in miliseconds)
* onebest: the sentence content
* si: sentence index (batch size seems to be around 15 tokens and can contain multiple "onebests" per index), * starts at 0
* speaker: 1 for doctor, 2 for patient

* wordsName: word token (can be up to 3 characters)
    * Use these values as input for the frequency vectorizer
* wc: word content, a score that ranges from 0-1 float value. The more meaningful the word the higher wc value it has. 
    * Punctuations have a value of 0.0000
    * Filler words have a value greater than 0.0000 but lower than 1.0000
    * Meaningful words have a value very close to or exactly 1.0000 
* wordBg: no clue, might have something to do with miliseconds of time passed relative to the start of the sentence being spoken
* wordEd: same as wordBg except now its the timestamp at the end of the word
* wp: 
    * s - start of sentence
    * n - regular word (i.e. words that are not described by the other identifiers listed in `wp`)
    * p - punctuation 
    * g - end of sentence