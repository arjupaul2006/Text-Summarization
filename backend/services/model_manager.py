from logger import logging
from exception import CustomeException
import sys
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, LEDForConditionalGeneration
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

def load_model_and_tokenizer(model_name: str):
    try:
        if model_name == "news":
            # model_path = 'facebook/bart-large-cnn'
            model_path = BASE_DIR / 'models' / 'news_model'

            tokenizer = AutoTokenizer.from_pretrained(model_path)
            model = AutoModelForSeq2SeqLM.from_pretrained(model_path)

        elif model_name == "medical":
            # model_path = 'google/long-t5-tglobal-base'
            model_path = BASE_DIR / 'models' / 'medical_model'

            tokenizer = AutoTokenizer.from_pretrained(model_path)
            model = AutoModelForSeq2SeqLM.from_pretrained(model_path)

        elif model_name == "bills":
            # model_path = 'Anurag33Gaikwad/legal-led-billsum-summarization'

            model_path = BASE_DIR / 'models' / 'bills_model'

            tokenizer = AutoTokenizer.from_pretrained(model_path)
            model = LEDForConditionalGeneration.from_pretrained(model_path)

        else:
            raise ValueError("Invalid model name provided.")

        logging.info(f"Model and tokenizer for '{model_name}' loaded successfully.")

        return tokenizer, model

    except Exception as e:
        raise CustomeException(e, sys)