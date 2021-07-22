

# https://stackoverflow.com/questions/25501403/storing-the-secrets-passwords-in-a-separate-file
# https://stackoverflow.com/questions/7014953/i-need-to-securely-store-a-username-and-password-in-python-what-are-my-options

from mycredentials import sys_stg, sys_db
import mysystemlib


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    mysystemlib.system_login(sys_stg)

#
# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
