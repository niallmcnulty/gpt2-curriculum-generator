import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import subprocess
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK data
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

def rtf_to_text(rtf_path):
    # Use textutil (macOS command) to convert RTF to plain text
    result = subprocess.run(['textutil', '-convert', 'txt', '-stdout', rtf_path], 
                            capture_output=True, text=True)
    return result.stdout

def clean_text(text):
    # Convert to lowercase
    text = text.lower()
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Remove special characters and digits (modify as needed)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    return text

def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word not in stop_words]
    return ' '.join(filtered_text)

def improve_formatting(text):
    # Capitalize the first letter of each sentence
    sentences = sent_tokenize(text)
    capitalized_sentences = [s.capitalize() for s in sentences]
    return ' '.join(capitalized_sentences)

def lemmatize_text(text):
    lemmatizer = WordNetLemmatizer()
    word_tokens = word_tokenize(text)
    lemmatized_text = [lemmatizer.lemmatize(word) for word in word_tokens]
    return ' '.join(lemmatized_text)

def process_rtf_file(input_path, output_path):
    # Convert RTF to plain text
    plain_text = rtf_to_text(input_path)
    
    # Clean the text
    cleaned_text = clean_text(plain_text)
    
    # Remove stopwords (optional, comment out if you want to keep all words)
    # cleaned_text = remove_stopwords(cleaned_text)
    
    # Improve formatting
    improved_text = improve_formatting(cleaned_text)
    
    # Lemmatize the text (optional)
    # cleaned_text = lemmatize_text(cleaned_text)
    
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(improved_text)

    print(f"RTF has been converted to plain text, cleaned, and improved. Saved to {output_path}")

# Specify the paths
input_file = "dataset/FP.rtf"  # Make sure this matches your RTF file name
output_file = "dataset/FP_text_cleaned.txt"

# Process the RTF file
process_rtf_file(input_file, output_file)
