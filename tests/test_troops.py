import pytest

from duke.troops import ALL_TROOPS, Oracle


@pytest.mark.parametrize("troop", ALL_TROOPS)
def test_troop__troop_name__equals_class_name(troop):
    assert troop().troop.value.title() == troop.__name__


def test_oracle__two_images__return_true():
    assert Oracle().two_troop_images
