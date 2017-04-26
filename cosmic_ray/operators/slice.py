import ast
import itertools

from .operator import Operator
from ..util import build_mutations

def _permute(_slice):
    """
        Generate permutation of all slice arguments (minus original arguments).
    """
    p = itertools.permutations([_slice.lower, _slice.upper, _slice.step])

    # Remove duplicates (incase of NoneType in lower/upper/step)
    p = list(set(p))

    # Don't mutate to original state
    p.remove((_slice.lower, _slice.upper, _slice.step))
    return p

class MutateSlice(Operator):
    """An operator that modifies slices."""

    def visit_Slice(self, node):
        return self.visit_mutation_site(
            node,
            len(_permute(node)))

    def mutate(self, node, idx):
        cur = _permute(node)[idx]
        return ast.Slice(lower=cur[0], upper=cur[1], step=cur[2])
