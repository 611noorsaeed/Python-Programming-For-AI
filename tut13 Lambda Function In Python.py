# Syntax:
# lambda arguments: expression


# 1. Text Preprocessing
# A common use case in NLP is to preprocess text data by transforming it into a suitable format.
# Sample text data
texts = ["Hello World!", "This is a sample text.", "Python is great for data science!"]
# Convert texts to lowercase and remove punctuation using lambda
clean_text = list(map(lambda x: x.lower().replace('!','').replace('.',''), texts))
print(clean_text)

# ===========================
# 2. Filtering Stop Words
# In NLP, it's common to remove stop words from text.
stop_words = {'is', 'a', 'for', 'this'}
# Sample sentences
sentences = ["This is a test sentence.", "Python is great for data science."]
words = list(map(lambda s: " ".join(filter(lambda w: w.lower(),s.split())), sentences))
print(words)

# ===================================
# 3. Feature Creation
# In ML, you might want to create new features based on existing ones.
import pandas as pd

# Sample DataFrame
data = {'text': ['Good', 'Bad', 'Average'], 'rating': [1, 0, 0]}
df = pd.DataFrame(data)

df['is_pos'] = df['rating'].apply(lambda x: True if x == 1 else False)
print(df.head())

#===================================
# 4. Custom Sorting
# Sorting lists of dictionaries based on specific criteria.

# Sample data
data = [
    {'name': 'John', 'age': 25},
    {'name': 'Jane', 'age': 30},
    {'name': 'Doe', 'age': 22}
]

sorted_data = sorted(data, key=lambda x: x['age'])
print(sorted_data)

