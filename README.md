# paisaiq-backend


### Scripts
For creating requirements.txt -> store where all the installed libraries will be saved
    pip freeze > requirements.txt

For installing all the packages from requirements.txt file
    pip install -r requirements.txt

For generating migrations
    alembic revision --autogenerate -m "Initial migration"

For Applying migrations
    alembic upgrade head