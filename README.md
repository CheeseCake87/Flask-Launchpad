# Flask-Launchpad

```bash
pip install flask-launchpad
```

---

## Setup GitHub version

! This project imports Flask-Launchpad from a local directory (_flask_launchpad) !

### Linux setup

(Assuming location is home directory)

#### Git clone:

```bash
git clone https://github.com/CheeseCake87/Flask-Launchpad.git
```

```bash
cd Flask-Launchpad
```

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

```bash
pip install -r requirements.txt
```

#### Manual:

1. Download zip and unpack
2. cd into unpacked folder

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

```bash
pip install -r requirements.txt
```

---

# What is Flask-Launchpad?

Flask-Launchpad's main purpose is to help simplify the importing of blueprints, templates and models.

It has a few extra features built in to help with theming, securing pages and password authentication.

## Minimal Flask-Launchpad app

```app_config.toml``` file is required to sit next to your app's ```__init__.py``` file.

The ```app_config.toml``` file contains Flask config settings, a minimal version of this file looks like this:

```toml
# Updates the Flask app config with the variables below.
# If any variable below does not exist in the standard Flask env vars it is created and will be accessible using
# current_app.config["YOUR_VAR_NAME"] or of course, app.config["YOUR_VAR_NAME"] if you are not using app factory.

[flask]
app_name = "main"
version = "0.0.0"
secret_key = "sdflskjdflksjdflksjdflkjsdf"
debug = true
testing = true
session_time = 480
static_folder = "static"
template_folder = "templates"
error_404_help = true
```

Your app's ```__init__.py``` file should look like this:

```python
from flask import Flask
from flask_launchpad import FlaskLaunchpad

fl = FlaskLaunchpad()


def create_app():
    main = Flask(__name__)
    fl.init_app(main)
    fl.app_config("app_config.toml")
    fl.import_builtins("routes")
    return main
```

The ```fl.import_builtins("routes")``` method looks in the ```routes``` folder for ```.py``` files to import app routes
from.

Let's say we have this folder structure:

```
Flask-Launchpad
    main
        static
        templates
        routes
            index.py
        __init__.py
        app_config.toml
    venv
    run.py
```

The ```index.py``` file should look like this:

```python
from flask import current_app


@current_app.route("/", methods=['GET'])
def index_page():
    """
    Example index route
    """
    return "You will see this text in the browser"
```

This file will get imported into the main app using the ```import_builtins()```method.

This is also the case if we add another file into the ```routes``` folder. Let's say we add ```my_page.py``` into the
routes folder, and it looks like this:

```python
from flask import current_app


@current_app.route("/my-page", methods=['GET'])
def my_page():
    """
    My Page Route
    """
    return "This is my page route"
```

So now our folder structure looks like this:

```
Flask-Launchpad
    main
        static
        templates
        routes
            index.py
            my_page.py
        __init__.py
        app_config.toml
    venv
    run.py
```

The ```my_page.py``` routes will also be imported into the main app.

Using this method you can keep your routes in different files, and not have to worry about adding the import into
your ```__init__.py``` file.

This is an example of a very basic app in Flask-Launchpad.

Please check out the Flask-Launchpad GitHub project. It contains working examples of what Flask-Launchpad can do, and
how it can be used to save some time with projects that require a lot of importing.

More documentation coming soon!