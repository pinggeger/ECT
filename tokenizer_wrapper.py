#!/usr/bin/env python


import sys
import twokenize
import re

word_pattern = re.compile(r'[0-9a-zA-Z@#]+')


def tokenize_and_join_tweet(tweet, abbrevs=set(["None"])):
    tokens = twokenize.tokenize(tweet)
    s= split_contractions_tweet(tokens, abbrevs)
    s = " ".join(s)
    return s


def split_contractions_tweet(tokens, abbrevs=set(["None"])):
    # Fix "n't", "I'm", "'re", "'s", "'ve", "'ll"  cases
    new_token_list = []
    curr = 0
    for token in tokens:
        for word in reset_dash(token):
            if len(word) < 1:
                continue
            # print(token + " --> " + word)
            curr += 1
            new_tk = None
            if word[-3:].lower() == 'n\'t':
                if word.lower() == 'won\'t':
                    new_token_list.append('will')
                    new_token_list.append('not')
                elif word.lower() == 'can\'t':
                    new_token_list.append('can')
                    new_token_list.append('not')
                else:
                    new_tk = word[:-3]
                    new_token_list.append('not')
            elif word == 'I\'m' or word == 'i\'m':
                new_token_list.append('I')
                new_token_list.append('\'m')
            elif word[-3:].lower() == '\'re':
                new_tk = word[:-3]
                new_token_list.append('\'re')
            elif word[-2:] == '\'s':
                new_tk = word[:-2]
                new_token_list.append('\'s')
            elif word[-3:].lower() == '\'ve':
                new_tk = word[:-3]
                new_token_list.append('\'ve')
            elif word[-3:] == '\'ll':
                new_tk = word[:-3]
                new_token_list.append('\'ll')
            elif word == "doesnt":
                new_token_list.append('does')
                new_token_list.append('not')
            elif word_pattern.match(word) is None:
                if len(new_token_list) == 0 and word == ".":
                    continue
                else:
                    new_token_list.append(word)
                    continue
            elif word == "HTTPURL":
                continue
            elif word.startswith("#"):
                new_token_list.append(word.lower())
            elif word.startswith("@"):
                new_token_list.append(word.lower())
            else:
                if word.isdigit():
                    new_token_list.append(word)
                elif word.isupper() and word in abbrevs:
                    new_token_list.append(word)
                else:
                    new_token_list.append(word.lower())
            # Add new token if one exists
            if new_tk:
                new_token_list.insert(-1, new_tk)
    # print(type_list)
    return new_token_list


def reset_dash(word):
    if word.startswith('#'):
        type = '#'
        word = word[1:]
    elif word.startswith('@'):
        type = '@'
        word = word[1:]
    else:
        type = ''
    if '-' in word:
        words = []
        isnum = False
        for w in word.split('-'):
            if w.isdigit() and isnum:
                words[-1] += '-' + w
            elif w.isdigit():
                isnum = True
                words.append(w)
            else:
                isnum = False
                words.append(w)
    else:
        words = word.split()
    for i in range(len(words)):
        words[i] = type + words[i]
    return words


if __name__ == '__main__':
    for line in sys.stdin:
        print(tokenize_and_join_tweet(line))
