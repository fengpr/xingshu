from xingshu_desktop.app.bootstrap import create_application


def test_create_application() -> None:
    app = create_application()
    assert app is not None

