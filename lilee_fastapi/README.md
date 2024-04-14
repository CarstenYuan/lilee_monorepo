## I use pytest to test my APIs and will provide steps for both Windows and macOS
### On Windows
- Prerequisites:
    - Have Python version 3.11 installed
- Steps
1. Create and enter a virtual environment
```
Create a virtual environment
> python -m venv venv

Activate/Enter the virtual environment you just created
> ./venv/Scripts/activate

You'll be able to see the name of your current virtual environment at the front of your console
(venv) > 
```
2. Install necessary packages
```
Check if you are using the pip inside your virtual environment
> pip -V

The output will show something like this:
pip 2X.X.X from THE_PATH_OF_WHERE_YOU_CLONE_THIS_PROJECT/lilee/lilee_fastapi/venv/Lib/site-packages/pip (python 3.11)

Install the packages we need
> pip install -r requirements.txt
> pip install -r requirements-dev.txt
```
3. Setting the PYTHONPATH
```
Find out where you at first
> pwd

The output will show something like this:
THE_PATH_OF_WHERE_YOU_CLONE_THIS_PROJECT/lilee/lilee_fastapi

Copy the above path and paste it to the PYTHONPATH
> $env:PYTHONPATH="THE_PATH_OF_WHERE_YOU_CLONE_THIS_PROJECT/lilee/lilee_fastapi/src"
```
4. Run tests by pytest
```
> pytest

You'll see "3 passed"!
```
---
### On MacOS
- Prerequisites:
    - Have Python version 3.11 installed
- Steps
1. Create and enter a virtual environment
```
Create a virtual environment
> python -m venv venv

NOTE: If you have python3.11 installed but it shows "command not found: python"
You might need to use 'python3' instead
> python3 -m venv venv

Activate/Enter the virtual environment you just created
> source venv/bin/activate

You'll be able to see the name of your current virtual environment at the front of your console
(venv) > 
```
2. Install necessary packages
```
Check if you are using the pip inside your virtual environment
> pip -V

The output will show something like this:
pip 2X.X.X from THE_PATH_OF_WHERE_YOU_CLONE_THIS_PROJECT/lilee/lilee_fastapi/venv/lib/python3.11/site-packages/pip (python 3.11)

Install the packages we need
> pip install -r requirements.txt
> pip install -r requirements-dev.txt
```
3. Setting the PYTHONPATH
```
> export PYTHONPATH=.:./src:$PYTHONPATH
```
4. Run tests by pytest
```
> pytest

You'll see "3 passed"!
```
