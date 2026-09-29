# NLP Intelligence Studio

NLP Intelligence Studio is a Python-based Natural Language Processing application designed to analyze and process textual data through an interactive graphical interface. The system integrates text preprocessing, named entity extraction, sentiment analysis, and REST API functionality into a modular architecture.

## Overview

The application provides a centralized platform for performing fundamental NLP operations on user-provided text. It processes input through multiple stages and presents the results through a user-friendly Tkinter interface.

The project is designed with a modular structure, making it suitable for academic learning, experimentation, and future integration of advanced NLP and transformer-based techniques.

## Key Features

### Text Preprocessing

The system performs several preprocessing operations, including:

- Original text handling
- Lowercase conversion
- Text cleaning
- Tokenization
- Stop-word removal

### Named Entity Extraction

The application identifies and displays relevant entities present in the input text along with their corresponding entity types.

### Sentiment Analysis

The system analyzes the emotional characteristics of text and provides:

- Sentiment classification
- Polarity score
- Subjectivity score

### Graphical User Interface

The application provides an interactive desktop interface developed using Tkinter. Users can enter text, load sample data, execute analysis, and view results within a single interface.

### REST API

A Flask-based REST API is integrated into the application and runs in the background. This enables NLP functionality to be accessed programmatically through HTTP requests.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Tkinter | Graphical user interface |
| spaCy | Natural language processing and entity extraction |
| TextBlob | Sentiment analysis |
| Flask | REST API development |
| Regex | Text cleaning and preprocessing |

## Project Structure

```text
NLP-Intelligence-Studio/
│
├── main.py
├── nlp_pipeline.py
├── rest_api.py
├── requirements.txt
├── .gitignore
└── README.md
```

The file structure may vary depending on the implementation and additional modules.

## Installation

### Prerequisites

Make sure the following are installed:

- Python 3.9 or later
- pip
- Git

### Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/NLP-Intelligence-Studio.git
```

Navigate to the project directory:

```bash
cd NLP-Intelligence-Studio
```

### Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

If the project uses the spaCy English language model, install it using:

```bash
python -m spacy download en_core_web_sm
```

## Running the Application

Start the application using:

```bash
python main.py
```

The NLP Intelligence Studio interface will open.

Enter text in the input area and select the analysis option. The application will process the input and display preprocessing results, extracted entities, and sentiment analysis results.

The integrated REST API runs locally at:

```text
http://127.0.0.1:5000
```

## Application Workflow

```text
User Input
     |
     v
Text Preprocessing
     |
     v
Tokenization and Stop-word Removal
     |
     v
Named Entity Extraction
     |
     v
Sentiment Analysis
     |
     v
Results Display
     |
     v
REST API Integration
```

## Example

### Input

```text
OpenAI is an amazing company in San Francisco.
I really love artificial intelligence and ChatGPT!
```

### Output

The system processes the input and provides information such as:

```text
Text Preprocessing
- Original Text
- Lowercase Text
- Clean Text
- Tokens
- Stop Words Removed

Entity Extraction
- Entity Text
- Entity Type

Sentiment Analysis
- Sentiment
- Polarity
- Subjectivity
```

## Objectives

The primary objectives of this project are:

1. To implement fundamental Natural Language Processing techniques.
2. To understand and apply text preprocessing methods.
3. To perform named entity extraction from textual data.
4. To analyze sentiment and subjectivity in text.
5. To develop an interactive NLP analysis interface.
6. To integrate NLP functionality with a REST API.
7. To demonstrate modular software architecture for NLP applications.

## Future Enhancements

The project can be extended with advanced NLP capabilities, including:

- Transformer-based text understanding
- Automatic text summarization
- Semantic search
- Document intelligence
- PDF and DOCX document processing
- Document classification
- Question answering
- Multiple language support
- Database integration
- Cloud deployment

## Applications

The system can serve as a foundation for applications such as:

- Customer feedback analysis
- Product review analysis
- Text classification
- Document analysis
- Chatbot systems
- Content processing
- Academic NLP research and experimentation

## Author

**Vaishnavi Bachhav**

B.Tech Computer Science and Engineering

## License

This project is developed for educational and academic purposes.
