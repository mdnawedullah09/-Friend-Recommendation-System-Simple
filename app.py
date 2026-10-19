
import pandas as pd
import streamlit as st

# Page settings
st.set_page_config(
    page_title="Friend Recommendation System",
    layout="centered"
)

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("friendships_with_names.csv")

df = load_data()

# Build friendship graph
@st.cache_data
def build_graph(data):
    graph = {}

    for _, row in data.iterrows():
        person = row["user_name"]
        friend = row["friend_name"]

        if person not in graph:
            graph[person] = []

        if friend not in graph:
            graph[friend] = []

        if friend not in graph[person]:
            graph[person].append(friend)

        if person not in graph[friend]:
            graph[friend].append(person)

    return graph

graph = build_graph(df)


# Recommend friends using mutual connections
def recommend(person):
    if person not in graph:
        return []

    friends = graph[person]
    mutual_counts = {}

    for friend in friends:
        for potential_friend in graph[friend]:
            if potential_friend != person and potential_friend not in friends:
                if potential_friend not in mutual_counts:
                    mutual_counts[potential_friend] = 0

                mutual_counts[potential_friend] += 1

    return sorted(
        mutual_counts.items(),
        key=lambda item: item[1],
        reverse=True
    )


# Assign recommendation levels
def recommendation_level(count):
    if count > 5:
        return "Highly Recommended"
    elif count >= 3:
        return "Good Match"
    else:
        return "Possible Match"


# Website interface
st.title("Friend Recommendation System")
st.write(
    "Discover new friends based on your existing "
    "friendship network and mutual connections."
)

st.caption(f"People in the network: {len(graph)}")

people = sorted(graph.keys())

selected_person = st.selectbox(
    "Select your name",
    people
)

if st.button("Find Friends", type="primary"):
    recommendations = recommend(selected_person)

    st.subheader(f"Recommendations for {selected_person}")

    if not recommendations:
        st.info("No new friend recommendations found.")
    else:
        for name, count in recommendations:
            level = recommendation_level(count)

            st.markdown(f"### 👤 {name}")
            st.write(f"Mutual connections: **{count}**")
            st.write(f"Recommendation: **{level}**")
            st.divider()
