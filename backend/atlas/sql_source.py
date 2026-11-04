"""Read SQL source occurrences without splitting literals or comments at semicolons."""
import re
import sqlite3


def query_text(statement):
    """Remove only leading source annotations; preserve the SQL itself verbatim."""
    return re.sub(r'\A(?:\s+|--[^\n]*(?:\n|$)|/\*.*?\*/)*', '', statement, flags=re.S).rstrip()


def sql_statements(text):
    start = 0
    statements = []
    for index, character in enumerate(text):
        if character == ';' and sqlite3.complete_statement(text[start:index + 1]):
            statements.append(text[start:index + 1].strip())
            start = index + 1
    if query_text(text[start:]):
        raise ValueError('Unterminated SQL source statement')
    return statements
