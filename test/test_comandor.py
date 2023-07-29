from comandor.settings import newConfig
from comandor.app import App

import unittest
import os


class TestCore(unittest.TestCase):

    def test_ymlAction(self):
        App(newConfig(
            "./log.log",
            "test_comandor.yml",
            True,
            "",
        )).Run()

    def test_Skip(self):
        App(newConfig(
            "./log.log",
            "test_comandor.json",
            True,
            "test",
        )).Run()


if __name__ == '__main__':
    unittest.main()
