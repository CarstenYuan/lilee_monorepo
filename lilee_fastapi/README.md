## I use pytest to test my APIs and will provide steps for both Windows and macOS
### Prerequisites:
- Have Python version 3.11 installed
---
### On Windows
1. Create a virtual environment
```
python -m venv venv
```
2. Activate/Enter the virtual environment you just created
```
./venv/Scripts/activate
```

3. Check if you are using the pip inside your virtual environment
```
pip -V
```
The output will show something like this:
pip 2X.X.X from THE_PATH_OF_WHERE_YOU_CLONE_THIS_PROJECT/lilee/lilee_fastapi/venv/Lib/site-packages/pip (python 3.11)

4. Install the necessary packages
```
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

5. Get the current working directory you at
```
pwd
```
The output will show something like this:
THE_PATH_OF_WHERE_YOU_CLONE_THIS_PROJECT/lilee/lilee_fastapi

6. Setup the PYTHONPATH: Copy the above path and paste it to the PYTHONPATH
```
$env:PYTHONPATH="THE_PATH_OF_WHERE_YOU_CLONE_THIS_PROJECT/lilee/lilee_fastapi/src"
```
7. Run tests by pytest
```
pytest
```
You'll see "3 passed"!

---
### On MacOS
1. Create a virtual environment
```
python -m venv venv
```
NOTE: If you have python3.11 installed but it shows "command not found: python"
You might need to use 'python3' instead
```
python3 -m venv venv
```

2. Activate/Enter the virtual environment you just created
```
source venv/bin/activate
```

3. Check if you are using the pip inside your virtual environment
```
pip -V
```

The output will show something like this:
pip 2X.X.X from THE_PATH_OF_WHERE_YOU_CLONE_THIS_PROJECT/lilee/lilee_fastapi/venv/lib/python3.11/site-packages/pip (python 3.11)

4. Install the necessary packages
```
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

5. Setting the PYTHONPATH
```
export PYTHONPATH=.:./src:$PYTHONPATH
```

6. Run tests by pytest
```
pytest
```
You'll see "3 passed"!
