import ast
import itertools
import sys

from .operator import Operator
from ..util import build_mutations

def _permute(args):
    """
        Generate permutation of all arguments (minus original arguments).
    """
    p = itertools.permutations(args)

    # Remove duplicates (incase of NoneType in lower/upper/step)
    p = list(set(p))

    # Don't mutate to original state
    p.remove(tuple(args))
    return p

class MutateCall(Operator):
    """An operator that modifies function call arguments."""

    def visit_Call(self, node):
        return self.visit_mutation_site(
            node,
            len(_permute(node.args)))

    def mutate(self, node, idx):
        cur = _permute(node.args)[idx]
        
        if sys.version_info < (3, 5):
            return ast.Call(node.func, cur, node.keywords, node.starargs, node.kwargs)
        else:
            return ast.Call(node.func, cur, node.keywords)
