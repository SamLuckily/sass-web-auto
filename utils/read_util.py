import os
import yaml


class ReadYaml:
    # data.yaml的文件路径
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "data", "data.yaml")

    def read_data(self):
        """
        获取data.yaml数据
        :return:
        """
        with open(self.path, encoding="utf-8") as f:
            data = yaml.safe_load(f)
            return data


base_data = ReadYaml()
