import requests as requests
from bs4 import BeautifulSoup
import sys

class WrongLangException(Exception):
    def __init__(self, langs):
        self.message = f"Sorry, the program doesn't support {langs}"
        super().__init__(self.message)

class WordException(Exception):
    def __init__(self, word):
        self.message = f"Sorry, unable to find {word}"
        super().__init__(self.message)




class Translator():

    def __init__(self):
        self.choiсe = ["Arabic", "German", "English", "Spanish", "French", "Hebrew", "Japanese",
        "Dutch", "Polish", "Portuguese", "Romanian", "Russian", "Turkish"]

    def translate(self, lang_from, lang_to, word, sess, headers, filename):

        with open(filename, "a+", encoding="utf-8") as f:
            if lang_to != lang_from:
                translate_to = f'{lang_from}-{lang_to}'.lower()
                url = f"https://context.reverso.net/translation/{translate_to}/{word}"
                try:
                    reply = sess.get(url, headers=headers)
                except requests.exceptions.ConnectionError:
                    print('Something wrong with your internet connection')
                    sys.exit(0)
                if reply.status_code == 404:
                    #raise WordException(word)
                    print(f"Sorry, unable to find {word}")
                    sys.exit()
                soup = BeautifulSoup(reply.content, 'html.parser')
                # get translations
                trans = []
                examples_src = []
                examples_trg = []
                for tag in soup.find_all('a', class_='translation'):
                    trans.append(tag.text.strip())
                # get examples
                for tag in  soup.find_all('div', {"class": "src ltr"}):
                    examples_src.append(tag.text.strip())
                for tag in  soup.find_all('div', {"class": ["trg ltr", "trg rtl arabic", "trg rtl"]}):
                    examples_trg.append(tag.text.strip())
                # write to the file
                f.write(f'\n{lang_to} Translations:\n')
                f.write(trans[1] + "\n")
                f.write(f'\n{lang_to} Examples:\n')
                f.write(f'{examples_src[0]}:\n')
                f.write(f'{examples_trg[0]}\n\n')

    def main(self):

        lang_from = sys.argv[1].capitalize()
        lang_to = sys.argv[2].capitalize()
        word = sys.argv[3]

        lang_err = ""
        if lang_from.capitalize() not in self.choiсe:
            lang_err = lang_from.lower();
        if lang_to.capitalize() not in self.choiсe:
            if lang_to.capitalize() != "All":
                if lang_err:
                    lang_err = lang_err + f", {lang_to}".lower()
                else: lang_err = lang_to.lower()

        if lang_err:
            #raise WrongLangException(lang_err)
            print(f"Sorry, the program doesn't support {lang_err}")

        filename = f"{word}.txt"
        headers = {'User-Agent': 'Mozilla/5.0'}
        sess = requests.Session()

        if lang_to == "All":
            for lang in self.choiсe:
                self.translate(lang_from, lang, word, sess, headers, filename)
        else:
            self.translate(lang_from, lang_to, word, sess, headers, filename)


        with open(filename) as f:
            print(f.read())



if __name__ == "__main__":
    try:
        translator = Translator()
        translator.main()
    except Exception as e:
        sys.exit(e)
