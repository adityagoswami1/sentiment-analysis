Text Emotion and Sentiment Analysis
This project provides Python scripts for performing emotion and sentiment analysis on text data. It utilizes a custom emotion lexicon and, in one version, integrates NLTK for more advanced text processing and VADER sentiment analysis.

Features
Emotion Analysis: Counts the occurrences of various emotions in text based on a provided emotion.txt mapping.

Text Preprocessing: Includes steps for lowercasing, punctuation removal, and stop word filtering.

Sentiment Analysis (using NLTK): main2.0.py extends functionality to include positive/negative/neutral sentiment scoring using NLTK's VADER.

Visualization: main2.0.py includes basic plotting of emotion distribution (requires matplotlib).

Files
main.py: The initial script for basic text cleaning and emotion counting.

main2.0.py: An enhanced version that uses NLTK for tokenization and stop words, and includes VADER sentiment analysis and emotion visualization.

emotion.txt: A plain text file containing a mapping of words to primary emotions (e.g., word:emotion).

read.txt: A sample text file used as input for the analysis scripts.

requirements.txt: Lists all Python dependencies required to run the scripts.

LICENSE: Specifies the licensing terms for this project.

.gitignore: Specifies intentionally untracked files to ignore.

Getting Started
Prerequisites
Make sure you have Python 3.x installed (preferably Python 3.10 or newer, as NLTK compatibility is best with recent versions).

This project uses several Python libraries that need to be installed. You can install them using pip:

pip install -r requirements.txt

Additionally, if you are using main2.0.py, you will need to download NLTK data. Create a file named download_nltk_data.py in your project directory with the following content and run it:

import nltk

print("Downloading NLTK 'punkt' tokenizer...")
nltk.download('punkt')
print("Downloading NLTK 'punkt_tab' for specific tokenizer tables...")
nltk.download('punkt_tab')
print("Downloading NLTK 'stopwords' corpus...")
nltk.download('stopwords')
print("Downloading NLTK 'vader_lexicon' (for sentiment analysis)...")
nltk.download('vader_lexicon')

print("\nNLTK data download complete!")

Run this script from your terminal:

python download_nltk_data.py

Usage
Place your text: Ensure the text you want to analyze is in a file named read.txt in the same directory as the Python scripts.

Run the script:

For basic emotion analysis:

python main.py

For enhanced emotion and sentiment analysis with visualization:

python main2.0.py

The scripts will print the emotion counts and sentiment scores to the console. main2.0.py will also display a bar chart of emotion distribution.

Customizing Emotions
The emotion.txt file defines the word-to-emotion mapping. You can modify this file to include more words and emotions relevant to your specific needs. The format should be word:emotion on each line.

Contributing
Contributions are welcome! If you find a bug or have a suggestion, please open an issue or submit a pull request.

License
This project is licensed under the MIT License.

Contact
[Your Name/GitHub Username] - [Your Email/Portfolio Link]