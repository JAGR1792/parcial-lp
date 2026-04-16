from __future__ import annotations

import sys
from pathlib import Path

from antlr4 import CommonTokenStream, FileStream, InputStream

ROOT = Path(__file__).resolve().parent
GENERATED_DIR = ROOT / "generated"
if str(GENERATED_DIR) not in sys.path:
    sys.path.insert(0, str(GENERATED_DIR))

from NoSqlLexer import NoSqlLexer
from NoSqlParser import NoSqlParser

from eval_visitor import EvalVisitor


def run_program(program_text: str) -> EvalVisitor:
    lexer = NoSqlLexer(InputStream(program_text))
    parser = NoSqlParser(CommonTokenStream(lexer))
    visitor = EvalVisitor()
    visitor.visit(parser.program())
    return visitor


def main() -> None:
    if len(sys.argv) > 1:
        program_path = Path(sys.argv[1])
        program_text = program_path.read_text(encoding="utf-8")
    else:
        program_text = sys.stdin.read()

    run_program(program_text)


if __name__ == "__main__":
    main()