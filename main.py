from flask import Flask, request, redirect
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True
form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
    <form action="/" method="post">
        <label for="rot">
            Rotate by
            <input type="text" value="0" id="rot" name="rot"</><br>
            <textarea type="text" name="text">{0}</textarea>                
            <input type="submit" name="Submit"/> 
        </label>
    </form>
    </body>
</html>
""" 


@app.route("/")
def index():
    return form.format('')

@app.route("/", methods=["POST"])
def encrypt():
    caesar_message = request.form['text']
    caesar_rot = request.form['rot']
    caesar_message = str(caesar_message)
    caesar_rot = int(caesar_rot)
    encrypted_message = rotate_string(caesar_message, caesar_rot)


    return form.format(encrypted_message)



app.run()