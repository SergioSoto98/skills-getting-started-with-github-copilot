import copy
import pytest
from fastapi.testclient import TestClient
import src.app as app_module


@pytest.fixture
def client():
    return TestClient(app_module.app)


@pytest.fixture(autouse=True)
def isolate_activities():
    # Make a deep copy of in-memory activities and restore after each test
    original = copy.deepcopy(app_module.activities)
    try:
        yield
    finally:
        app_module.activities.clear()
        app_module.activities.update(original)
