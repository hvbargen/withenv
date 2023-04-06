# withenv
A very simple tool executing commands with a given environment.
This uses python-dotenv internally and is just a tiny wrapper.
Loads the .env file with load_dotenv(), then executes the arguments as a command-line.

## Installing dependencies

    py -m pip install -r requirements.txt

## Installing

    pip install flit
    flit install

## Configuration

Edit the `.env` file (it is UTF-8 encoded) and enter a valid email address.

## Running

    withenv echo %DATEINAME%

Note: The variable was read from the .env file.

    set DATEINAME=xyz
    withenv echo %DATEINAME%

Note: The environment variable will not be not ovveridden.


