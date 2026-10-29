# Friend Recommendation System

Discover new friends through mutual connections! This interactive web application uses a graph-based recommendation algorithm to suggest potential friends based on your existing friendship network.

##  Live Demo

 **[Try the Friend Recommendation System](https://freindsrecommendationsystem.streamlit.app/)**

##  Features

-  Explore a friendship network of 100 people.
-  Build an undirected graph from friendship data.
-  Recommend new friends using mutual connections.
-  Display the number of mutual connections for each recommendation.
-  Categorize recommendations by match strength:
  - **Highly Recommended:** More than 5 mutual connections.
  - **Good Match:** 3–5 mutual connections.
  - **Possible Match:** Fewer than 3 mutual connections.
-  Simple and interactive web interface built with Streamlit.

##  Technologies Used

- **Python** — Core application logic
- **Pandas** — Data loading and processing
- **Graph Algorithms** — Friendship network and recommendations
- **Streamlit** — Interactive web application

##  Project Structure

```text
Friend-Recommendation-System/
├── app.py
├── friendships_with_names.csv
├── requirements.txt
└── README.md
```

##  Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/mdnawedullah09/-Friend-Recommendation-System-Simple.git
```

### 2. Open the project folder

```bash
cd -Friend-Recommendation-System-Simple
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the application

```bash
streamlit run app.py
```

The application will open in your browser.

##  How It Works

1. Loads friendship data from a CSV file.
2. Represents people and their friendships as an undirected graph.
3. Finds friends of each person's existing friends.
4. Excludes the selected person and their existing friends.
5. Counts mutual connections for each potential friend.
6. Sorts recommendations by mutual connections and assigns a recommendation level.

##  Future Improvements

- Search for people by name.
- Visualize the friendship network.
- Add more recommendation criteria.
- Integrate a database for managing friendships.
- Improve the user interface.

##  Author

**MD Nawedullah Saif**

GitHub: [@mdnawedullah09](https://github.com/mdnawedullah09)

**Taffhimuz Zaman**

GitHub: [@taffhimuzzamanhamza-beep]
(https://github.com/taffhimuzzamanhamza-beep)
---

⭐ If you find this project interesting, consider giving the repository a star!

*Built with Python and Streamlit to explore graph-based friend recommendations.*
