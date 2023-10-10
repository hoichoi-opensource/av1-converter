from flask import Flask, render_template, request, redirect, url_for
import main

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        filename = request.form['filename']
        main.download_file(filename)
        output_filename = main.convert_to_av1(filename)
        main.calculate_scores(output_filename)
        main.upload_file(output_filename)
        return f"File Converted: {output_filename}"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
