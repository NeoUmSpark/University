import string

class WordsFinder:
    def __init__(self, *file_names):
        self.names = list(file_names)
        self.all_words = {}
    def get_all_words(self):
        for file_name in self.names:
            with open(file_name, encoding='utf-8') as file:
                text = file.read()
                words = text.lower().translate(str.maketrans('', '', string.punctuation)).split()
                self.all_words[file_name] = words
        return self.all_words
    def find(self, word):
        result = {}
        for name, words in self.get_all_words().items():
            for i, finder in enumerate(words):
                if word.lower() == finder.lower():
                    result[name] = i +1
                    return result

    def count(self, word):
        result = {}
        for name, words in self.get_all_words().items():
            count = words.count(word.lower())
            result[name] = count
        return result

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
