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
    session.execute("INSERT INTO dog_facts (fact) VALUES ('test fact 1'), ('test fact 2'), ('test fact 3')")
    session.connection.commit()
