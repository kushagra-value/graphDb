import streamlit as st
from langchain_community.graphs import Neo4jGraph
from langchain_groq import ChatGroq
from langchain.chains import GraphCypherQAChain
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Set up Neo4j connection details
NEO4J_URI = "neo4j+s://e108e955.databases.neo4j.io"
NEO4J_USERNAME = "neo4j"
NEO4J_PASSWORD = "iCcYTVGFCGvZtj3SxIixrvwyYtU5XeawwlNJUs86Md0"

# Set up ChatGroq API key
groq_api_key = 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

# Initialize Neo4j graph
graph = Neo4jGraph(url=NEO4J_URI, username=NEO4J_USERNAME, password=NEO4J_PASSWORD)

# Initialize ChatGroq model
llm = ChatGroq(groq_api_key=groq_api_key, model_name="Gemma2-9b-It")

# Create the QA chain
chain = GraphCypherQAChain.from_llm(graph=graph, llm=llm, verbose=True)

# Streamlit app layout
st.title("Graph Database Question Answering")

# User input for the query
query = st.text_input("Enter your question about the movie database:")

if query:
    # Get the response from the QA chain
    response = chain.invoke({"query": query})
    
    # Display the response
    st.write("Response:")
    st.write(response['result'])

    # Optionally, show the generated Cypher query
    st.write("Generated Cypher Query:")
    st.write(response.get('generated_cypher', 'No Cypher query generated.'))
