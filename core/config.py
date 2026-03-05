import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
HTTP_PROXY = os.getenv("HTTP_PROXY")
HTTPS_PROXY = os.getenv("HTTPS_PROXY")

if not GOOGLE_API_KEY:
    raise ValueError("⚠️ 致命错误：未在 .env 文件中找到 GOOGLE_API_KEY！请确保你在项目根目录下创建了 .env 文件并正确填写。")

if HTTP_PROXY and HTTPS_PROXY:
    os.environ["HTTP_PROXY"] = HTTP_PROXY
    os.environ["HTTPS_PROXY"] = HTTPS_PROXY
    print("🌐 已检测到并加载本地代理设置。")

print("✅ 环境配置加载成功！")