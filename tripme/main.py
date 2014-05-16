# -*- coding: utf-8 -*-


"""TripMe
...my way how to survive TripIt without LSD

Usage:
    tripme
    tripme setup
    tripme -h|--help
    tripme --version

Options:
    setup               Interactive setup.
    -h --help           Show this screen.
    --version           Show tripme version.
"""


from docopt import docopt

from tripme import __version__


def main():
    args = docopt(__doc__, version=__version__)
    try:
        if args.get('setup'):
            raise NotImplementedError('setup')
        else:
            raise NotImplementedError('main')

    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
