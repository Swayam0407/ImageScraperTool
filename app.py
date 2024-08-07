from flask import Flask, render_template, request, redirect, url_for
from icrawler.builtin import BingImageCrawler
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    keyword = request.form['keyword']
    limit = int(request.form['limit'])
    
    output_dir = os.path.join('images', keyword)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    bing_crawler = BingImageCrawler(storage={'root_dir': output_dir})
    bing_crawler.crawl(keyword=keyword, max_num=limit)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
