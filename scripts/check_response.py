#!/usr/bin/env python3
"""Validate rendered emphasis in chat-response samples; never rewrite user data."""

import argparse
import re
from pathlib import Path

from markdown_it import MarkdownIt

PARSER = MarkdownIt("commonmark")


def inspect_response(source):
    issues = []
    if re.search(r"\\\*", source):
        issues.append("Escaped emphasis markers in response source")
    tokens = PARSER.parse(source)
    strong_texts = []
    quote_depth = 0
    for token in tokens:
        if token.type == "blockquote_open":
            quote_depth += 1
        elif token.type == "blockquote_close":
            quote_depth -= 1
        if token.type in {"fence", "code_block", "html_block"}:
            issues.append("Code or HTML block in a normal chat response")
        if token.type != "inline":
            continue
        if quote_depth and "💬" in token.content:
            issues.append("Feedback paragraph is inside a timeline quote")
        strong_depth = 0
        buffer = []
        for child in token.children or []:
            if child.type == "strong_open":
                strong_depth += 1
                if strong_depth != 1:
                    issues.append("Nested emphasis")
                buffer = []
            elif child.type == "strong_close":
                strong_depth -= 1
                value = "".join(buffer)
                strong_texts.append(value)
                if not value or not value[0].isalnum() or not value[-1].isalnum():
                    issues.append("Keep outer punctuation and whitespace outside bold text")
            elif child.type == "text":
                if "*" in child.content or "__" in child.content:
                    issues.append("Visible emphasis marker remains after parsing")
                if strong_depth:
                    buffer.append(child.content)
            elif child.type in {"softbreak", "hardbreak"} and strong_depth:
                issues.append("Bold text crosses a line boundary")
            elif child.type in {"code_inline", "html_inline", "em_open"}:
                issues.append("Code, HTML, or nested emphasis in a normal chat response")
            elif strong_depth and child.type not in {"text"}:
                issues.append("Non-text content inside bold text")
    return {"issues": sorted(set(issues)), "strong_texts": strong_texts}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("responses", type=Path, nargs="+")
    args = parser.parse_args()
    failed = False
    for path in args.responses:
        result = inspect_response(path.read_text(encoding="utf-8"))
        if result["issues"]:
            failed = True
            print(f"{path}: " + "; ".join(result["issues"]))
        else:
            print(f"{path}: PASS ({len(result['strong_texts'])} bold spans)")
    raise SystemExit(1 if failed else 0)


if __name__ == "__main__":
    main()
