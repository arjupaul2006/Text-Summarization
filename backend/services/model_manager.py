from logger import logging
from exception import CustomeException

import sys
from transformers import (
    AutoTokenizer,
    AutoModelForSeq2SeqLM,
    LEDForConditionalGeneration
)


class ModelManager:

    def __init__(self):

        self.models = {}
        self.tokenizers = {}

    def load_all_models(self):

        try:

            logging.info("Loading all models...")

            # ---------------- NEWS ----------------

            news_path = "facebook/bart-large-cnn"

            self.tokenizers["news"] = AutoTokenizer.from_pretrained(
                news_path
            )

            self.models["news"] = AutoModelForSeq2SeqLM.from_pretrained(
                news_path
            )

            self.models["news"].eval()

            logging.info("News model loaded.")

            # ---------------- MEDICAL ----------------

            medical_path = "google/long-t5-tglobal-base"

            self.tokenizers["medical"] = AutoTokenizer.from_pretrained(
                medical_path
            )

            self.models["medical"] = AutoModelForSeq2SeqLM.from_pretrained(
                medical_path
            )

            self.models["medical"].eval()

            logging.info("Medical model loaded.")

            # ---------------- BILLS ----------------

            # bills_path = "Anurag33Gaikwad/legal-led-billsum-summarization"

            # self.tokenizers["bills"] = AutoTokenizer.from_pretrained(
            #     bills_path
            # )

            # self.models["bills"] = LEDForConditionalGeneration.from_pretrained(
            #     bills_path
            # )

            # self.models["bills"].eval()

            # logging.info("Bills model loaded.")

            # logging.info("All models loaded successfully.")

        except Exception as e:

            raise CustomeException(e, sys)

    def get_model(self, model_name):

        return self.tokenizers[model_name], self.models[model_name]