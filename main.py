from src import app
from src.sgrid import SgridConfig

# 使用示例
config_data = SgridConfig()
print(config_data)  # 输出解析后的字典

if __name__ == '__main__':
    app.run(host=config_data.server_host, port=config_data.server_port)
