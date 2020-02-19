from src import create_app


if __name__ == '__main__':
    app_env = 'development'
    app = create_app(app_env)
    app.run()