"""Derived invariants over declared response structures.

These functions are mathematical utilities, not physical interpretations.
"""
from math import sqrt


def reciprocity_defect(response):
    """Return ||R-R^T||_F / ||R+R^T||_F for a square nonnegative response.

    The operation is defined on the declared response matrix itself. It is
    invariant under simultaneous node relabelling and positive global scaling.
    """
    n = len(response)
    if n == 0 or any(len(row) != n for row in response):
        raise ValueError("response must be a non-empty square matrix")
    den2 = 0.0
    num2 = 0.0
    for i in range(n):
        for j in range(n):
            x = float(response[i][j])
            y = float(response[j][i])
            if x < 0 or y < 0:
                raise ValueError("response entries must be nonnegative")
            d = x - y
            s = x + y
            num2 += d * d
            den2 += s * s
    if den2 == 0.0:
        raise ValueError("reciprocity defect is undefined for a zero response")
    return sqrt(num2 / den2)
