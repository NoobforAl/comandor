from typing import Tuple, List

import argparse


def read_args() -> Tuple[str, str, bool, List[str, str]]:
    parser = argparse.ArgumentParser()

    parser.add_argument('-l', "--logfile", type=str,
                        default="", help='where save logfile')
    parser.add_argument('-c', "--config", type=str, default=".comandor",
                        help='where you have config file')
    parser.add_argument('-d', "--debug", action='store_true',
                        required=False, help='run debug mod')
    parser.add_argument('-sk', "--skip", default="0-0",
                        required=False, help='run debug mod')

    args = parser.parse_args()
    logfile: str = args.logfile
    config: str = args.config
    debug: bool = args.debug
    skip: List[str, str] = args.skip.split("-")
    return (logfile, config, debug, skip)


__all__ = [
    "read_args",
]
