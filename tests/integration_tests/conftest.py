import sqlite3
import pytest


@pytest.fixture
def session():
    connection = sqlite3.connect('facts_test.db')
    db_session = connection.cursor()
    yield db_session
    connection.close()


@pytest.fixture
# pylint: disable=redefined-outer-name
def setup_db(session):
    session.execute("DROP TABLE IF EXISTS dog_facts")
    session.execute("CREATE TABLE dog_facts (id INTEGER PRIMARY KEY AUTOINCREMENT, fact TEXT)")
    session.execute("INSERT INTO dog_facts (fact) VALUES ('Forty-five percent of U.S. dogs sleep in their owner''s bed'), ('Seventy percent of people sign their dog''s name on their holiday cards'), ('Dogs have about 1,700 taste buds. We humans have between 2,000-10,000')")
    session.connection.commit()
