import pytest

from roadmap_fixture import stable_task_key


def test_stable_task_key() -> None:
    assert stable_task_key("FIXTURE", 7) == "FIXTURE-7"


@pytest.mark.parametrize("project,index", [("", 1), ("lower", 1), ("FIXTURE", 0)])
def test_invalid_task_key(project: str, index: int) -> None:
    with pytest.raises(ValueError):
        stable_task_key(project, index)
