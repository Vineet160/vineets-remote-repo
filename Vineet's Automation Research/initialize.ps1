remove -Item venvironment -Force -Recurse
pip install virtualenv
virtualenv -p C:\Python36\python.exe venvironment
venvironment\Scripts\activate
pip install -r requirement.txt