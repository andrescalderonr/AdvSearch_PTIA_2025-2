# noinspection SpellCheckingInspection
"""
Common decorators for marking or modifying functions.

Currently, contains:
  - privatemethod: marks a method as "private" (informational only)
"""

# noinspection SpellCheckingInspection
def privatemethod(method):
    """
    Decorator to mark a method as private.

    This decorator does not enforce access restrictions. It is
    purely informational, e.g., for tooling, linters, or readability.

    Example:
        @privatemethod
        def _helper(self):
            pass

    Args:
        method: The function/method to decorate.

    Returns:
        The same method with an additional attribute '__privatemethod__'.
    """
    method.__privatemethod__ = True
    return method
