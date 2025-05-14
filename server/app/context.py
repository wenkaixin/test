from typing import Dict, Any

class GlobalContext:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GlobalContext, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance
    
    def _initialize(self):
        """初始化全局上下文"""
        self._url_mapping: Dict[str, Dict[str, Any]] = {}
    
    @property
    def url_mapping(self) -> Dict[str, Dict[str, Any]]:
        return self._url_mapping
    
    def add_url_mapping(self, short_url: str, original_url: str) -> None:
        """添加URL映射"""
        self._url_mapping[short_url] = {
            "original_url": original_url,
            "clicks": 0
        }
    
    def get_original_url(self, short_url: str) -> str:
        """获取原始URL并增加点击次数"""
        if short_url in self._url_mapping:
            self._url_mapping[short_url]["clicks"] += 1
            return self._url_mapping[short_url]["original_url"]
        return None
    
    def get_all_mappings(self):
        """获取所有URL映射"""
        return [
            {
                "short_url": short_url,
                "original_url": data["original_url"],
                "clicks": data["clicks"]
            }
            for short_url, data in self._url_mapping.items()
        ]

# 创建全局上下文实例
global_context = GlobalContext() 