"""
pymake
-------------------------------

pymake package

 - E. Marinetto
 - nenetto@gmail.com
"""

import json
from pprint import pprint
from tabulate import tabulate
import sys

# Vars file
# This file contains useful variables for project configuration
project_vars={
 'author': 'E. Marinetto',
 'author-email': 'nenetto@gmail.com',
 'docker-tag': '',
 'git-repo': 'https://github.com/nenetto/pymake.git',
 'project-description': 'pymake package',
 'project-name': 'pymake',
 'project-version-major': 2,
 'project-version-minor': 5,
 'pymake-version': 2.5,
 'type-of-project': 'python'
}


class PrettyMessaging:

    color_codes = {
        # Reset
        'Color_Off': '\033[0m',      # Text Reset

        # Regular Colors
        'Black': '\033[0;30m',        # Black
        'Red': '\033[0;31m',          # Red
        'Green': '\033[0;32m',        # Green
        'Yellow': '\033[0;33m',       # Yellow
        'Blue': '\033[0;34m',         # Blue
        'Purple': '\033[0;35m',       # Purple
        'Cyan': '\033[0;36m',         # Cyan
        'White': '\033[0;37m',        # White

        # Bold
        'BBlack': '\033[1;30m',       # Black
        'BRed': '\033[1;31m',         # Red
        'BGreen': '\033[1;32m',       # Green
        'BYellow': '\033[1;33m',      # Yellow
        'BBlue': '\033[1;34m',        # Blue
        'BPurple': '\033[1;35m',      # Purple
        'BCyan': '\033[1;36m',        # Cyan
        'BWhite': '\033[1;37m',       # White

        # Underline
        'UBlack': '\033[4;30m',       # Black
        'URed': '\033[4;31m',         # Red
        'UGreen': '\033[4;32m',       # Green
        'UYellow': '\033[4;33m',      # Yellow
        'UBlue': '\033[4;34m',        # Blue
        'UPurple': '\033[4;35m',      # Purple
        'UCyan': '\033[4;36m',        # Cyan
        'UWhite': '\033[4;37m',       # White

        # Background
        'On_Black': '\033[40m',       # Black
        'On_Red': '\033[41m',         # Red
        'On_Green': '\033[42m',       # Green
        'On_Yellow': '\033[43m',      # Yellow
        'On_Blue': '\033[44m',        # Blue
        'On_Purple': '\033[45m',      # Purple
        'On_Cyan': '\033[46m',        # Cyan
        'On_White': '\033[47m',       # White

        # High Intensity
        'IBlack': '\033[0;90m',       # Black
        'IRed': '\033[0;91m',         # Red
        'IGreen': '\033[0;92m',       # Green
        'IYellow': '\033[0;93m',      # Yellow
        'IBlue': '\033[0;94m',        # Blue
        'IPurple': '\033[0;95m',      # Purple
        'ICyan': '\033[0;96m',        # Cyan
        'IWhite': '\033[0;97m',       # White

        # Bold High Intensity
        'BIBlack': '\033[1;90m',      # Black
        'BIRed': '\033[1;91m',        # Red
        'BIGreen': '\033[1;92m',      # Green
        'BIYellow': '\033[1;93m',     # Yellow
        'BIBlue': '\033[1;94m',       # Blue
        'BIPurple': '\033[1;95m',     # Purple
        'BICyan': '\033[1;96m',       # Cyan
        'BIWhite': '\033[1;97m',      # White

        # High Intensity backgrounds
        'On_IBlack': '\033[0;100m',   # Black
        'On_IRed': '\033[0;101m',     # Red
        'On_IGreen': '\033[0;102m',   # Green
        'On_IYellow': '\033[0;103m',  # Yellow
        'On_IBlue': '\033[0;104m',    # Blue
        'On_IPurple': '\033[0;105m',  # Purple
        'On_ICyan': '\033[0;106m',    # Cyan
        'On_IWhite': '\033[0;107m',   # White
    }

    print_colors = {
        '1': color_codes['BIGreen'],
        '2': color_codes['Yellow'],
        '3': color_codes['BIBlue'],
        'warningH': color_codes['On_Green'] + color_codes['BBlack'],
        'warning': color_codes['Green'],
        'errorH': color_codes['On_Red'] + color_codes['BBlack'],
        'error': color_codes['Red'],
        'off': color_codes['Color_Off']
    }

    @staticmethod
    def project_header():
        header = PrettyMessaging.print_colors['1'] + '[' + project_vars['project-name'] + ']' + PrettyMessaging.print_colors['off']
        separator = PrettyMessaging.print_colors['1'] + ': ' + PrettyMessaging.print_colors['off']
        return header, separator

    @staticmethod
    def print_info(msg):
        header, separator = PrettyMessaging.project_header()
        header_info = header + PrettyMessaging.print_colors['1'] + '[   info]' + PrettyMessaging.print_colors['off'] + separator
        msg = header_info + PrettyMessaging.print_colors['2'] + msg + PrettyMessaging.print_colors['off']
        print(msg)

    @staticmethod
    def print_error(msg):
        header, separator = PrettyMessaging.project_header()
        header_info = header + PrettyMessaging.print_colors['errorH'] + '[#error#]' + PrettyMessaging.print_colors['off'] + separator
        msg = header_info + PrettyMessaging.print_colors['error'] + msg + PrettyMessaging.print_colors['off']
        print(msg)

    @staticmethod
    def print_warning(msg):
        header, separator = PrettyMessaging.project_header()
        header_info = header + PrettyMessaging.print_colors['warningH'] + '[warning]' + PrettyMessaging.print_colors['off'] + separator
        msg = header_info + PrettyMessaging.print_colors['warning'] + msg + PrettyMessaging.print_colors['off']
        print(msg)

    @staticmethod
    def print_separator(size = 67):
        msg = PrettyMessaging.print_colors['2'] + '-'*size + PrettyMessaging.print_colors['off']
        print(msg)

    @staticmethod
    def print_json(path):
        example_conf = json.load(open(path))

        PrettyMessaging.print_separator()
        print(PrettyMessaging.print_colors['2'])
        pprint(example_conf)
        print(PrettyMessaging.print_colors['off'])
        PrettyMessaging.print_separator()

    @staticmethod
    def print_table(df, n=None):
        if n is None:
            n = 5

        print(PrettyMessaging.print_colors['2'])
        print(tabulate(df.head(n), headers='keys', tablefmt='psql'))
        print(PrettyMessaging.print_colors['off'])

    @staticmethod
    def print_info_percentage(percentage, msg_pre='', msg_post=''):

        header, separator = PrettyMessaging.project_header()
        header_info = header + PrettyMessaging.print_colors['1'] + '[   info]' +\
                      PrettyMessaging.print_colors['off'] + separator
        msg = header_info + PrettyMessaging.print_colors['2'] + msg_pre + PrettyMessaging.print_colors['off']

        msg += PrettyMessaging.print_colors['3'] +\
               ': [ {0:.2f} %]-'.format(percentage) +\
               PrettyMessaging.print_colors['2'] + \
               msg_post + \
               PrettyMessaging.print_colors['off']

        if percentage >= 100:
            str1 = "\r{0}\n".format(msg)
        else:
            str1 = "\r{0}".format(msg)

        sys.stdout.write(str1)
        sys.stdout.flush()
