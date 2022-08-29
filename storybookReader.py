from urllib.request import urlopen

story = urlopen('http://sixty-north.com/c/t.txt')
story_words = []
for line in story:
    #line_words = line.decode('utf8').split()
    story_words.append(line.decode('utf8').replace('\n', '. ').capitalize())
wholeStory = ''.join(story_words)
story.close()
print(wholeStory)