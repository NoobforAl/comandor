from comandor import settings
from comandor import models
from comandor import main


import unittest


class TestCore(unittest.TestCase):

    def test_loadSetting(self):
        with self.assertRaises(settings.ValidationError):
            settings.loadSetting("./comandor_break.json")

    def test_modelAction(self):
        # raise error for commands type
        with self.assertRaises(settings.ValidationError):
            models.Action(
                action_name="test ",
                path=".",
                commands=""
            )

    def test_modelSetting(self):
        # raises error for action type
        with self.assertRaises(settings.ValidationError):
            models.Setting(
                name="test ",
                actions=[""]
            )

    def test_main(self):
        setting = main.newConfig(
            logfile="",
            config="test_comandor.json",
            debug=True
        )
        # if action return 1 status code assert!
        self.assertEqual(0,  main.runActions(setting.actions))


if __name__ == '__main__':
    unittest.main()
