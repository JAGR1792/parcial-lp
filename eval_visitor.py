from __future__ import annotations

from collections import OrderedDict
from decimal import Decimal
from typing import Any

from antlr4 import ParseTreeVisitor


class EvalVisitor(ParseTreeVisitor):
    def __init__(self) -> None:
        self.collections: dict[str, list[dict[str, Any]]] = OrderedDict()
        self.current_document: dict[str, Any] | None = None

    def visitProgram(self, ctx):
        for statement in ctx.statement():
            self.visit(statement)
        return None

    def visitCreateCollectionStatement(self, ctx):
        collection_name = ctx.IDENTIFIER().getText()
        self.collections.setdefault(collection_name, [])
        print(f"Collection created: {collection_name}")
        return None

    def visitInsertStatement(self, ctx):
        collection_name = ctx.IDENTIFIER().getText()
        document = self.visit(ctx.objectLiteral())
        self.collections.setdefault(collection_name, []).append(document)
        print(f"Inserted into {collection_name}: {document}")
        return document

    def visitFindStatement(self, ctx):
        collection_name = ctx.IDENTIFIER().getText()
        documents = self.collections.get(collection_name, [])
        matches = [document for document in documents if self._matches_where(ctx.whereClause(), document)]
        print(f"Find in {collection_name}: {matches}")
        return matches

    def visitUpdateStatement(self, ctx):
        collection_name = ctx.IDENTIFIER().getText()
        documents = self.collections.get(collection_name, [])
        updates = self.visit(ctx.assignmentList())
        updated = 0

        for document in documents:
            if self._matches_where(ctx.whereClause(), document):
                document.update(updates)
                updated += 1

        print(f"Update in {collection_name}: {updated} documents")
        return updated

    def visitDeleteStatement(self, ctx):
        collection_name = ctx.IDENTIFIER().getText()
        documents = self.collections.get(collection_name, [])
        before = len(documents)
        documents[:] = [document for document in documents if not self._matches_where(ctx.whereClause(), document)]
        deleted = before - len(documents)
        print(f"Delete from {collection_name}: {deleted} documents")
        return deleted

    def visitShowCollectionsStatement(self, ctx):
        print(f"Collections: {list(self.collections.keys())}")
        return list(self.collections.keys())

    def visitObjectLiteral(self, ctx):
        document: dict[str, Any] = {}
        for pair in ctx.pair():
            document[pair.IDENTIFIER().getText()] = self.visit(pair.expression())
        return document

    def visitAssignmentList(self, ctx):
        updates: dict[str, Any] = {}
        for assignment in ctx.assignment():
            updates[assignment.IDENTIFIER().getText()] = self.visit(assignment.expression())
        return updates

    def visitExpression(self, ctx):
        return self.visit(ctx.orExpr())

    def visitOrExpr(self, ctx):
        result = self.visit(ctx.andExpr(0))
        if len(ctx.andExpr()) == 1:
            return result

        for index in range(1, len(ctx.andExpr())):
            if self._as_bool(result):
                return True
            result = self.visit(ctx.andExpr(index))
        return self._as_bool(result)

    def visitAndExpr(self, ctx):
        result = self.visit(ctx.equalityExpr(0))
        if len(ctx.equalityExpr()) == 1:
            return result

        for index in range(1, len(ctx.equalityExpr())):
            if not self._as_bool(result):
                return False
            result = self.visit(ctx.equalityExpr(index))
        return self._as_bool(result)

    def visitEqualityExpr(self, ctx):
        left = self.visit(ctx.relationalExpr(0))
        if len(ctx.relationalExpr()) == 1:
            return left

        for index in range(1, len(ctx.relationalExpr())):
            right = self.visit(ctx.relationalExpr(index))
            operator = ctx.getChild(2 * index - 1).getText()
            left = self._equals(left, right) if operator == '==' else not self._equals(left, right)
        return left

    def visitRelationalExpr(self, ctx):
        left = self.visit(ctx.primary(0))
        if len(ctx.primary()) == 1:
            return left

        for index in range(1, len(ctx.primary())):
            right = self.visit(ctx.primary(index))
            operator = ctx.getChild(2 * index - 1).getText()
            comparison = self._compare(left, right)
            left = {
                '<': comparison < 0,
                '<=': comparison <= 0,
                '>': comparison > 0,
                '>=': comparison >= 0,
            }[operator]
        return left

    def visitPrimary(self, ctx):
        if ctx.literal() is not None:
            return self.visit(ctx.literal())
        if ctx.IDENTIFIER() is not None:
            if self.current_document is None:
                return None
            return self.current_document.get(ctx.IDENTIFIER().getText())
        return self.visit(ctx.expression())

    def visitLiteral(self, ctx):
        if ctx.STRING() is not None:
            return self._unescape_string(ctx.STRING().getText())
        if ctx.NUMBER() is not None:
            return Decimal(ctx.NUMBER().getText())
        if ctx.BOOLEAN() is not None:
            return ctx.BOOLEAN().getText() == 'true'
        return None

    def _matches_where(self, where_ctx, document: dict[str, Any]) -> bool:
        if where_ctx is None:
            return True
        previous = self.current_document
        self.current_document = document
        try:
            return self._as_bool(self.visit(where_ctx.expression()))
        finally:
            self.current_document = previous

    def _as_bool(self, value: Any) -> bool:
        if isinstance(value, bool):
            return value
        if isinstance(value, (int, float, Decimal)):
            return value != 0
        if isinstance(value, str):
            return value != ''
        return value is not None

    def _equals(self, left: Any, right: Any) -> bool:
        if isinstance(left, Decimal) and isinstance(right, Decimal):
            return left == right
        return left == right

    def _compare(self, left: Any, right: Any) -> int:
        if isinstance(left, Decimal) and isinstance(right, Decimal):
            return (left > right) - (left < right)
        if isinstance(left, str) and isinstance(right, str):
            return (left > right) - (left < right)
        if isinstance(left, bool) and isinstance(right, bool):
            return (left > right) - (left < right)
        raise ValueError(f"Cannot compare values: {left!r} and {right!r}")

    def _unescape_string(self, raw: str) -> str:
        content = raw[1:-1]
        return (
            content.replace('\\n', '\n')
            .replace('\\t', '\t')
            .replace('\\r', '\r')
            .replace('\\"', '"')
            .replace('\\\\', '\\')
        )