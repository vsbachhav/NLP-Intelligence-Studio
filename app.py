import tkinter as tk
from tkinter import ttk, messagebox
import threading
import requests

from nlp_pipeline import NLPPipeline
from rest_api import start_server


# ==========================================
# COLORS
# ==========================================

BG = "#0F172A"
CARD = "#1E293B"
CARD2 = "#334155"
TEXT = "#F8FAFC"
SUBTEXT = "#CBD5E1"
ACCENT = "#38BDF8"
GREEN = "#22C55E"
RED = "#EF4444"
YELLOW = "#FACC15"


# ==========================================
# NLP PIPELINE
# ==========================================

pipeline = NLPPipeline()


# ==========================================
# START REST SERVER IN BACKGROUND
# ==========================================

server_thread = threading.Thread(
    target=start_server,
    daemon=True
)

server_thread.start()


# ==========================================
# MAIN WINDOW
# ==========================================

root = tk.Tk()

root.title("NLP Intelligence Studio")
root.geometry("1200x760")
root.configure(bg=BG)

root.minsize(1000, 650)


# ==========================================
# TITLE
# ==========================================

title = tk.Label(
    root,
    text="NLP INTELLIGENCE STUDIO",
    font=("Segoe UI", 26, "bold"),
    bg=BG,
    fg=TEXT
)

title.pack(pady=(20, 2))


subtitle = tk.Label(
    root,
    text="Text Preprocessing  •  Entity Extraction  •  Sentiment Analysis  •  REST API",
    font=("Segoe UI", 11),
    bg=BG,
    fg=SUBTEXT
)

subtitle.pack(pady=(0, 15))


# ==========================================
# INPUT CARD
# ==========================================

input_frame = tk.Frame(
    root,
    bg=CARD,
    highlightbackground=ACCENT,
    highlightthickness=1
)

input_frame.pack(
    fill="x",
    padx=30,
    pady=10
)


input_label = tk.Label(
    input_frame,
    text="ENTER YOUR TEXT",
    font=("Segoe UI", 12, "bold"),
    bg=CARD,
    fg=ACCENT
)

input_label.pack(
    anchor="w",
    padx=20,
    pady=(15, 5)
)


text_input = tk.Text(
    input_frame,
    height=5,
    font=("Segoe UI", 12),
    bg="#020617",
    fg=TEXT,
    insertbackground=TEXT,
    relief="flat",
    wrap="word"
)

text_input.pack(
    fill="x",
    padx=20,
    pady=10
)


# ==========================================
# SAMPLE TEXT
# ==========================================

sample_text = (
    "OpenAI is an amazing company in San Francisco. "
    "I really love artificial intelligence and ChatGPT!"
)


def load_sample():

    text_input.delete("1.0", tk.END)

    text_input.insert(
        tk.END,
        sample_text
    )


sample_btn = tk.Button(
    input_frame,
    text="Load Sample",
    command=load_sample,
    bg=CARD2,
    fg=TEXT,
    activebackground=ACCENT,
    activeforeground=BG,
    relief="flat",
    padx=15,
    pady=7,
    cursor="hand2"
)

sample_btn.pack(
    side="left",
    padx=20,
    pady=(0, 15)
)


# ==========================================
# ANALYZE BUTTON
# ==========================================

def analyze_text():

    text = text_input.get(
        "1.0",
        tk.END
    ).strip()

    if not text:

        messagebox.showwarning(
            "Input Required",
            "Please enter some text."
        )

        return

    try:

        result = pipeline.analyze(text)

        show_preprocessing(
            result["preprocessing"]
        )

        show_entities(
            result["entities"]
        )

        show_sentiment(
            result["sentiment"]
        )

        status_label.config(
            text="● Analysis Complete",
            fg=GREEN
        )

    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )


analyze_btn = tk.Button(
    input_frame,
    text="⚡ ANALYZE TEXT",
    command=analyze_text,
    bg=ACCENT,
    fg=BG,
    activebackground="#7DD3FC",
    relief="flat",
    font=("Segoe UI", 11, "bold"),
    padx=25,
    pady=8,
    cursor="hand2"
)

analyze_btn.pack(
    side="right",
    padx=20,
    pady=(0, 15)
)


# ==========================================
# RESULTS AREA
# ==========================================

results_frame = tk.Frame(
    root,
    bg=BG
)

results_frame.pack(
    fill="both",
    expand=True,
    padx=30,
    pady=10
)


# ==========================================
# PREPROCESSING CARD
# ==========================================

preprocess_frame = tk.LabelFrame(
    results_frame,
    text="  TEXT PREPROCESSING  ",
    font=("Segoe UI", 11, "bold"),
    bg=CARD,
    fg=ACCENT,
    bd=1,
    relief="flat"
)

preprocess_frame.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(0, 8)
)


