import pytest
from pytest_bdd import given, when, then, scenarios, scenario
from features.cucumbers import CucumberBasket
from functools import partial

# * * * * BEZ PARAMETRYZACJI * * * * * *

EXTRA_TYPES = {
    'd' : int,

}

CONVERTERS = {
    "initial" : int,
    "some" : int,
    "total" : int,
}
scenarios(r'../ogorki.feature', example_converters=CONVERTERS)



# * * * * * * * PARAMETRYZACJA * * * * * * * * * *

# EXTRA_TYPES = {
#     'd' : int,
#
# }
#
# CONVERTERS = {
#     "initial" : int,
#     "some" : int,
#     "total" : int,
# }
#
#
# @pytest.mark.parametrize(
#     ['initial', 'some', 'total'],
#     [(0, 3, 3),
#      (2, 4, 6),
#      (5, 5, 10)]
# )
# @scenario(r'../ogorki.feature', 'Add cucumbers to a basket')
# def test_add(initial, some, total):
#     pass


@given('the basket has "<initial>" cucumbers')
def basket(initial):
    return CucumberBasket(initial_count=initial)


@when('"<some>" cucumbers are added to the basket')
def add_cucumbers(basket, some):
    basket.add(some)


@when('"<some>" cucumbers are removed from the basket')
def remove_cucumbers(basket, some):
    basket.remove(some)


@then('the basket contains "<total>" cucumbers')
def basket_total(basket, total):
    assert basket.count == total



