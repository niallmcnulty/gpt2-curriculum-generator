# GPT-2 Curriculum Content Generator

## Project Overview

This project is a GPT-2 based curriculum content generator, designed to assist educators in creating lesson plans and educational materials. It uses natural language processing and machine learning techniques to process educational texts and generate curriculum-related content.

## Features

- OCR and text extraction from PDF documents
- Text cleaning and preprocessing
- Fine-tuning GPT-2 model on curriculum data
- Generating lesson plans based on subject and grade level

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/gpt2-curriculum-generator.git
   cd gpt2-curriculum-generator
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

   Note: If you're using a GPU, you might need to install a specific version of PyTorch. Please refer to the [PyTorch installation guide](https://pytorch.org/get-started/locally/) for more information.

## Usage

### Data Preparation

1. Place your PDF documents in the `dataset` folder.
2. Run the OCR and text extraction script:
   ```
   python ocr-pdf-to-text.py
   ```
3. Clean the extracted text:
   ```
   python text-cleaner.py
   ```

### Model Fine-tuning

To fine-tune the GPT-2 model on your curriculum data:

```
python gpt2-ft.py
```

This process may take several hours depending on your hardware and the amount of data.

### Generating Lesson Plans

To generate lesson plans using the fine-tuned model:

```
python gpt2-curriculum-generator.py
```

Follow the prompts to specify the subject and grade level for the lesson plan.

## Project Structure

- `data-preparation.py`: Prepares data for model training
- `ocr-pdf-to-text.py`: Extracts text from PDF files
- `text-cleaner.py`: Cleans and preprocesses extracted text
- `gpt2-ft.py`: Fine-tunes the GPT-2 model
- `gpt2-curriculum-generator.py`: Generates lesson plans using the fine-tuned model
- `dataset/`: Directory for storing input PDFs and processed text files
- `gpt2-curriculum/`: Directory for storing the fine-tuned model

## Configuration

You can modify the training parameters in the `config.yaml` file located in the project root directory.

## Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your proposed changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project uses the [Transformers](https://github.com/huggingface/transformers) library by Hugging Face.
- OCR functionality is provided by [OCRmyPDF](https://github.com/jbarlow83/OCRmyPDF).

## Contact

For any questions or feedback, please open an issue on this GitHub repository.
