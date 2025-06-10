import nltk

print("Downloading NLTK 'punkt' tokenizer...")
nltk.download('punkt') # This generally includes the necessary components for tokenization
print("Downloading NLTK 'punkt_tab' for specific tokenizer tables...")
nltk.download('punkt_tab') # Explicitly download as requested by the error
print("Downloading NLTK 'stopwords' corpus...")
nltk.download('stopwords')
print("Downloading NLTK 'vader_lexicon' (for sentiment analysis)...")
nltk.download('vader_lexicon')

print("\nNLTK data download complete!")