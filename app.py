from main import create_app

# if need test change controller to test
blueprints = ['main.controller:v1', ]
# if need test change development to testing
app = create_app('development', blueprints)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5555)
