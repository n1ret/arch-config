import os
import unittest
from pathlib import Path

from arch_cfg import escape_text
from setup import expand_env_templates


class ExpandEnvTemplatesTests(unittest.TestCase):
    def test_expands_regular_placeholder(self):
        self.assertEqual(
            expand_env_templates("{{HOME}}"),
            os.getenv("HOME", ""),
        )

    def test_preserves_escaped_placeholder(self):
        self.assertEqual(
            expand_env_templates(r"\{{HOME}}"),
            "{{HOME}}",
        )

    def test_unescapes_double_backslash(self):
        self.assertEqual(
            expand_env_templates(r"C:\\Users\\me"),
            r"C:\Users\me",
        )


class EscapeDataTests(unittest.TestCase):
    def test_escapes_unescaped_placeholder(self):
        self.assertEqual(
            escape_text(b"{{HOME}}"),
            b"\\{{HOME}}",
        )

    def test_doubles_backslashes(self):
        self.assertEqual(
            escape_text(br"path\to\file"),
            rb"path\\to\\file",
        )

    def test_non_utf8_bytes_are_unchanged(self):
        data = b"\xff\xfe\xfd"
        self.assertEqual(escape_text(data), data)
