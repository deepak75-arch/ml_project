# app.py
from flask import Flask, render_template, request, jsonify
import os
import pandas as pd
import plotly.express as px
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# Import our chatbot response function
from chatbot_model import get_chatbot_response

app = Flask(__name__)

def load_data():

    df = pd.read_csv("C:/Users/deepa/PycharmProjects/PythonProject2/data/customer_purchase_data.csv")
    return df

def perform_clustering(df, n_clusters):
    features = df[['Age', 'AnnualIncome', 'NumberOfPurchases', 'TimeSpentOnWebsite', 'DiscountsAvailed']]
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(features_scaled)
    df['Cluster'] = clusters
    pca = PCA(n_components=2, random_state=42)
    pca_result = pca.fit_transform(features_scaled)
    viz_df = pd.DataFrame({
        'PCA1': pca_result[:, 0],
        'PCA2': pca_result[:, 1],
        'Cluster': clusters.astype(str)
    })
    fig = px.scatter(viz_df, x='PCA1', y='PCA2', color='Cluster',
                     title=f"Consumer Clusters (K={n_clusters}) Visualized with PCA",
                     labels={"PCA1": "Principal Component 1", "PCA2": "Principal Component 2"})
    graph_html = fig.to_html(full_html=False)
    return graph_html, df

@app.route("/", methods=["GET", "POST"])
def index():
    df = load_data()
    n_clusters = 3
    if request.method == "POST":
        try:
            n_clusters = int(request.form.get("clusters", 3))
        except Exception as e:
            n_clusters = 3
    graph_html, df_clustered = perform_clustering(df, n_clusters)
    cluster_summary = df_clustered.groupby("Cluster")[['Age', 'AnnualIncome', 'NumberOfPurchases', 'TimeSpentOnWebsite', 'DiscountsAvailed']].mean().round(2)
    return render_template("index.html", graph_html=graph_html, n_clusters=n_clusters, cluster_summary=cluster_summary.to_html())

@app.route("/chat", methods=["GET"])
def chat():
    # Render a separate template for the chatbot interface
    return render_template("chatbot.html")

@app.route("/get_response", methods=["GET"])
def get_response():
    user_message = request.args.get("msg")
    response = get_chatbot_response(user_message)
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
