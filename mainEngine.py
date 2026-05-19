import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

sections = pickle.load(open("sections (1).pkl" , 'rb'))

sum = pd.read_excel("Section_wise_summary.xlsx")
sum = sum[["Section","Name" , "Description" , "One-sentence significance"]]

def search(query, top_k=5):

    # convert query to vector
    query_vec = vectorizer.transform([query])

    # similarity scores
    scores = cosine_similarity(query_vec, X).flatten()

    # best matches
    top_indices = scores.argsort()[-top_k:][::-1]

    results = []

    for i in top_indices:

        results.append({

            "section": sum.iloc[i]["Section"],

            "name": sum.iloc[i]["Name"],

            "one_line_summary": sum.iloc[i]["One-sentence significance"],

            "description": sum.iloc[i]["Description"],

            "score": float(scores[i]),


            "pdf_file": f"output/Section_{sum.iloc[i]['Section']}..pdf"

        })

    return results


vectorizer = TfidfVectorizer(
    stop_words='english',
    ngram_range=(1,3),
    lowercase=True
)

search_corpus = []

for i in range(len(sections)):

    title = str(sum.iloc[i]["Name"])

    one_line = str(
        sum.iloc[i]["One-sentence significance"]
    )

    description = str(
        sum.iloc[i]["Description"]
    )

    raw_text = str(
        sections[i]
    )

    # =====================================
    # PRIORITY WEIGHTING
    # =====================================

    combined_text = (

        # Highest priority
        (one_line + " ") * 5 +

        # Second priority
        (title + " ") * 4 +

        # Third priority
        (description + " ") * 3 +

        # Lowest priority
        raw_text
    )

    search_corpus.append(combined_text)

X = vectorizer.fit_transform(search_corpus)


