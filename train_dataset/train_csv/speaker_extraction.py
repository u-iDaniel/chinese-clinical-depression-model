import pandas as pd
import os

def speaker_extraction(file: str, speaker: int) -> pd.DataFrame:
    """
    params:
        file - the file to extract the speaker from
        speaker - the speaker to extract {1: doctor, 2: patient}
    Returns a dataframe with the doctor/patient speaking only
    """
    if speaker not in [1, 2]:
        raise ValueError("Speaker must be 1 or 2")
    if isinstance(file, str) == False:
        raise ValueError("File must be a string")
    df = pd.read_csv(file)
    df = df.loc[df['speaker'] == speaker]
    return df

def sentence_extraction(df):
    """
    params:
        df - dataframe containing doctor/patient only 
    Returns a dataframe with only the users sentences
    """
    sentence_df = df.copy()
    sentence_df = sentence_df.drop_duplicates(subset='bg', keep='first')
    return sentence_df

def qa_extraction(sentence_df: pd.DataFrame) -> list[tuple[str, str]]:
    """
    params:
        sentence_df - dataframe containing only the users' sentences  
    Iterate through the dataframe and extract the question and answer pairs
    Returns: a list of tuples containing the question and answer pairs
        [(question, answer), (question, answer), ...]]
    """
    qa_pairs = []
    current_speaker = 1
    question, answer = "", ""
    for index, row in sentence_df.iterrows():
        if row['speaker'] != current_speaker and question and answer:
            qa_pairs.append((question, answer))
            question, answer = "", ""
        
        if row['speaker'] == 1:
            question += row['onebest']
        elif row['speaker'] == 2:
            answer += row['onebest']
        current_speaker = row['speaker']
    return qa_pairs

def concat_to_str(sentence_df: pd.DataFrame) -> str:
    """
    params:
        sentence_df - dataframe containing users' sentences
    Returns a concatenated string of all the users' sentences
    """
    return ''.join(sentence_df['onebest'].tolist())


def write_files(string: str, filename: str, path: str = '') -> None:
    """
    params:
        string - string to print
        filename - name of the file to create
        path - path to directory to create file in
    Creates a .txt file with the string within path directory
    """
    if path and not os.path.exists(path):
        os.makedirs(path)
    with open(os.path.join(path, filename), 'w', encoding='utf-8') as f:
        f.write(string)

def append_files(string: str, filename: str, path: str = '') -> None:
    """
    params:
        string - string to print
        filename - name of the file to create
        path - path to directory to create file in
    Appends the string to the end of the .txt file within path directory
    """
    if path and not os.path.exists(path):
        os.makedirs(path)
    with open(os.path.join(path, filename), 'a', encoding='utf-8') as f:
        f.write(string)
    

if __name__ == '__main__':
    # Creating QA txt files
    file_names = os.listdir()
    file_names = [file for file in file_names if file.endswith('.csv')]
    for file in file_names:
        df = pd.read_csv(file)
        sentence_df = sentence_extraction(df)
        qa_pairs = qa_extraction(sentence_df)
        for question, answer in qa_pairs:
            string = f"Question: {question}\nAnswer: {answer}\n"
            append_files(string, file.replace('.csv', '.txt'), '../question_and_answer_txt_files')
        
