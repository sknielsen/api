from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def warmer_or_colder():
    return render_template('warmer.html')

@app.route('/answer')
def answer():
    answer = 'warmer'
    image = '/static/sun.png'
    alt = 'sun'
    return render_template('answer.html', answer=answer, image=image, alt=alt)

if __name__ == "__main__":
      app.run(debug=True)
