#!/usr/bin/python3.6

from sys import argv
from sys import exit
from random import choice


def extract_words(text_file):
    words = []
    try:
        with open(text_file) as fin:
            for line in fin:
                for word in line.lower().rstrip().split():
                    if word.isalpha():
                        words.append(word)
    except FileNotFoundError:
        print('Файла с таким именем не существует')
        exit(0)
    return words


def fit(words):
    model = dict()
    for i in range(len(words) - 1):
        if model.get(words[i]) is None:
            model[words[i]] = []
        model[words[i]].append(words[i + 1])
    for x in model:
        model[x] = set(model[x])
    for x in model:
        model[x] = list(model[x])
    return model


def generate_seq(seed, model):
    try:
        choice(model[seed])
    except KeyError:
        print('Такого слова в тексте нет')
        return 0
    print(seed, end=' ')
    for i in range(length - 1):
        seed = choice(model[seed])
        print(seed, end=' ')
    print()


try:
    input_file = argv[1]
    cond_word = argv[2]
    length = int(argv[-1])
except (IndexError, ValueError):
    print('Ещё раз проверьте формат ввода')
    exit(0)

clear_words = extract_words(input_file)
lang_model = fit(clear_words)
generate_seq(cond_word, lang_model)
