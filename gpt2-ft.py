import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer, GPT2Config
from transformers import Trainer, TrainingArguments
from datasets import load_dataset
from transformers import DataCollatorForLanguageModeling
import yaml

def load_config(config_path):
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

def load_and_tokenize_dataset(file_path, tokenizer):
    def tokenize_function(examples):
        return tokenizer(examples["text"], truncation=True, max_length=512)

    dataset = load_dataset('text', data_files={'train': file_path})
    tokenized_dataset = dataset.map(tokenize_function, batched=True, num_proc=4, remove_columns=["text"])
    
    # Filter out empty examples
    filtered_dataset = tokenized_dataset.filter(lambda example: len(example['input_ids']) > 0)
    
    print(f"Original dataset size: {len(tokenized_dataset)}")
    print(f"Filtered dataset size: {len(filtered_dataset)}")
    
    return filtered_dataset["train"]

def train():
    # Load pre-trained model and tokenizer
    model_name = "gpt2"
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)

    # Set the padding token
    tokenizer.pad_token = tokenizer.eos_token
    model.config.pad_token_id = model.config.eos_token_id

    # Load and preprocess the dataset
    train_dataset = load_and_tokenize_dataset("dataset/train_data.txt", tokenizer)
    val_dataset = load_and_tokenize_dataset("dataset/val_data.txt", tokenizer)

    # Print dataset info
    print(f"Final train dataset size: {len(train_dataset)}")
    print(f"Final validation dataset size: {len(val_dataset)}")

    # Print first few examples
    print("First 3 training examples:")
    for i in range(min(3, len(train_dataset))):
        print(f"Example {i}:")
        print(train_dataset[i])
        print(f"Input IDs length: {len(train_dataset[i]['input_ids'])}")
        print()

    # Data collator
    data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

    # Load configuration
    config = load_config('config.yaml')
    training_args = TrainingArguments(
        **config['training'],
        overwrite_output_dir=True,
        evaluation_strategy="steps",
        load_best_model_at_end=True,
        no_cuda=True,  # Disable CUDA to use MPS
    )

    # Create Trainer instance
    trainer = Trainer(
        model=model,
        args=training_args,
        data_collator=data_collator,
        train_dataset=train_dataset,
        eval_dataset=val_dataset,
    )

    # Start training
    trainer.train()

    # Save the fine-tuned model
    trainer.save_model()

if __name__ == "__main__":
    # Set the default tensor type to float32
    torch.set_default_tensor_type(torch.FloatTensor)
    
    # Check if MPS is available
    if torch.backends.mps.is_available():
        device = torch.device("mps")
        print("Using MPS device")
    else:
        device = torch.device("cpu")
        print("MPS not available, using CPU")
    
    train()
