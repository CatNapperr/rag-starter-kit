import bs4
import os
from langchain import hub
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_google_genai import ChatGoogleGenerativeAI,GoogleGenerativeAIEmbeddings

# 定义一个全局变量，用来存储当前构建好的 RAG 链
global_rag_chain = None

def load_and_index_url(url:str) -> bool:
    global global_rag_chain
    try:
        #-----INDEXING------#
        print(f"🔗 开始处理网址: {url}")
        # load #
        loader = WebBaseLoader(
            web_path=(url),
        )
        docs = loader.load()
        
        if not docs:
            return False
        
        # split #
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        splits = text_splitter.split_documents(docs)

        # embed #
        vectorstore = Chroma.from_documents(documents=splits,
                            embedding=GoogleGenerativeAIEmbeddings(
                                model="models/gemini-embedding-001"))
        retriever = vectorstore.as_retriever() # 生成基本检索器，用于后续查询

        #-----RETRIVEL and GENERATION------#
        prompt = hub.pull("rlm/rag-prompt")
        llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0)
        parser = StrOutputParser()

        # 用于将检索到的文档列表转换成字符串供 LLM 使用
        def format_docs(docs):
            return "\n\n".join(doc.page_content for doc in docs)

        global_rag_chain = (
            {"context": retriever | format_docs, "question":RunnablePassthrough()}
            | prompt
            | llm
            | parser
        )
        print("✅ 网址处理并向量化完成！")
        return True
    
    except Exception as e:
        print(f"❌ 处理网址时出错: {e}")
        return False

def get_answer(question:str) -> str:
    
    global global_rag_chain

    if global_rag_chain is None:
        return "请先在页面上方输入一个网址并点击加载，然后再向我提问哦！"

    try:
        result = global_rag_chain.invoke(question)
        return result
    except Exception as e:
        print(f"❌ RAG 引擎调用出错: {e}")
        return "抱歉，AI 在检索和思考时遇到了一点问题。"




