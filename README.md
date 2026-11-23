# 流转租金和务工工资的家庭增收核实

本资料记录合作社区组截至不同日期取得的家庭登记、地块租金和工资凭据。 数据为合成资料。交换说明见 [数据约定](data-contract.md)。

使用 Python 3.11。当前可读取和抽查原始业务资料。
如使用业务分析依赖，可从项目根目录运行 `python3 -m pip install -r requirements.txt`。

```sh
python3 inspect_data.py
python3 inspect_data.py households --limit 2
python3 -m unittest discover -s tests -v
```

测试检查交换资料的关联和原始凭据的可读性。命令可离线使用。
