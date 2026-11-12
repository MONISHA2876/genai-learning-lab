from google import genai
from google.genai import types
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from dotenv import load_dotenv

load_dotenv()

# Test Data
documents = [
    "Water boils at 100 degrees Celsius at sea level.",
    "Photosynthesis converts sunlight into chemical energy in plants.",
    "The Milky Way contains over 100 billion stars.",
    "A black hole's gravity is so strong that light cannot escape.",
    "Leonardo da Vinci painted the Mona Lisa in the early 1500s.",
    "Vincent van Gogh painted The Starry Night in 1889.",
]
query = "How do plants get energy?"

client = genai.Client()

query_embedding = client.models.embed_content(
    model="gemini-embedding-001",
    contents=query,
    config=types.EmbedContentConfig(output_dimensionality=200)
)
q_embedding = query_embedding.embeddings[0].values

data_embeddings = client.models.embed_content(
    model="gemini-embedding-001",
    contents=documents,
    config=types.EmbedContentConfig(output_dimensionality=200)
)
doc_embeddings = [ e.values for e in data_embeddings.embeddings ]

result = []
for i, e in enumerate(doc_embeddings):
    [similarity] = cosine_similarity([q_embedding],[e])
    similarity = [i, similarity[0]]
    result.append(similarity)

result.sort(key=lambda x:x[1], reverse=True)

print("After Sementic search the most similar content found is : \n\n documents[result[0][0]] \n")