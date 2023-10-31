from app import create_app

app = create_app("prd")




if __name__ == '__main__':
    with app.app_context():
        # Inside this block, you can access app and related resources
        app.run()