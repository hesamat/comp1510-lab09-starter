"""Tests for Lab 09 (icedtea.py).

There are no example tests this time: the whole suite is yours.
Before you implement each function in icedtea.py, work here first.
For every function below: list its ordinary cases, the boundaries
where its answer changes, and the cases where two rules act at once
as comments, write one test per case (a single assert statement),
run the tests in PyCharm to watch them fail, and only then implement
the function until your tests pass.

A rejected input is tested the other way round: the call must raise.
Wrap it in a with block,

    with pytest.raises(ValueError):
        place_order("peach", size="tall")

and the test passes only when the call raises ValueError. Add
match="size" to also check that the message explains itself.
"""

import pytest

from icedtea import (
    tea_price,
    add_ins_cost,
    loyalty_discount,
    place_order,
    take_add_ins,
)


# ----------------------------------------------------------------------------
# Prices with defaults: tea_price(tea, size="medium")
# Returns the price of one cup: the menu price times the size multiplier,
# rounded to two decimals. Leaving size out means medium.
# Write your tests below.
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
# Prices with defaults: add_ins_cost(add_ins, each=ADD_IN_PRICE)
# Returns the cost of a list of add-ins at a price each, rounded to two
# decimals. An empty list costs nothing.
# Write your tests below.
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
# Prices with defaults: loyalty_discount(total, stamps=0)
# Returns one dollar off per ten stamps, never more than the total.
# Write your tests below.
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
# Impossible orders: place_order(tea, size, sweetness, ice, cups)
# Returns the order record, or raises ValueError for an unknown tea,
# size, sweetness, or ice level, or for fewer than one cup.
# Five rejected inputs means five pytest.raises tests. Around the cups
# rule the interesting values are 0, -1, and 1.
# Write your tests below.
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
# The shared add-in tray: take_add_ins(add_in, order_add_ins)
# Returns the order's add-ins with the new one at the end. After your
# repair, two calls that both leave order_add_ins out must each return
# only their own add-in. That is the test that proves the repair.
# Write your tests below.
# ----------------------------------------------------------------------------
