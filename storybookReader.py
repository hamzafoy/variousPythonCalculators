# This imported module facilitates the opening of URLs to derive data
from urllib.request import urlopen

def fetch_words():
    story = urlopen('http://sixty-north.com/c/t.txt')
    story_words = []
    for line in story:
        #The following line appends each decoded byte, replaces the \n character, and capitalizes each new line
        story_words.append(line.decode('utf8').replace('\n', '. ').capitalize())
    wholeStory = ''.join(story_words)
    story.close()
    print(wholeStory)

if __name__ == '__main__':
    fetch_words()