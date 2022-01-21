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
        return "Got the data"+topic
    return render_template('add.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)



