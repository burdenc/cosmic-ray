import ast
import sys

from .operator import Operator
from ..util import build_mutations


OPERATORS = (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.FloorDiv, ast.Mod,
             ast.Pow, ast.LShift, ast.RShift, ast.BitOr, ast.BitXor,
             ast.BitAnd)

def _to_ops(from_op):
    """
        The sequence of operators which `from_op` could be mutated to.
    """
    for to_op in OPERATORS:
        yield to_op


class MutateAssign(Operator):
    """An operator that modifies assignment statements."""

    def visit_Assign(self, node):
        if (len(node.targets) != 1):
            return node

        return self.visit_mutation_site(
            node,
            len(build_mutations([None], _to_ops)))

    def mutate(self, node, idx):
        _, to_op = build_mutations([None], _to_ops)[idx]
        return ast.AugAssign(target=node.targets[0], op=to_op(), value=node.value)

class MutateAugAssign(Operator):
    """An operator that modifies augmented assignment statements."""

    def visit_AugAssign(self, node):
        return self.visit_mutation_site(
            node,
            len(build_mutations([node.op], _to_ops)))

    def mutate(self, node, idx):
        _, to_op = build_mutations([node.op], _to_ops)[idx]
        node.op = to_op()
        return node
