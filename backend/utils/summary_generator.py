from logger import logging
from exception import CustomeException

import sys
import torch


# ==========================================================
# NEWS SUMMARY
# ==========================================================

def news_summary(inputs, model, tokenizer) -> str:

    try:

        model.eval()

        with torch.inference_mode():

            summary_ids = model.generate(
                input_ids=inputs["input_ids"],
                attention_mask=inputs["attention_mask"],
                max_length=120,
                min_length=35,
                num_beams=6,
                length_penalty=1.0,
                no_repeat_ngram_size=3,
                early_stopping=True
            )

        summary = tokenizer.decode(
            summary_ids[0],
            skip_special_tokens=True,
            clean_up_tokenization_spaces=False
        )

        logging.info(
            "News summary generated successfully."
        )

        return summary.strip()

    except Exception as e:

        raise CustomeException(e, sys)


# ==========================================================
# BILLS SUMMARY
# ==========================================================

def bills_summary(inputs, model, tokenizer) -> str:

    try:

        model.eval()

        # LED requires global attention
        global_attention_mask = torch.zeros_like(
            inputs["input_ids"]
        )

        # Give global attention to the first token
        global_attention_mask[:, 0] = 1

        with torch.inference_mode():

            summary_ids = model.generate(
                input_ids=inputs["input_ids"],
                attention_mask=inputs["attention_mask"],
                global_attention_mask=global_attention_mask,
                num_beams=5,
                max_length=512,
                min_length=80,
                no_repeat_ngram_size=3,
                early_stopping=True
            )

        summary = tokenizer.decode(
            summary_ids[0],
            skip_special_tokens=True,
            clean_up_tokenization_spaces=True
        )

        logging.info(
            "Bills summary generated successfully."
        )

        return summary.strip()

    except Exception as e:

        raise CustomeException(e, sys)


# ==========================================================
# MEDICAL SUMMARY
# ==========================================================

def medical_summary(inputs, model, tokenizer) -> str:

    try:

        model.eval()

        with torch.inference_mode():

            summary_ids = model.generate(
                input_ids=inputs["input_ids"],
                attention_mask=inputs["attention_mask"],
                num_beams=6,
                max_length=256,
                min_length=80,
                length_penalty=1.0,
                no_repeat_ngram_size=3,
                early_stopping=True
            )

        summary = tokenizer.decode(
            summary_ids[0],
            skip_special_tokens=True,
            clean_up_tokenization_spaces=True
        )

        logging.info(
            "Medical summary generated successfully."
        )

        return summary.strip()

    except Exception as e:

        raise CustomeException(e, sys)

