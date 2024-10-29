def test_login(login_page):
    login_page.login("standard_user", "secret_sauce")
    assert "inventory" in login_page.driver.current_url