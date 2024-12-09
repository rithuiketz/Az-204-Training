#from src.utils.business_service import sum
from pytest import fixture
from flask import Flask
from app import app



@fixture
def test_app():
    app.config.update({"TESTING":True})
    yield app

@fixture()
def client(test_app):
    return app.test_client()
    
@fixture()
def runner(test_app):
    return app.test_cli_runner()


def test_api_get_check(client):
    client_ =  client
    resp = client_.get("/envs")
    assert resp.status_code ==200
