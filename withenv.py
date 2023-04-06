"""
{script} uses an .env file and runs a command within this environment.
Does not alter the current environment.

Syntax: {script} whatever_command args...
"""

__version__ = "0.1.1" 

import subprocess
import sys
from dotenv import load_dotenv

load_dotenv()

CMD_COMMANDS = [
    "SET",
    "ECHO",
    "FOR"
]

def run(argv, script="withenv"):
    if not argv:
        print(f"{script}: Missing command argument.", file=sys.stderr)
        print(__doc__.format(**locals()), file=sys.stderr)
        return 2
    first_arg = argv[0]
    use_shell = False
    if first_arg.upper() in CMD_COMMANDS:
        use_shell = True
    return subprocess.call(argv, shell=use_shell)

def main():
    argv = sys.argv[:]
    this_script = argv.pop(0)
    exit(run(argv, this_script))

if __name__ == "__main__":
    main()
