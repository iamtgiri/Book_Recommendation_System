from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load pickle files with error handling
try:
    popular_df = pickle.load(open('popular.pkl', 'rb'))
    pt = pickle.load(open('pt.pkl', 'rb'))
    books = pickle.load(open('books.pkl', 'rb'))
    similarity_score = pickle.load(open('similarity_score.pkl', 'rb'))
except FileNotFoundError as e:
    print(f"Error: {e}")
    exit()
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    exit()

@app.route('/')
def index():
    return render_template('index_final.html',
                           book_name=list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           publisher=list(popular_df['Publisher'].values),
                           year_published=list(popular_df['Year-Of-Publication'].values),
                           cover_image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['Num-Rating'].values),
                           avg_rating=list(popular_df['Avg-Rating'].values)
                           )


@app.route('/recommend')
def recommend():
    return render_template('recommend_final.html')


@app.route('/recommend_books', methods=['POST'])
def recommend_books():
    user_input = request.form.get('user_input').strip().lower()  # Normalize the input to lowercase

    # Check if input is empty
    if not user_input:
        return render_template('recommend_final.html', error="Input cannot be empty.")
    
    # Exact match first (case insensitive)
    if user_input in pt.index.str.lower():  # Using lower() to compare case-insensitively
        index = np.where(pt.index.str.lower() == user_input)[0][0]
        got = True
    else:
        index = None
        for book in books['Book-Title']:
            if user_input.lower() in book.strip().lower():
                try:
                    index = np.where(pt.index == book)[0][0]
                except:
                    pass
                if index:
                    got = False
                    break
        if not index:
            return render_template('recommend_final.html', error="No matching book found.")

    # Find similar items
    if got:
        similar_items = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:5]
    else:
        similar_items = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[0:4]
        
    suggestion = []
    for i in similar_items:
        temp_df = books[books['Book-Title'] == pt.index[i[0]]].drop_duplicates('Book-Title')
        if not temp_df.empty:
            item = list(temp_df[['Book-Title', 'Book-Author', 'Image-URL-M', 'Year-Of-Publication', 'Publisher']].values[0])
            suggestion.append(item)
    
    if not suggestion:
        return render_template('recommend_final.html', error="No recommendations found.")
    
    return render_template('recommend_final.html', data=suggestion)



@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/send_message', methods=['POST'])
def send_message():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    
    if not (name and email and message):
        return render_template('contact.html', error="All fields are required.")
    
    try:
        with open('messages.txt', 'a') as file:
            file.write(f"""Name    : {name}
Email   : {email}
Message : {message}
--------------------------------------------------

""")
    except IOError as e:
        return "An error occurred while saving your message. Please try again later."

    return render_template('thank_you.html')


if __name__ == '__main__':
    app.run(debug=True)
