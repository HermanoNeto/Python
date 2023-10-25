from flask import Flask
import random

app = Flask(__name__)
CORRECT_NUMBER = random.randint(0,9)
print(CORRECT_NUMBER)

@app.route("/")
def hello_world():
    return """
    <h1 style='text-align: center; color: white;'>Guess a number between 0 and 9</h1>

    <img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif class=center>

    <div class=div>
        <a href="/0">0</a>
        <a href="/1">1</a>
        <a href="/2">2</a>
        <a href="/3">3</a>
        <a href="/4">4</a>
        <a href="/5">5</a>
        <a href="/6">6</a>
        <a href="/7">7</a>
        <a href="/8">8</a>
        <a href="/9">9</a>
    </div>

    <style>
        .div {
            text-align:center;
            padding-top:20px;
        }

        body {
            background-color: black;
        }
    
        .center {
            display: block;
            margin-left: auto;
            margin-right: auto;;
        }
</style>

    """
@app.route("/<number>")
def numberCorrector(number):
    if int(number) == CORRECT_NUMBER:
        return """
        <h1 style= 'color:green;'>You Found Me</h1>
        <img src=https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif>
        <a href="/">Home</a>
        """
    elif int(number) < CORRECT_NUMBER:
        return """
        <h1 style= 'color:red;'>Too Low, Try Again</h1>
        <img src=https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif>
        <a href="/">Home</a>
        """
    else:
        return """
        <h1 style= 'color:purple;'>Too High, Try Again</h1>
        <img src=https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif>
        <a href="/">Home</a>
        """





if __name__ == "__main__":
    app.run(debug=True)