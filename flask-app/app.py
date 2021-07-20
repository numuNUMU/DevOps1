from flask import Flask, render_template

app = Flask(__name__)

book_data = {
    1: { "name": "적정한 삶", "info":{ "author" : "김경일", "publisher": "진성북스"} , "comment" : "따뜻하게 힘을 주는 책", "image": "static/img/jacaranda.jpg"}, 
    2: { "name": "신경끄기의 기술", "info":{ "author" : "마크 맨슨", "publisher": "갤리온" }, "comment" : "냉소적이지만 힘을 주는 책", "image": "static/img/rose.jpg"}
}

@app.route('/')
def index():
    return render_template("index.html", template_books = book_data)

@app.route("/book/<int:id>")
def book(id):
    return render_template( "book.html",
                           template_name = book_data[id]["name"],
                           template_info = book_data[id]["info"],
                           template_comment = book_data[id]["comment"],
                           template_image = book_data[id]["image"])

if __name__ == '__main__':
    app.run(host='0.0.0.0')