import sys
import os

class Checker(object):
    def __init__(self):
        self.filename = 'article_id.log'

    def read_file(self):
        with open(self.filename, 'r') as f:
            lines = f.readlines()
        for line in lines: print(line)

    def check_file_duplicate(self, content):
        with open(self.filename, 'r') as f:
            lines = f.readlines()
        for line in lines:
            if content is line.rstrip('\n'):
                print("duplicated!")
                return True
            else:
                return False

    def write_file(self, content):
        with open(self.filename, 'a') as f:
            f.write(content+'\n')


if __name__ == '__main__':
    c = Checker()
    a = ["1", "2", "3", "4", "5"]
    for e in a:
        c.write_file(e)

    c.check_file("2")

