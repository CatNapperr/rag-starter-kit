from fastapi import FastAPI, UploadFile, File, HTTPException, Request
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import core.config
from api.chat_router import router as chat_router #导入我的聊天路由

app = FastAPI(title="文档问答系统 API")

# 1. 挂载静态文件目录 (让你的 CSS 和 JS 能被浏览器加载)
app.mount("/static", StaticFiles(directory="static"), name="static")

# 2. 注册API路由
app.include_router(chat_router, prefix="/api")

# 3. 设置根路由 "/"，当用户访问 127.0.0.1:8000/ 时，返回 index.html
@app.get("/")
async def read_index():
    return FileResponse("static/index.html")