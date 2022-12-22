import numpy as np
from hypernetx import Entity, EntitySet


def test_construct_empty_entityset():
    es = EntitySet()
    assert es.empty
    assert len(es.elements) == 0
    assert es.dimsize == 0


def test_construct_entityset_from_data(harry_potter):
    es = EntitySet(
        data=np.asarray(harry_potter.data),
        labels=harry_potter.labels,
        level1=1,
        level2=3,
    )
    assert es.indices("Blood status", ["Pure-blood", "Half-blood"]) == [2, 1]
    assert es.incidence_matrix().shape == (36, 11)
    assert len(es.collapse_identical_elements()) == 11


def test_construct_entityset_from_entity_hp(harry_potter):
    es = EntitySet(
        entity=Entity(data=np.asarray(harry_potter.data), labels=harry_potter.labels),
        level1="Blood status",
        level2="House",
    )
    assert es.indices("Blood status", ["Pure-blood", "Half-blood"]) == [2, 1]
    assert es.incidence_matrix().shape == (7, 11)
    assert len(es.collapse_identical_elements()) == 9


def test_construct_entityset_from_entity(sbs):
    es = EntitySet(entity=Entity(entity=sbs.edgedict), cell_properties="cell_weights")

    assert not es.empty
    assert es.dimsize == 2
    assert es.incidence_matrix().shape == (7, 6)