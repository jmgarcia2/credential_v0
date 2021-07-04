#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Código de prueba de recoger parámetros

import argparse
import sys

username = ""
password = ""
if __name__ == '__main__':

    print(f"This is the name of the script: ", {sys.argv[0]})
    print(f"Number of arguments: ", {len(sys.argv)})
    print(f"The arguments are: ", {str(sys.argv)})

    # initialize parser
    parser = argparse.ArgumentParser()
    parser.add_argument("user", type=str, help="userId")
    parser.add_argument("pw", type=str, help="Password para este userId")

    # Read arguments from command line
    args = parser.parse_args()

    username = args.user
    password = args.pw

    print(f"Userid = \'{username}\', password =\'{password}\'")

    if args.user:
        print(f"Userid1 = \'{username}\', password1 =\'{password}\'")
    else:
        username = 'default'
        password = 'default'
