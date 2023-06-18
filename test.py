
from gensim.summarization import summarize

# Input text to be summarized
text = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod auctor neque, 
a ultricies metus tempus sed. Quisque nec dolor nec lorem posuere laoreet. 
Nulla sollicitudin tortor sed justo efficitur, ac interdum sem ultrices. 
Phasellus sed lectus ac urna gravida rutrum. Fusce fermentum, mi ut faucibus 
faucibus, sem lorem laoreet nunc, nec faucibus elit velit id nisl. 
'''

# Summarize the text
summary = summarize(text)

# Print the summarized text
print(summary)