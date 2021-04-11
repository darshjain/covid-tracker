# covid-tracker

## Installation
1. Fork the repository.
2. Clone the repository to your local computer and change directory.
```
git clone https://github.com/<your-username>/covid-tracker.git
cd covid-tracker
```

3. Create a virtual environment to install packages (recommended).
```
python -m venv myvenv
```

4. Install Django and all packages.
```
pip install -r requirements.txt
```

5. Set environment variables.
```
cp .env.example .env
```
Now, edit `.env` to add `RAPI_KEY` from your [RapidApi Dashboard](https://rapidapi.com/developer/dashboard) for your app and a new `SECRET_KEY` for your Django project ([Read more](https://docs.djangoproject.com/en/3.1/ref/settings/#std:setting-SECRET_KEY)).

6. Start project.
```
python manage.py runserver
```
