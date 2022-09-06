# This imported module facilitates the opening of URLs to derive data
from urllib.request import urlopen
# Allows access to command line parameters passed in terminal
import sys



def fetch_words(url):
    """
    Fetch a list of sentences from a story from an URL

    Arguments: 
        url: The URL of an UTF-8 .txt file

    Returns:
        A list of strings containing the sentences composing
        the story.
    """
    story = urlopen(url)
    story_words = []
    for line in story:
        #The following line appends each decoded byte, replaces the \n character, and capitalizes each new line
        story_words.append(line.decode('utf8').replace('\n', '. ').capitalize())
    wholeStory = ''.join(story_words)
    story.close()
    return wholeStory



def main(url):
    storybook = fetch_words(url)
    print(storybook)

# Enables taking URLs of .txt files and will print them.
# Use http://textfiles.com/stories/snowmaid.txt as an example
if __name__ == '__main__':
    help(fetch_words)
    main(sys.argv[1])