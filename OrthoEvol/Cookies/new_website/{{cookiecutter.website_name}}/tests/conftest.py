# -*- coding: utf-8 -*-
"""Defines fixtures available to all tests."""

import pytest
from webtest import TestApp

from {{cookiecutter.website_name}}.app import create_app
from {{cookiecutter.website_name}}.database import db as _db
from {{cookiecutter.website_name}}.settings import TestConfig

from .factories import UserFactory


@pytest.yield_fixture(scope='function')
def app():
    """An application for the tests."""
    _app = create_app(TestConfig)
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture(scope='function')
def testapp(app):
    """A Webtest app.

    :param app: 

    """
    return TestApp(app)


@pytest.yield_fixture(scope='function')
def db(app):
    """A database for the tests.

    :param app: 

    """
    _db.app = app
    with app.app_context():
        _db.create_all()

    yield _db

    # Explicitly close DB connection
    _db.session.close()
    _db.drop_all()


@pytest.fixture
def user(db):
    """A user for the tests.

    :param db: 

    """
    user = UserFactory(password='myprecious')
    db.session.commit()
    return user
