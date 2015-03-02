from .operator import Operator


class ArithmeticOperatorDeletion(Operator):
    """A NodeTransformer that deletes the n-th arithmetic operator.
    """

    @property
    def activated(self):
        "Whether this replace has performed any replacements."
        return self._activated

    def visit_Add(self, node):
        return self._visit_arithmetic_op(node)

    def visit_Sub(self, node):
        return self._visit_arithmetic_op(node)

    def visit_Mult(self, node):
        return self._visit_arithmetic_op(node)

    def visit_Div(self, node):
        return self._visit_arithmetic_op(node)

    def _visit_arithmetic_op(self, node):
        return self.visit_mutation_site(node)

    def mutate(self, node):
        return None

    def __repr__(self):
        return 'ArithmeticOperatorDeletion(target={})'.format(
            self._target)
