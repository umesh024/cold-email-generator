import pandas as pd
import chromadb
import uuid

class Portfolio:
    def __init__(self, file_path="app/resource/my_portfolio.csv"):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        self.chroma_client = chromadb.PersistentClient('vectorstore')
        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")

    def load_portfolio(self):
        if not self.collection.count():
            for _, row in self.data.iterrows():
                techstack = str(row.get("Techstack", "")).strip()
                links = str(row.get("Links", "")).strip()

                if techstack and links:
                    self.collection.add(
                        documents=[techstack],
                        metadatas={"links": links},
                        ids=[str(uuid.uuid4())]
                    )

    def query_links(self, skills):
        if not skills:
            return []

        try:
            result = self.collection.query(query_texts=skills, n_results=2)
            metadatas = result.get("metadatas", [])
            return metadatas if metadatas else []
        except Exception as e:
            print("Query error:", e)
            return []