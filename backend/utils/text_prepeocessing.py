from logger import logging
from exception import CustomeException
import sys


def news_text_preprocessing(text: str, tokenizer):
    try:
        input = tokenizer(text, return_tensors='pt', max_length=1024, truncation=True)

        logging.info("News text preprocessing completed successfully.")
        return input

    except Exception as e:
        raise CustomeException(e, sys)
    
def bills_text_preprocessing(text: str, tokenizer):
    try:
        inputs = tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            max_length=4096
        )

        logging.info("Bills text preprocessing completed successfully.")
        return inputs

    except Exception as e:
        raise CustomeException(e, sys)

    
def medical_text_preprocessing(text: str, tokenizer):
    try:
        inputs = tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            max_length=4096
        )

        logging.info("Medical text preprocessing completed successfully.")
        return inputs

    except Exception as e:
        raise CustomeException(e, sys)
