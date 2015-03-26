# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .product import *


def register():
    Pool.register(
        Group,
        GroupTemplate,
        Template,
        module='product_groups', type_='model')
