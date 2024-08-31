# purpose: describe your command's purpose...
# command: describe the command

# import dependencies
# import sys


# import templates and config
from utils.config_manager import Util as config_manager_util

get_config = config_manager_util.get_config
plugin_config = config_manager_util.get_plugin_config("smyk07/pandoc-vinotes")


# write utility class
class Util:
    def __init__(self, command_args=[]) -> None:
        self.name = "export"
        self.docstring = """Exports the provided or chosen file into a PDF document"""
        # completely optional:
        self.extended_docstring = """
Usage: 

- [bright-green]vn export <filepath>[/]
- [bright-green]vn export (opens fuzzy finder)[/]

Converts the given file or chosen file into PDF and saves into the directory provided in config. This is a part of the plugin smyk07/pandoc-vinotes.
This basically integrates pandoc into vinotes.
        """
        self.util_type = "command"
        self.command_args = command_args

    def command(self):
        # write your command here
        pass  # delete this line


# write helper functions here (delete the code below obv)
# def helper_func1():
#     pass

# test file if run as main.
if __name__ == "__main__":
    pass  # testing code goes here.
