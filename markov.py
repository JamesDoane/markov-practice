"""Generate Markov text from text files."""

import random 


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    file = open(file_path)
    contents = file.read()


    return contents


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
  
    chains = {}

    # your code goes here

    words = text_string.split()
    for i in range(len(words)-1):
        if (words[i],words[i+1]) not in chains:
            chains[(words[i],words[i+1])] = []
        
        try:
            if words[i+2]:
                chains[(words[i], words[i+1])].append(words[i+2])
        except IndexError:
            pass

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here
    link_key = random.choice(list(chains.keys()))
    words.append(link_key[0])
    words.append(link_key[1])
    while True:
        try:
            link_value = random.choice(list(chains.get(link_key)))
            words.append(link_value)
            link_key = tuple((words[-2], words[-1]))
        except:
            break

    
    return ' '.join(words)


input_path = '98-0.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)
# # Produce random text
random_text = make_text(chains)

print(random_text)
