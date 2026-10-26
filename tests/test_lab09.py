"""Tests for Lab 09 (icedtea.py).

One example test ships with the impossible-orders part below: it
shows the with-block shape for a rejected input, match= included.
The rest of the suite is yours. Before you implement each function in
icedtea.py, work here first. For every function below: list its
ordinary cases, the boundaries where its answer changes, and the
cases where two rules act at once as comments, write one test per
case (a single assert statement), run the tests in PyCharm to watch
them fail, and only then implement the function until your tests
pass.
"""

import pytest

from icedtea import (
    tea_price,
    loyalty_discount,
    menu_board,
    affordable_teas,
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
# Prices with defaults: loyalty_discount(total, stamps=0)
# Returns one dollar off per ten stamps, never more than the total.
# Write your tests below.
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
# The menu board: menu_board(size="medium")
# Returns one "name: $price" line per menu tea, in the menu's order,
# built as one list comprehension. Leaving size out means medium.
# Write your tests below.
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
# The menu board: affordable_teas(budget, size="medium")
# Returns the names of the teas costing at most budget, in the menu's
# order. A budget exactly equal to a tea's price covers that tea.
# Write your tests below.
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
# Impossible orders: place_order(tea, size, sweetness, ice, cups)
# Returns the order record, or raises ValueError for an unknown tea,
# size, sweetness, or ice level, or for fewer than one cup.
# The five guards' rejected inputs take six pytest.raises tests: one
# each for an unknown tea, size, sweetness, and ice level, plus one
# each for cups 0 and -1. Around the cups rule the interesting values
# are 0, -1, and 1.
# An example test follows. Write your tests below it.
# ----------------------------------------------------------------------------


def test_unknown_size_is_rejected():
    # Example test: the call must raise, so it goes inside a with
    # block, and match= carries a piece of the expected message.
    # The test fails if the call quietly returns a value instead.
    with pytest.raises(ValueError, match="size"):
        place_order("peach", size="tall")


# ----------------------------------------------------------------------------
# The shared add-in tray: take_add_ins(add_in, order_add_ins)
# Returns the order's add-ins with the new one at the end. After your
# repair, two calls that both leave order_add_ins out must each return
# only their own add-in. That is the test that proves the repair.
# Write your tests below.
# ----------------------------------------------------------------------------
