import os
import tempfile

import pytest

from app import app
from app import db

@pytest.fixture
def client():
    db_path = tempfile.mkstemp()
    test_app = app({'DATABASE': db_path})
    with test_app.test_client() as client:
        with test_app.context():
            init_db()
        yield client
os.close(db_fd)
os.unlink(db_path)
