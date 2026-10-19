# Friend Recommendation System

A simple and interactive Friend Recommendation System built using **Python, Pandas, Graph Algorithms, and Streamlit**. It recommends new friends based on mutual connections in a friendship network.

## ✨ Features

- 👥 Explore a network of 100 people.
- 🔗 Build a friendship graph from the dataset.
- 🤝 Recommend new friends using mutual connections.
- 📊 Display the number of mutual connections.
- ⭐ Categorize recommendations into three levels:
  - **Highly Recommended** — More than 5 mutual connections
  - **Good Match** — 3–5 mutual connections
  - **Possible Match** — Fewer than 3 mutual connections
- 🌐 Interactive web interface built with Streamlit.

## 🛠️ Technologies Used

- Python
- Pandas
- Graph Algorithms
- Streamlit

## 📂 Project Structure

```text
Friend-Recommendation-System/
├── app.py
├── friendships_with_names.csv
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd Friend-Recommendation-System
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🧠 How It Works

1. Loads friendship data from a CSV file.
2. Creates an undirected graph representing friendships.
3. Finds friends of a person's existing friends.
4. Excludes the selected person and their existing friends.
5. Counts mutual connections for each potential friend.
6. Ranks recommendations by mutual connections and assigns a recommendation level.

## 📌 Future Improvements

- Search for people by name.
- Display the strongest friend recommendations first.
- Visualize the friendship network.
- Add a database to store friendship information.
- Deploy the application online.

## 👨‍💻 Author

**MD Nawedullah Saif**

---

*Built as a Python project to explore graph-based friend recommendations.*
