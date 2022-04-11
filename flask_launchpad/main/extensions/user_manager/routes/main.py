from flask_launchpad.main.builtins.functions.security import login_required
from .. import bp
from .. import Structure
from .. import extmod
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import url_for


@bp.route("/", methods=["GET"])
def index():
    render = "renders/_index.html"
    extend = Structure.location + "base.html"

    return render_template(render, structure=Structure.name, extend=extend)


@bp.route("/logout", methods=["GET", "POST"])
def logout():
    session["example1_auth"] = False
    return redirect(url_for("example1.login"))


@bp.route("/login", methods=["GET", "POST"])
def login():
    """
    Used to test the session set for the login_required decorator.
    """
    if request.method == "POST":
        session["auth"] = True
        return redirect(url_for("example1.account"))

    print(session)
    return f""" 
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Title</title>
</head>
<body>
<form method='post'>
<input type='submit' value='login'/>
</form>
</body>
</html>
    """


@bp.route("/account", methods=["GET"])
@login_required(session_bool_key="auth", on_error_endpoint="example1.login")
def account():
    """
    This page is protected by the login_required decorator, with the login page endpoint set.
    """
    return f"""Account Page {session}"""