from __future__ import annotations

import argparse
from typing import Sequence


CONFLICT_PATTERNS = [
    b'nocommit',
    b'NOCOMMIT',
    b'no commit',
    b'NO COMMIT',
]


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    parser.add_argument('--assume-in-merge', action='store_true')
    args = parser.parse_args(argv)

    retcode = 0
    for filename in args.filenames:
        with open(filename, 'rb') as inputfile:
            for i, line in enumerate(inputfile):
                for pattern in CONFLICT_PATTERNS:
                    if pattern in line:
                        print(
                            f'{pattern.decode()}" found in {filename}:{i + 1}',
                        )
                        retcode = 1

    return retcode


if __name__ == '__main__':
    raise SystemExit(main())
