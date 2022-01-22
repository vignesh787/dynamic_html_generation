from flask import Flask, render_template, request

app =  Flask(__name__)

@app.route('/',methods=["GET","POST"])


def generate():
    if request.method=='POST':
        topic = request.form.get('Topic')
        subTopic = request.form.get('SubTopic')
        content = request.form.get('Content')
        image = request.form.get('Image')
        link = request.form.get('Link')
        template = f"""

            <div id="container-1">
            <h1>{ topic }</h1>
            <h2>{ subTopic } </h2>
            </div>
            <div id="container-2">
            <p id="back"> {content}
            </p>

            <h3> Image </h3>
            <img src='static/{image} alt="DS2.jpeg">
            <p id ="inlinepara">
            </p></div>

            <div id="container-3">
            <h3> Additional Information </h3>
            <a href={link}>More Info Here </a>
            </div>


        """

        final = "{% extends 'base.html' %} {% block main %}" + template + "{% endblock %}"

        file=open(f'templates/{topic}.html', 'w')
        file.write(final)
        file.close()
        return render_template(f'{topic}.html')
    return render_template('add.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)





