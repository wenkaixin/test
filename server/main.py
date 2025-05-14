import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from app.routes import router

# 创建 FastAPI 应用实例
app = FastAPI(
    title="URL Shortener API",
    description="短链接生成服务",
    version="1.0.0"
)

# 配置 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 在生产环境中应该设置具体的域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(router, prefix="/api")

# 根路径重定向到 API 文档
@app.get("/")
async def root():
    return RedirectResponse(url="/docs")

# 启动配置
if __name__ == "__main__":
    # 开发环境配置
    uvicorn.run(
        "main:app",
        host="0.0.0.0",  # 监听所有网络接口
        port=8000,       # 端口号
        reload=True,     # 开发模式下启用热重载
        workers=1        # 工作进程数
    ) 