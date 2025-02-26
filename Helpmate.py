import os
from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter
from langchain. chains import RetrievalQA
from langchain_openai import OpenAIEmbeddings, ChatOpenAI  
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyMuPDFLoader  

# Load API key from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


# Load the PDF document
pdf_loader = PyMuPDFLoader("Principal-Sample-Life-Insurance-Policy.pdf")  
documents = pdf_loader.load()

# Split the text into smaller chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
docs = text_splitter.split_documents(documents)

# Create embeddings and store them in ChromaDB
embeddings = OpenAIEmbeddings(openai_api_key=api_key)
vector_store = Chroma.from_documents(docs, embeddings)

# Set up the retriever
retriever = vector_store.as_retriever(search_kwargs={"k": 3})  # Fetch top 3 relevant documents

# Set up the RetrievalQA chain
llm = ChatOpenAI(model_name="gpt-4", openai_api_key=api_key)
qa_chain = RetrievalQA.from_chain_type(llm, retriever=retriever)

# Test the RAG system with 3 different queries
queries = [
    "What are the requirements for two person to estabish a civil union in Rhode Island?",
    "What is Article 11 related to",
    "Is there any policy Number mentioned in the document?"
]

for query in queries:
    response = qa_chain.invoke(query)
    print(f"\n **Query:** {query}")
    print(f" **Response:** {response}")
