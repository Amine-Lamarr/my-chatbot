<h1>🧠 RAG Chatbot using Custom Data</h1>

<p>
This project is a <strong>Retrieval-Augmented Generation (RAG)</strong> chatbot built using 
<strong>LangChain</strong>, <strong>FAISS</strong>, <strong>HuggingFace embeddings</strong>, and <strong>FastAPI</strong>.<br>
It uses a custom <code>.txt</code> file (<strong>amine_website_data.txt</strong>) as the knowledge base 
to answer user questions through a simple <strong>HTML/CSS interface</strong>.
</p>

<h2>🚀 Features</h2>
<ul>
  <li>Uses <strong>LangChain</strong> for building the RAG pipeline</li>
  <li>Embeds custom data with <strong>HuggingFaceBgeEmbeddings</strong> (<code>sentence-transformers/all-MiniLM-L6-v2</code>)</li>
  <li>Stores text chunks in a <strong>FAISS</strong> vector database</li>
  <li>Generates answers using <strong>DeepSeek Chat Model</strong> (<code>deepseek/deepseek-chat-v3.1:free</code>) via <strong>OpenRouter API</strong></li>
  <li>Provides a <strong>FastAPI</strong> backend with a <code>/ask</code> endpoint</li>
  <li>Includes a <strong>frontend interface</strong> made with HTML/CSS</li>
</ul>

<h2>🧩 How It Works</h2>
<ul>
  <li>The text from <code>amine_website_data.txt</code> is read and split into chunks using <strong>CharacterTextSplitter</strong>.</li>
  <li>Each chunk is embedded with <strong>HuggingFaceBgeEmbeddings</strong>.</li>
  <li>Chunks are stored in a <strong>FAISS</strong> vectorstore.</li>
</ul>

<h2>🧱 Tech Stack</h2>
<ul>
  <li>Python</li>
  <li>LangChain</li>
  <li>FAISS</li>
  <li>HuggingFace Embeddings</li>
  <li>OpenRouter API</li>
  <li>FastAPI</li>
  <li>HTML / CSS</li>
</ul>

<h2>🧠 Model & API</h2>
<ul>
  <li><strong>Model used:</strong> <code>deepseek/deepseek-chat-v3.1:free</code></li>
  <li><strong>API Base URL:</strong> <a href="https://openrouter.ai/api/v1" target="_blank">https://openrouter.ai/api/v1</a></li>
  <li><strong>Library:</strong> <code>ChatOpenAI</code> from <code>langchain.chat_models</code></li>
</ul>

<h2>🖥️ Frontend</h2>
<p>
A simple <strong>HTML/CSS interface</strong> is included to send user questions to the 
<strong>FastAPI</strong> <code>/ask</code> endpoint and display the chatbot’s responses.
</p>

<p>
When a user asks a question, the retriever fetches the most relevant chunks.<br>
The <strong>DeepSeek Chat model</strong> (through <strong>OpenRouter</strong>) generates a response using the retrieved context.
</p>