preprocess_output = tk.Text(
    preprocess_frame,
    font=("Consolas", 10),
    bg="#020617",
    fg=TEXT,
    relief="flat",
    wrap="word"
)

preprocess_output.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)


# ==========================================
# ENTITY CARD
# ==========================================

entity_frame = tk.LabelFrame(
    results_frame,
    text="  ENTITY EXTRACTION  ",
    font=("Segoe UI", 11, "bold"),
    bg=CARD,
    fg=ACCENT,
    bd=1,
    relief="flat"
)

entity_frame.pack(
    side="left",
    fill="both",
    expand=True,
    padx=8
)


entity_tree = ttk.Treeview(
    entity_frame,
    columns=("Entity", "Type"),
    show="headings"
)

entity_tree.heading(
    "Entity",
    text="Entity"
)

entity_tree.heading(
    "Type",
    text="Type"
)

entity_tree.column(
    "Entity",
    width=130
)

entity_tree.column(
    "Type",
    width=130
)

entity_tree.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)


# ==========================================
# SENTIMENT CARD
# ==========================================

sentiment_frame = tk.LabelFrame(
    results_frame,
    text="  SENTIMENT ANALYSIS  ",
    font=("Segoe UI", 11, "bold"),
    bg=CARD,
    fg=ACCENT,
    bd=1,
    relief="flat"
)

sentiment_frame.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(8, 0)
)


sentiment_title = tk.Label(
    sentiment_frame,
    text="😐",
    font=("Segoe UI", 45),
    bg=CARD,
    fg=TEXT
)

sentiment_title.pack(
    pady=(35, 5)
)


sentiment_result = tk.Label(
    sentiment_frame,
    text="Waiting for analysis...",
    font=("Segoe UI", 17, "bold"),
    bg=CARD,
    fg=TEXT
)

sentiment_result.pack(
    pady=10
)


polarity_label = tk.Label(
    sentiment_frame,
    text="Polarity: --",
    font=("Segoe UI", 11),
    bg=CARD,
    fg=SUBTEXT
)

polarity_label.pack(
    pady=5
)


subjectivity_label = tk.Label(
    sentiment_frame,
    text="Subjectivity: --",
    font=("Segoe UI", 11),
    bg=CARD,
    fg=SUBTEXT
)

subjectivity_label.pack(
    pady=5
)


# ==========================================
# REST API STATUS
# ==========================================

status_label = tk.Label(
    root,
    text="● REST API: http://127.0.0.1:5000",
    font=("Segoe UI", 10),
    bg=BG,
    fg=GREEN
)

status_label.pack(
    pady=(0, 12)
)


# ==========================================
# DISPLAY PREPROCESSING
# ==========================================

def show_preprocessing(data):

    preprocess_output.delete(
        "1.0",
        tk.END
    )

    preprocess_output.insert(
        tk.END,
        "ORIGINAL TEXT\n"
    )

    preprocess_output.insert(
        tk.END,
        data["original_text"] + "\n\n"
    )

    preprocess_output.insert(
        tk.END,
        "LOWERCASE\n"
    )

    preprocess_output.insert(
        tk.END,
        data["lowercase_text"] + "\n\n"
    )

    preprocess_output.insert(
        tk.END,
        "CLEAN TEXT\n"
    )

    preprocess_output.insert(
        tk.END,
        data["clean_text"] + "\n\n"
    )

    preprocess_output.insert(
        tk.END,
        "TOKENS\n"
    )

    preprocess_output.insert(
        tk.END,
        ", ".join(data["tokens"]) + "\n\n"
    )

    preprocess_output.insert(
        tk.END,
        "STOP WORDS REMOVED\n"
    )

    preprocess_output.insert(
        tk.END,
        ", ".join(data["stopwords_removed"])
    )


# ==========================================
# DISPLAY ENTITIES
# ==========================================

def show_entities(entities):

    for item in entity_tree.get_children():

        entity_tree.delete(item)

    for entity in entities:

        entity_tree.insert(
            "",
            tk.END,
            values=(
                entity["text"],
                entity["label"]
            )
        )

    if not entities:

        entity_tree.insert(
            "",
            tk.END,
            values=(
                "No entities",
                "-"
            )
        )


# ==========================================
# DISPLAY SENTIMENT
# ==========================================

def show_sentiment(data):

    sentiment = data["sentiment"]

    sentiment_result.config(
        text=sentiment
    )

    polarity_label.config(
        text=f"Polarity: {data['polarity']}"
    )

    subjectivity_label.config(
        text=f"Subjectivity: {data['subjectivity']}"
    )

    if "Positive" in sentiment:

        sentiment_title.config(
            text="😊",
            fg=GREEN
        )

    elif "Negative" in sentiment:

        sentiment_title.config(
            text="😞",
            fg=RED
        )

    else:

        sentiment_title.config(
            text="😐",
            fg=YELLOW
        )


# ==========================================
# START UI
# ==========================================

root.mainloop()