# -*- coding: utf-8 -*-
import argparse


def migration():
    parser = argparse.ArgumentParser()
    parser.add_argument('--conf',
                        help='wsgi conf file')

    parser.add_argument('--database',
                        help='sqlite database')
