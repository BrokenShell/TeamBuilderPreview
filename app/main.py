from math import ceil

from flask import Flask, render_template, request


APP = Flask(__name__)


@APP.route("/", methods=["GET", "POST"])
def home():
    n_web = int(request.values.get("n_web", "40"))
    n_ds = int(request.values.get("n_ds", "20"))

    web_teams = ceil(n_web / 8)
    ds_teams = ceil(n_ds / 6)
    web_only = web_teams - ds_teams

    ave_web = round(n_web / web_teams, 2)
    ave_ds = round(n_ds / ds_teams, 2)

    return render_template(
        "index.html",
        n_web=n_web,
        n_ds=n_ds,
        web_only=web_only,
        ds_teams=ds_teams,
        web_teams=web_teams,
        ave_web=ave_web,
        ave_ds=ave_ds,
    )


if __name__ == '__main__':
    APP.run()
