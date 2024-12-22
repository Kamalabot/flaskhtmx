from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

# Sample data - in a real app, this would be a database
ITEMS = [
    "Python Programming",
    "Flask Framework",
    "HTMX Library",
    "Web Development",
    "JavaScript Basics",
    "HTML & CSS",
    "Database Design",
    "API Development",
    "Frontend Development",
    "Backend Development"
]

@app.route('/get-time')
def get_time():
    return datetime.now().strftime("%H:%M:%S")

@app.route('/search')
def search():
    query = request.args.get('search', '').lower()
    if not query:
        return '<div class="search-results">Type to search...</div>'
    
    matches = [item for item in ITEMS if query in item.lower()]
    
    if not matches:
        return '<div class="search-results">No matches found</div>'
    
    results = '<div class="search-results"><ul>'
    for item in matches:
        results += f'<li>{item}</li>'
    results += '</ul></div>'
    return results

@app.route('/')
def index():
    return open('index.html').read()

if __name__ == '__main__':
    app.run(debug=True)