from logger import logging
from exception import CustomeException

import sys

from utils.text_prepeocessing import (
    news_text_preprocessing,
    bills_text_preprocessing,
    medical_text_preprocessing
)

from utils.summary_generator import (
    news_summary,
    bills_summary,
    medical_summary
)


def summarize_text(
    text: str,
    type: str,
    model_manager
) -> dict:

    try:

        # --------------------------------------------------
        # Determine model name
        # --------------------------------------------------

        if type == "News Article":

            model_name = "news"

        elif type == "Medical Paper":

            model_name = "medical"

        elif type == "Bills and Acts":

            model_name = "bills"

        else:

            return {
                "error": (
                    "Invalid type provided. Please choose from "
                    "'News Article', 'Medical Paper', or "
                    "'Bills and Acts'."
                )
            }


        # --------------------------------------------------
        # Get already-loaded model
        # --------------------------------------------------

        tokenizer, model = model_manager.get_model(model_name)


        # --------------------------------------------------
        # Preprocess text
        # --------------------------------------------------

        if type == "News Article":

            inputs = news_text_preprocessing(
                text,
                tokenizer
            )

        elif type == "Medical Paper":

            inputs = medical_text_preprocessing(
                text,
                tokenizer
            )

        elif type == "Bills and Acts":

            inputs = bills_text_preprocessing(
                text,
                tokenizer
            )


        # --------------------------------------------------
        # Generate summary
        # --------------------------------------------------

        if type == "News Article":

            summary = news_summary(
                inputs,
                model,
                tokenizer
            )

        elif type == "Medical Paper":

            summary = medical_summary(
                inputs,
                model,
                tokenizer
            )

        elif type == "Bills and Acts":

            summary = bills_summary(
                inputs,
                model,
                tokenizer
            )


        logging.info(
            f"Summary generated successfully for type: {type}"
        )

        return {
            "summary": summary,
            "type": type
        }


    except Exception as e:

        logging.error(
            f"Error in summarize_text: {e}"
        )

        raise CustomeException(e, sys)

