from logger import logging
from exception import CustomeException
import sys
import torch


def news_summary(input, model, tokenizer) -> str:
    try:
        model.eval()
        # Generate the summary
        with torch.no_grad():
            summarize_ids = model.generate(
                input["input_ids"],
                attention_mask=input["attention_mask"],
                max_length=100,
                min_length=35,
                num_beams=6,
                length_penalty=1.0,
                no_repeat_ngram_size=3,
                early_stopping=True
            )

        # decode the generated summary
        summary = tokenizer.decode(
            summarize_ids[0],
            skip_special_tokens=True,
            clean_up_tokenization_spaces=False
        )

        return summary
    except Exception as e:
        raise CustomeException(e, sys)
    
def bills_summary(input, model, tokenizer) -> str:
    try:
        model.eval()

        # Give global attention to the first token
        global_attention_mask = torch.zeros_like(input["input_ids"])
        global_attention_mask[:, 0] = 1

        # Generate summary
        with torch.no_grad():
            summary_ids = model.generate(
                input_ids=input["input_ids"],
                attention_mask=input["attention_mask"],
                global_attention_mask=global_attention_mask,
                num_beams=5,
                max_length=512,
                min_length=80,
                early_stopping=True
            )

        # Decode summary
        summary = tokenizer.decode(
            summary_ids[0],
            skip_special_tokens=True,
            clean_up_tokenization_spaces=True
        )

        return summary.strip()

    except Exception as e:
        raise CustomeException(e, sys)

def medical_summary(input, model, tokenizer) -> str:
    try:
        model.eval()

        with torch.no_grad():
            summary_ids = model.generate(
                input_ids=input["input_ids"],
                attention_mask=input["attention_mask"],
                num_beams=5,
                max_length=300,
                min_length=40,
                length_penalty=1.0,
                no_repeat_ngram_size=3,
                early_stopping=True
            )

        summary = tokenizer.decode(
            summary_ids[0],
            skip_special_tokens=True,
            clean_up_tokenization_spaces=True
        )

        return summary.strip()

    except Exception as e:
        raise CustomeException(e, sys)