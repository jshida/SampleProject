#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

import subprocess


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print('Hello {}!'.format(self.name))


def main():
    cmd = "ls -l"
    run_cmd = subprocess.call(cmd.split())
    print('Hello World!')
    print(run_cmd)

    jeff = Person("Jefferson", 23)
    jeff.greeting()


if __name__ == "__main__":
    main()
