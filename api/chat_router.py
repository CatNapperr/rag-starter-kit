from fastapi import APIRouter,HTTPException
from pydantic import BaseModel
from schemas.models import QARequest, UrlRequest
from services.rag_engine import get_answer,load_and_index_url

router = APIRouter()

@router.post("/chat")
async def chat_endpoint(req: QARequest):
    #1.提取用户问题
    question = req.question
    answer = get_answer(question)
    return {"answer": answer}

@router.post("/load_url")
async def load_url_endpoint(req: UrlRequest):
    success = load_and_index_url(req.url)
    if success:
        return {"status": "success", "message": "文档加载并向量化成功！现在你可以开始提问了。"}
    else: 
        # 如果处理失败，返回 500 错误
        raise HTTPException(status_code=500, detail="文档加载或向量化失败，请检查网址是否正确。")

