import re
import os

def read_text_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        print(f"Successfully read {len(content)} characters from {file_path}")
        return content
    except Exception as e:
        print(f"Error reading file {file_path}: {str(e)}")
        return ""

def split_into_chunks(text, chunk_size=500):
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    print(f"Split text into {len(chunks)} chunks")
    return chunks

def save_chunks_to_file(chunks, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            for chunk in chunks:
                f.write(chunk + "\n\n")  # Add two newlines between chunks
        print(f"Successfully wrote {len(chunks)} chunks to {file_path}")
    except Exception as e:
        print(f"Error writing to file {file_path}: {str(e)}")

def prepare_data_for_model(input_file, output_dir):
    # Read the cleaned text file
    text = read_text_file(input_file)
    
    if not text:
        print("No text read from input file. Exiting.")
        return
    
    # Split the text into chunks
    chunks = split_into_chunks(text)
    
    if not chunks:
        print("No chunks created. Exiting.")
        return
    
    # Force split chunks equally between train and validation
    mid = len(chunks) // 2
    train_chunks = chunks[:mid]
    val_chunks = chunks[mid:]
    
    print(f"Number of train chunks: {len(train_chunks)}")
    print(f"Number of validation chunks: {len(val_chunks)}")
    
    # Save the chunks to text files
    train_file = os.path.join(output_dir, "train_data.txt")
    val_file = os.path.join(output_dir, "val_data.txt")
    
    save_chunks_to_file(train_chunks, train_file)
    save_chunks_to_file(val_chunks, val_file)
    
    # Verify file sizes after writing
    print(f"Train file size: {os.path.getsize(train_file)} bytes")
    print(f"Validation file size: {os.path.getsize(val_file)} bytes")

# Specify the paths
input_file = "dataset/FP_text_cleaned.txt"
output_dir = "dataset"

# Prepare the data
prepare_data_for_model(input_file, output_dir)

# Print current working directory
print(f"Current working directory: {os.getcwd()}")
