from langchain_openai import OpenAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
load_dotenv()

embeddings = OpenAIEmbeddings(model = "text-embedding-3-large", dimensions = 300)


docs = [
    'Rohit sharma is an Indian opener famous for his aggresive batting in powerplay',
    'Sachin tendulkar is a retired indian cricketing legend who scored 100 centuries in internatinal cricket',
    'Virat Kohli is the greatest batsman of the 21st century who has more than 50 ODI centuries',
    'Jasprit bumrah is a right arm fast bowler considered one of the best in the T20 format.',
    'Dakshat Pawale is a AI enginner from pune studying in D.Y. Patil University.'
]

quert = "tell me about DP"

docs_embeddings = embeddings.embed_documents(docs)

query_embeddings = embeddings.embed_query(quert)

scores = cosine_similarity([query_embeddings], docs_embeddings) [0]


      
index, score = sorted(list(enumerate(scores)), key=lambda x: x[1])[-1]

print(quert)
print(docs[index])
print(f"Score: {score}")