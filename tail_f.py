import sh
import re

from typing import Iterator, Optional
from server import server


def ansi_escape(line: str) -> str:
    escape = re.compile(r'(?:\x1B[@-_]|[\x80-\x9F])[0-?]*[ -/]*[@-~]')
    return escape.sub('', line)


def tail_f(file: str) -> Iterator[Optional[str]]:
    try:
        for line in server.tail('-f', file, _iter=True):
            yield ansi_escape(line.rstrip())
    except sh.ErrorReturnCode_1:
        yield None


if __name__ == '__main__':
    for line in tail_f('/var/log/miner/t-rex/t-rex.log'):
        print(line)

        with open('logs.txt', 'a') as f:
            f.write(f"{line}\n")
            f.close()
