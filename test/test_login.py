

def test_login(app):
    app.session.auth("administrator","root")
    assert app.session.is_logged_in_as("administrator")