import os
import yaml


class SgridConfig:
    def __init__(self, config_filename='sgrid.yml'):
        self.config_filename = config_filename
        self._config_data = self.load_config()

    def load_config(self):
        # 获取当前脚本所在的目录
        current_dir = os.path.dirname(os.path.curdir)
        # 构造配置文件的完整路径
        config_path = os.path.join(current_dir, self.config_filename)

        try:
            with open(config_path, 'r') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file {config_path} not found.")
        except yaml.YAMLError as e:
            raise ValueError(f"Error parsing YAML file: {e}")

    def __getitem__(self, key):
        # 提供字典接口访问配置数据
        return self._config_data[key]

    def get(self, key, default=None):
        # 提供类似字典的get方法，支持默认值
        return self._config_data.get(key, default)

        # 你可以为特定的配置项添加getter方法，例如：

    @property
    def server_host(self):
        return self._config_data.get('server', {}).get('host', 'default_host')

    @property
    def server_port(self):
        return self._config_data.get('server', {}).get('port', 5000)
