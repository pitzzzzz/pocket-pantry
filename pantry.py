"""Minimal file-backed pantry CLI; deliberately small for the custodian demo."""
import argparse
import json
import os
from pathlib import Path


def run(argv=None):
    parser = argparse.ArgumentParser(description="Pocket Pantry")
    parser.add_argument("--file", default=os.environ.get("PANTRY_FILE", "kitchen.json"))
    sub = parser.add_subparsers(dest="command", required=True)
    add = sub.add_parser("add")
    add.add_argument("name")
    add.add_argument("quantity", type=int)
    use = sub.add_parser("use")
    use.add_argument("name")
    use.add_argument("quantity", type=int)
    sub.add_parser("list")
    args = parser.parse_args(argv)
    path = Path(args.file)
    items = json.loads(path.read_text()) if path.exists() else {}
    if args.command == "list":
        for name, quantity in sorted(items.items()):
            print(f"{name}: {quantity}")
        return
    if args.quantity <= 0:
        parser.error("quantity must be positive")
    if args.command == "add":
        items[args.name] = items.get(args.name, 0) + args.quantity
    else:
        if items.get(args.name, 0) < args.quantity:
            parser.error("not enough stock")
        items[args.name] -= args.quantity
    path.write_text(json.dumps(items, indent=2, sort_keys=True) + "\n")
    print(f"{args.name}: {items[args.name]}")


if __name__ == "__main__":
    run()
