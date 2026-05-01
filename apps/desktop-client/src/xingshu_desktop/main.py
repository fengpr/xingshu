from xingshu_desktop.app.bootstrap import create_application


def main() -> int:
    app = create_application()
    return app.run()


if __name__ == "__main__":
    raise SystemExit(main())

