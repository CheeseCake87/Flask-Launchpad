from ....builtins.functions.security import login_required
from .. import bp
from .. import struc
from flask import request
from flask import current_app
from flask import render_template
from flask_sqlalchemy import SQLAlchemy


@bp.route("/settings", methods=["GET"])
def settings():
    render = "renders/settings.html"
    structure = struc.name()
    extend = struc.extend("backend.html")
    footer = struc.include("footer.html")

    return render_template(render, structure=structure, extend=extend, footer=footer)