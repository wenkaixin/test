import string
import random
from .context import global_context

class URLShortener:
    def __init__(self):
        self.chars = string.ascii_letters + string.digits

    def generate_short_url(self, length: int = 6) -> str:
        """生成随机短链接"""
        while True:
            short_url = ''.join(random.choices(self.chars, k=length))
            if short_url not in global_context.url_mapping:
                return short_url

    def add_url(self, original_url: str) -> str:
        """添加新的URL映射"""
        short_url = self.generate_short_url()
        global_context.add_url_mapping(short_url, original_url)
        return short_url

    def get_original_url(self, short_url: str) -> str:
        """获取原始URL"""
        return global_context.get_original_url(short_url)

    def get_all_urls(self):
        """获取所有URL映射"""
        return global_context.get_all_mappings()

# 创建URL缩短器实例
url_shortener = URLShortener() 