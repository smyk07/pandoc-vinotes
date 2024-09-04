# purpose: describe your command's purpose...
# command: describe the command

# import dependencies
import sys
import subprocess
from pathlib import Path


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
        self.command_args = " ".join(command_args)

    def command(self):
        if self.command_args == "":
            try:
                dirs = " ".join([i for i in get_config("principle_dirs")])
                file_path = Path(
                    subprocess.check_output(
                        f"find ./ {dirs} \\( -iname '*.md' \\) -type f 2>/dev/null | fzf",
                        shell=True,
                        executable=f"{get_config('shell_executable')}",
                    ).decode("utf-8")[:-1]
                )
            except subprocess.CalledProcessError:
                quit()
        else:
            file_path = Path(self.command_args)

            if not file_path.is_file():
                print("File does not exist...")
                quit()

        print("Exporting to PDF...")
        subprocess.run(
            f"pandoc -o ./{plugin_config['opts']['default_export_dir']}/{str(file_path).split('/')[-1][:-3]}.pdf {str(file_path)}",
            shell=True,
            executable=get_config("shell_executable"),
        )
        print("Done!")


# write helper functions here (delete the code below obv)
# def helper_func1():
#     pass

# test file if run as main.
if __name__ == "__main__":
    test_util = Util(sys.argv[1:])
    test_util.command()
