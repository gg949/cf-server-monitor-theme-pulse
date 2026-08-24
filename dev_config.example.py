#!/usr/bin/env python3
"""dev_proxy.py 的私密配置模板

用法：cp dev_config.example.py dev_config.py，然后填写下面的值。
dev_config.py 已加入 .gitignore，不会被提交。
"""

# 上游测试服地址（不带协议与路径）
UPSTREAM_HOST = "your-upstream.example.com"

# 管理端 JWT：填上则强制使用该 token；留空则透传浏览器的 Authorization 头
JWT_TOKEN = ""
