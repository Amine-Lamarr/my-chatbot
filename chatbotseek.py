# %%
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceBgeEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
from openai import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

# %%
api_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",  
  api_key=api_key,           
)

# %%
completion = client.chat.completions.create(
  model="deepseek/deepseek-chat-v3.1:free", 
  messages=[
    {"role": "user", "content": "answer in one word, what is the capital of morocco"}
  ]
)
# %%
with open("amine_website_data.txt", "r" , encoding="utf-8") as f:
    raw_text = f.read()
print(raw_text[:100])    

# %%
text_splitter = CharacterTextSplitter(
    separator="\n\n", 
    chunk_size= 500, 
    chunk_overlap = 50, 
)
texts = text_splitter.split_text(raw_text)
# %%
embeddings = HuggingFaceBgeEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.from_texts(texts, embeddings)

# %%
llm = ChatOpenAI(
    model_name="deepseek/deepseek-chat-v3.1:free",
    openai_api_base="https://openrouter.ai/api/v1",
    openai_api_key=api_key,
    temperature=0.5
)

# %%
retriever = vectorstore.as_retriever()
rag_chain = RetrievalQA.from_chain_type(
    llm = llm, 
    chain_type = 'stuff', 
    retriever=retriever,
)
