from fastapi import APIRouter, HTTPException
from typing import List
from .models import URLBase, URL
from .utils import url_shortener
from .context import global_context

router = APIRouter()

@router.post("/shorten", response_model=URL)
async def create_short_url(url: URLBase):
    """
    创建短链接
    """
    if not url.target_url:
        raise HTTPException(status_code=400, detail="URL不能为空")
    
    try:
        short_url = url_shortener.add_url(str(url.target_url))
        return URL(
            target_url=url.target_url,
            is_active=True,
            clicks=0,
            short_url=short_url
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"创建短链接失败: {str(e)}")

@router.get("/{short_url}")
async def redirect_to_url(short_url: str):
    """
    获取原始链接
    """
    if not short_url:
        raise HTTPException(status_code=400, detail="短链接不能为空")
    
    try:
        original_url = url_shortener.get_original_url(short_url)
        if not original_url:
            raise HTTPException(status_code=404, detail="短链接不存在")
        return {"url": original_url}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取原始链接失败: {str(e)}")

@router.get("/urls/list", response_model=List[URL])
async def list_urls():
    """
    获取所有短链接列表
    """
    try:
        urls = url_shortener.get_all_urls()
        return [
            URL(
                target_url=url["original_url"],
                is_active=True,
                clicks=url["clicks"],
                short_url=url["short_url"]
            )
            for url in urls
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取短链接列表失败: {str(e)}") 