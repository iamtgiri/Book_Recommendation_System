# Book Recommendation System

Welcome to the **Book Recommendation System**! This project leverages collaborative filtering to recommend books based on user preferences, using a rich dataset of books and similarity scoring.

---

## 🚀 Features
- **Personalized Book Recommendations:** Suggests similar books based on your input.
- **Interactive Web Interface:** A simple and intuitive UI built with Flask.
- **Detailed Book Information:** Each recommendation includes the title, author, year of publication, publisher, and cover image.

---

## 📂 Project Structure
```

├── templates/
│   ├── index_final.html
│   ├── recommend_final.html
│   ├── contact.html
│   ├── thank_you.html
├── app.py                # Main Flask application
├── books.pkl             # Preprocessed dataset (large file)
├── popular.pkl           # Preprocessed dataset (large file)
├── pt.pkl                # Preprocessed dataset (large file)
├── similarity_score.pkl  # Precomputed similarity scores
├── README.md             # Documentation
├── messages.txt          # Store messages from users
├── requirements.txt      # Python dependencies
```

---

## 🛠️ Installation and Setup

Follow these steps to run the project locally:

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### 1️⃣ Clone the Repository
```bash
$ git clone https://github.com/iamtgiri/Book_Recommendation_System.git
$ cd Book_Recommendation_System
```

### 2️⃣ Install Dependencies
Install the required Python libraries using:
```bash
$ pip install -r requirements.txt
```

### 3️⃣ Add Dataset Files
Ensure the following files are in the project directory:
- `books.pkl`
- `similarity_score.pkl`
- `popular.pkl`
- `pt.pkl`

### 4️⃣ Run the Flask Application
Start the application by running:
```bash
$ python app.py
```
The app will be live at `http://127.0.0.1:5000/`.

---

## 📖 Usage
1. On the homepage, you'll find the top 50 books recommended based on popularity.
2. Navigate to the 'Recommend' tab, where a search bar allows you to enter a book name.
3. Upon entering a book name, the system will display recommended books using a collaborative filtering approach.

---

## ⚙️ Key Technologies
- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Data Handling:** pandas, NumPy
- **Modeling:** Collaborative Filtering

---

## 🗂️ Dataset
- **Books Dataset:** Contains information such as book titles, authors, publishers, year of publication and cover images.
- **Similarity Scores:** Precomputed matrix of cosine similarity scores for efficient recommendations.
- **Popular Dataset:** Contains popular books with higher ratings.
---

## 🤝 Contributing
Contributions are welcome! Feel free to:
- Open an issue for bugs or feature requests.
- Submit a pull request with improvements or fixes.

---

## 📄 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🌟 Acknowledgments

I am sincerely grateful to Nitish Singh (YouTube: [CampusX](https://learnwith.campusx.in/)) for inspiring this project.  
Special thanks to the creators of the dataset and the developers of the open-source libraries that made this project possible.

---

### 🔗 Connect
- GitHub  : [iamtgiri](https://github.com/iamtgiri)
- LinkedIn: [iamtgiri](https://www.linkedin.com/in/iamtgiri/)
  
Feel free to explore and enjoy the recommendations! 📚✨
