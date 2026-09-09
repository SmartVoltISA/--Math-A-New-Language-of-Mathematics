import pytest

from omega_math.invariants import reciprocity_defect


def test_reciprocal_response_is_zero():
    r = [[1, 2, 3], [2, 4, 5], [3, 5, 6]]
    assert reciprocity_defect(r) == pytest.approx(0.0)


def test_directed_response_is_positive():
    r = [[1, 4], [1, 2]]
    assert reciprocity_defect(r) > 0


def test_permutation_invariance():
    r = [[1, 4, 2], [1, 3, 5], [7, 2, 6]]
    p = [2, 0, 1]
    rp = [[r[i][j] for j in p] for i in p]
    assert reciprocity_defect(rp) == pytest.approx(reciprocity_defect(r))


def test_positive_scale_invariance():
    r = [[1, 4], [2, 3]]
    assert reciprocity_defect([[17.3*x for x in row] for row in r]) == pytest.approx(reciprocity_defect(r))


def test_transpose_preserves_magnitude():
    r = [[1, 4], [2, 3]]
    rt = [list(x) for x in zip(*r)]
    assert reciprocity_defect(rt) == pytest.approx(reciprocity_defect(r))


def test_domain_validation():
    with pytest.raises(ValueError): reciprocity_defect([])
    with pytest.raises(ValueError): reciprocity_defect([[1, 2]])
    with pytest.raises(ValueError): reciprocity_defect([[1, -1], [2, 3]])
    with pytest.raises(ValueError): reciprocity_defect([[0, 0], [0, 0]])
