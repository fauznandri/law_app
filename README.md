# How to run
1. Create a virtual environment if you haven't already
```bash
python -m venv env
```
2. Activate the virtual environment
- For Windows
```bash
.\env\Scripts\activate
```
- For Linux or MacOS
```bash
source env/bin/activate
```
3. Install the required packages
```python
pip install -r requirements.txt
```

1. Run the project file
```bash
python manage.py runserver
```

to serve using Waitress
waitress-serve --listen=*:8000 law_app.wsgi:application