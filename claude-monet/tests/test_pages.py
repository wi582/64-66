import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()


@pytest.mark.parametrize("path", ["/", "/menu", "/about", "/contact", "/login", "/health"])
def test_pages_return_200(client, path):
    assert client.get(path).status_code == 200


def test_home_has_welcome(client):
    assert b"Welcome to our restaurant" in client.get("/").data


def test_menu_has_sections(client):
    html = client.get("/menu").data
    assert b"Dessert" in html and b"Salty" in html and b"Chocolate croissant" in html


def test_about_has_six_chefs(client):
    assert client.get("/about").data.count(b'class="photo"') == 6


def test_unknown_page_404(client):
    assert client.get("/nope").status_code == 404
