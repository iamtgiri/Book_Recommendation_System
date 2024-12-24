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

*(If these files are too large for GitHub, host them externally and provide download instructions.)*

### 4️⃣ Run the Flask Application
Start the application by running:
```bash
$ python app.py
```
The app will be live at `http://127.0.0.1:5000/`.

---

## 📖 Usage
1. Enter a book title in the input field on the homepage.
2. The system will recommend similar books based on your input.
3. Explore the details of each recommended book, including the cover image.

---

## ⚙️ Key Technologies
- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Data Handling:** pandas, NumPy
- **Modeling:** Collaborative Filtering

---

## 🗂️ Dataset
- **Books Dataset:** Contains information such as book titles, authors, publishers, year of publication, and cover images.
- **Similarity Scores:** Precomputed matrix of cosine similarity scores for efficient recommendations.

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
Special thanks to the creators of the dataset and the open-source libraries that made this project possible.

---

### 🔗 Connect
- GitHub: [iamtgiri](https://github.com/iamtgiri)

Feel free to explore and enjoy the recommendations! 📚✨
