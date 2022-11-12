# Welcome to Lumiere brillianté!

## Sources:

```
https://learn.co/lessons/sqlalchemy-alembic-migrations
https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login
```

## Environment:

Create a virtual environment inside your application folder but outside the project folder. In this case inside user-authentication folder. Run the following to do it:

``` 
python3 -m venv {env name, possibly env}
```

## Libraries and packages

install the following packages:
```
flask
flask-sqlalchemy
flask-login
```

Do so by running the following command:

```
pip install flask flask-sqlalchemy flask-login
```

## create a database:

For handling the database, we will be using Alembic, which will be handling our database and its migrations. 

# Alembic: 

## Installation:
    
    Run the following pip command in your terminal:
    ```
    pip install alembic
    ```

## Creating the Database

    We always need a database for organising the data. Else, the data ends up being confusing, and the computer is a pretty primitive by itself without parameters. So its always best to have a database for the sake of simplicity. In this case, we will be running the following commands. Go to your models.py, and below your models, type the following command:
    ```
    engine = create_engine('sqlite:///db.sqlite')
    Base.metadata.create_all(engine)
    ```
    After this, in the folder named instance, you should see the file named db.sqlite

    Now, go to your terminal and run the following:
    ```
    alembic init alembic
    ```

    Now you should see a new directory, or an environment named alembic. Go to alembic.ini in your main folder, outside /projects and near line 58 you should see the following line: 
    ```
    sqlalchemy.url = driver://user:pass@localhost/dbname
    ```
    and REPLACE THAT LINE WITH:
    ```
    sqlalchemy.url = sqlite:///db.sqlite
    ```

## Migrations:

To initialise your migrations, run the following command:
```
alembic revision -m "baseline"
```

Now you should see a migration file inside alembic/versions/{some_random_id}_baseline.py
Now in the file you should see something like this:
```
from alembic import op
import sqlalchemy as sa

def upgrade():
    pass

def downgrade():
    pass
```

Now, make it into something like this by replicating YOUR PREXISTING MODELS IN model.py

```
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'User',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String()),
        sa.Column('password', sa.String()),
        sa.Column('name', sa.String())
        )


def downgrade():
    op.drop_table('User')
```

## Final touches:

To execute your final migration, run the following command in the terminal

```
python alembic upgrade head
```

## Note:

Remember, to move back a to the previous migration, in case you did something wrong, run 

```
alembic downgrade -1
```