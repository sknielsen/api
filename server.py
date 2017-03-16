from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return '<html><body><h1>I am the landing page</h1></body></html>'

@app.route('/warmercolder')
def warmer_or_colder():
    return """
<html>
    <head>
        <title>Warmer or Colder</title>
        <link rel="stylesheet" href="/static/warmer.css">
    </head>
    <body>
        <h1>Warmer or Colder</h1>
        <br>
        <p>Will today be warmer or colder than yesterday?</p>
        <form>
            Zip Code<br>
            <input type="text" name="zip code">
            <br>
            <input type="submit" value="Submit">
        </form>
     </body>
</html>"""

@app.route('/warmer')
def warmer():
    return"""
<html>
    <head>
    <link rel="stylesheet" href="/static/warmer.css">
    </head>
    <body>
        <h1>Warmer or Colder</h1>
        <br>
        <p>Will today be warmer or colder than yesterday?</p>
        <br><br>
        <p>It will be warmer than yesterday!</>
        <br>
        <img src="/static/sun.png" alt="Sun">
"""

@app.route('/colder')
def colder():
    return"""
<html>
    <head>
    <link rel="stylesheet" href="/static/warmer.css">
    </head>
    <body>
        <h1>Warmer or Colder</h1>
        <br>
        <p>Will today be warmer or colder than yesterday?</p>
        <br><br>
        <p>It will be colder than yesterday!</>
        <br>
        <br>
        <img src="/static/snowflake.png" alt="Snowflake" style="width:200px;height:200px">
"""

if __name__ == "__main__":
      app.run(debug=True)
