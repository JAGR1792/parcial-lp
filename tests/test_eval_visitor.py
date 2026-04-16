from __future__ import annotations

import sys
from pathlib import Path

from antlr4 import CommonTokenStream, InputStream

ROOT = Path(__file__).resolve().parents[1]
GENERATED_DIR = ROOT / "generated"
if str(GENERATED_DIR) not in sys.path:
    sys.path.insert(0, str(GENERATED_DIR))

from NoSqlLexer import NoSqlLexer
from NoSqlParser import NoSqlParser

from eval_visitor import EvalVisitor


def test_crud_program():
    program = """
    CREATE COLLECTION users;
    INSERT INTO users { name: "Ana", age: 20, active: true };
    INSERT INTO users { name: "Luis", age: 17, active: false };
    FIND users WHERE age >= 18;
    UPDATE users SET active = false WHERE name == "Ana";
    DELETE FROM users WHERE age < 18;
    """

    lexer = NoSqlLexer(InputStream(program))
    parser = NoSqlParser(CommonTokenStream(lexer))
    visitor = EvalVisitor()
    visitor.visit(parser.program())

    assert "users" in visitor.collections
    assert len(visitor.collections["users"]) == 1
    assert visitor.collections["users"][0]["name"] == "Ana"
    assert visitor.collections["users"][0]["active"] is False