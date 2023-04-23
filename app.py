from flask import Flask, render_template, request, send_file
from pytube import YouTube
import os

app = Flask(__name__)
app.config['OUTPUT_FOLDER'] = 'outputs'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        url = request.form['url']
        try:
            video = YouTube(url)
            title = video.title
            thumbnail = video.thumbnail_url
            return render_template('search.html', url=url, title=title, thumbnail=thumbnail)
        except:
            return render_template('search.html', error='Invalid URL')
    else:
        return render_template('search.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    video = YouTube(url)
    title = video.title
    streams = video.streams.filter(only_audio=True)
    filename = f"{title}.mp3"
    path = os.path.join(app.config['OUTPUT_FOLDER'], filename)
    streams.first().download(output_path=app.config['OUTPUT_FOLDER'], filename=filename)
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
