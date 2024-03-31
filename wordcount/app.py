from flask import Flask, render_template, request

app = Flask(__name__)

def count_words(text):
    # Split the text into words
    words = text.split()
    # Count the number of words
    word_count = len(words)
    return word_count

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        text = request.form['text']
        if not text:
            return render_template('index.html', error="Please enter some text.")
        
        word_count = count_words(text)
        return render_template('result.html', text=text, word_count=word_count)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
