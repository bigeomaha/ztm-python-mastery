from translate import Translator

if __name__ == "__main__":
    lang = input('Enter a ISO 639-1 Two-Letter code to translate: ')
    translator = Translator(to_lang=lang)
    output_file_name = 'translator-' + lang + ".txt"
    try:
        with open('./translator.txt', 'r') as f:
            line = f.read()
            with open(output_file_name, 'w') as wf:
                wf.write(translator.translate(line))
    except FileNotFoundError:
        print('File was not there.')
    except IOError:
        print('Operating System Error on file.')
