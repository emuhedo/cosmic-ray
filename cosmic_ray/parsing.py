"""Facilities for generating ASTs from modules."""

import ast
import logging


LOG = logging.getLogger()

# TODO: This is where we can do different things for different kinds of
# modules. Right now we only really handle normal source-code, text-file
# modules.

def get_ast(source_file):
    """Generate an AST from a source file.

    This will be the AST for the contents of the module.

    Args:
        source_file: The path to the source file to be read.

    Returns: A tuple of the form `(source-code, ast)`. The `source-code`
        element is simply a string of the code in the file. The `ast` element
        is the AST of that code.

    Raises:
        OSError: If `source_file` can't be opened.
    """
    with open(source_file, mode='rt') as f:
        source = f.read()
    return (source, ast.parse(source, source_file, 'exec'))
