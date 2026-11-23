"""查看本地交换资料的原始记录。"""
import argparse
import json
from pathlib import Path


def read_table(name, directory):
    """从固定的交换目录读取指定表。"""
    with (directory / (name + ".json")).open(encoding="utf-8") as stream:
        return json.load(stream)


def main():
    directory = Path(__file__).resolve().parent / "data"
    tables = sorted(path.stem for path in directory.glob("*.json"))
    parser = argparse.ArgumentParser(description="查看原始业务凭据")
    parser.add_argument("table", choices=tables, nargs="?")
    parser.add_argument("--limit", type=int, default=5, help="数组最多显示该行数")
    args = parser.parse_args()
    if args.limit < 1:
        parser.error("显示行数应当为正整数")
    if args.table is None:
        for name in tables:
            print(name)
        return
    result = read_table(args.table, directory)
    print(json.dumps(result[:args.limit] if isinstance(result, list) else result,
                     ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
