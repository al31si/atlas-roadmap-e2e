"""Deliberately small package used only for Atlas Roadmap worker acceptance tests."""


def stable_task_key(project: str, index: int) -> str:
    """Return the stable task key for an already-normalized project identifier."""
    if not project or not project.isascii() or not project.isupper() or not project.isalnum():
        raise ValueError("project must be a non-empty uppercase ASCII identifier")
    if index < 1:
        raise ValueError("index must be positive")
    return f"{project}-{index}"
