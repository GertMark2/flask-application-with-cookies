from flask import Flask, request, redirect, url_for, render_template, make_response

app = Flask(__name__)


# Маршрут для установки cookie
# ?language=russian
# ?language=english
# ?language=kazakh

@app.route("/set_cookie", methods=["GET"])
def set_cookie():
    language = request.args.get("language")
    if language:
        response = make_response(redirect(url_for("welcome")))
        response.set_cookie("language", language)
        return response
    else:
        return "Язык не был указан."


# Маршрут для чтения cookie
@app.route("/get_cookie", methods=["GET"])
def get_cookie():
    language = request.cookies.get("language")
    if language:
        return f"Выбранный язык: {language}"
    else:
        return "Язык не был выбран."


# Страница с формой выбора языка
@app.route("/select_language", methods=["GET", "POST"])
def select_language():
    if request.method == "POST":
        language = request.form.get("language")
        response = make_response(redirect(url_for("welcome")))
        response.set_cookie("language", language)
        return response
    else:
        return render_template("select_language.html")


# Маршрут для перенаправления
@app.route("/redirect_example", methods=["GET"])
def redirect_example():
    return render_template("cookie.html")


# Основная страница
@app.route("/")
def welcome():
    language = request.cookies.get("language")
    if language:
        return f"Welcome! Your selected language is {language}."
    else:
        return "Welcome!"


if __name__ == "__main__":
    app.run(debug=True)
