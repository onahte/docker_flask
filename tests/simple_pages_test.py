"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/git">Git</a>' in response.data
    assert b'<a class="nav-link" href="/docker">Docker</a>' in response.data
    assert b'<a class="nav-link" href="/python">Python+Flask</a>' in response.data
    assert b'<a class="nav-link" href="/cicd">CI/CD</a>' in response.data
    assert b'<a class="nav-link" href="/oop">OOP</a>' in response.data
    assert b'<a class="nav-link" href="/plint">Pylint</a>' in response.data
    assert b'<a class="nav-link" href="/aaa">AAA</a>' in response.data
    assert b'<a class="nav-link" href="/solid">SOLID</a>' in response.data

def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Project" in response.data

def test_request_git(client):
    """This makes the git page"""
    response = client.get("/git")
    assert response.status_code == 200
    assert b"Git" in response.data

def test_request_docker(client):
    """This makes the docker page"""
    response = client.get("/docker")
    assert response.status_code == 200
    assert b"Docker" in response.data

def test_request_python(client):
    """This makes the python page"""
    response = client.get("/python")
    assert response.status_code == 200
    assert b"Python + Flask" in response.data

def test_request_cicd(client):
    """This makes the cicd page"""
    response = client.get("/cicd")
    assert response.status_code == 200
    assert b"CI/CD" in response.data

def test_request_oop(client):
    """This makes the oop page"""
    response = client.get("/oop")
    assert response.status_code == 200
    assert b"OOP" in response.data

def test_request_aaa(client):
    """This makes the aaa page"""
    response = client.get("/aaa")
    assert response.status_code == 200
    assert b"AAA" in response.data

def test_request_pylint(client):
    """This makes the pylint page"""
    response = client.get("/plint")
    assert response.status_code == 200
    assert b"Pylint" in response.data

def test_request_solid(client):
    """This makes the solid page"""
    response = client.get("/solid")
    assert response.status_code == 200
    assert b"SOLID" in response.data

def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404