import re
import spacy
from textblob import TextBlob


class NLPPipeline:

    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

        self.stop_words = {
            "a", "an", "the", "is", "are", "was", "were",
            "am", "be", "been", "being",
            "to", "of", "in", "on", "at", "for", "from",
            "and", "or", "but", "if", "then",
            "this", "that", "these", "those",
            "i", "you", "he", "she", "it", "we", "they",
            "my", "your", "his", "her", "our", "their",
            "with", "as", "by", "about", "into",
            "can", "could", "would", "should",
            "will", "shall", "do", "does", "did"
        }

    # -----------------------------
    # TEXT PREPROCESSING
    # -----------------------------
    def preprocess(self, text):

        original_text = text

        # Convert to lowercase
        lowercase = text.lower()

        # Remove URLs
        no_urls = re.sub(
            r"https?://\S+|www\.\S+",
            "",
            lowercase
        )

        # Remove punctuation
        clean_text = re.sub(
            r"[^a-zA-Z0-9\s]",
            "",
            no_urls
        )

        # Remove extra spaces
        clean_text = re.sub(
            r"\s+",
            " ",
            clean_text
        ).strip()

        # Tokenization
        tokens = clean_text.split()

        # Stop word removal
        filtered_tokens = [
            word for word in tokens
            if word not in self.stop_words
        ]

        return {
            "original_text": original_text,
            "lowercase_text": lowercase,
            "clean_text": clean_text,
            "tokens": tokens,
            "stopwords_removed": filtered_tokens
        }

    # -----------------------------
    # ENTITY EXTRACTION
    # -----------------------------
    def extract_entities(self, text):

        doc = self.nlp(text)

        entities = []

        for ent in doc.ents:

            entities.append({
                "text": ent.text,
                "label": ent.label_,
                "description": spacy.explain(ent.label_) or ent.label_
            })

        return entities

    # -----------------------------
    # SENTIMENT ANALYSIS
    # -----------------------------
    def sentiment(self, text):

        blob = TextBlob(text)

        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity

        if polarity > 0.1:
            sentiment = "Positive 😊"

        elif polarity < -0.1:
            sentiment = "Negative 😞"

        else:
            sentiment = "Neutral 😐"

        return {
            "sentiment": sentiment,
            "polarity": round(polarity, 3),
            "subjectivity": round(subjectivity, 3)
        }

    # -----------------------------
    # COMPLETE PIPELINE
    # -----------------------------
    def analyze(self, text):

        return {
            "preprocessing": self.preprocess(text),
            "entities": self.extract_entities(text),
            "sentiment": self.sentiment(text)
        }