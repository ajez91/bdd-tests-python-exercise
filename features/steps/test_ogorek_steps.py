from features.cucumbers import CucumberBasket

# # # # # # BEHAVE # # # # # #

from behave import given, when, then


# # # # # # zmiennie # # # # # #

# @given('the basket has {initial} cucumbers')
# def step_impl(context, initial):
#     context.basket = CucumberBasket(initial_count=initial)
#
#
# @when('{some} cucumbers are added to the basket')
# def step_impl(context, some):
#     context.basket.add(some)
#
#
# @then('the basket contains {total} cucumbers')
# def step_impl(context, total):
#     assert context.basket.count == total

# # # # # # sztywno # # # # # #

#
# @given("the basket has 2 cucumbers")
# def basket(context):
#     context.basket = CucumberBasket(initial_count=2)
#
#
# @when("4 cucumbers are added to basket")
# def add_cucumbers(context):
#     context.basket.add(4)
#
#
# @then("the basket contains 6 cucumbers")
# def basket_has_total(context):
#     assert context.basket.count == 6


# # # # # # PYTEST BDD # # # # # #

from pytest_bdd import given, when, then, parsers, scenarios
from functools import partial

# # # # # # zmiennie # # # # # #


# @scenario(r'..\ogorek.feature', 'Add cucumbers to a basket')
# def test_add():
#     pass
#
#
# @scenario(r'..\ogorek.feature', 'Remove cucumbers from the basket')
# def test_remove():
#     pass

scenarios(r"../ogorek.feature")

EXTRA_TYPES = {
    'd' : int,

}

parse_num = partial(parsers.cfparse, extra_types=EXTRA_TYPES)


# @given(parsers.cfparse('the basket has "{initial:d}" cucumbers', extra_types=dict(d=int)))
@given(parse_num('the basket has "{initial:d}" cucumbers'))
def basket(initial):
    return CucumberBasket(initial_count=initial)


# @when(parsers.cfparse('"{some:d}" cucumbers are added to basket', extra_types=dict(d=int)))
@when(parse_num('"{some:d}" cucumbers are added to basket'))
def add_cucumbers(basket, some):
    basket.add(some)


# @when(parsers.cfparse('"{some:d}" cucumbers are removed from the basket', extra_types=dict(d=int)))
@when(parse_num('"{some:d}" cucumbers are removed from the basket'))
def remove_cucumbers(basket, some):
    basket.remove(some)


# @then(parsers.cfparse('the basket contains "{total:d}" cucumbers',  extra_types=dict(d=int)))
@then(parse_num('the basket contains "{total:d}" cucumbers'))
def basket_has_total(basket, total):
    assert basket.count == total


# # # # # # sztywno # # # # # #
#
# @scenario("..\ogorek.feature", "Add cucumbers to a basket")
# def test_add():
#     pass


# @given("the basket has {initial} cucumbers")
# @given(parsers.cfparse("the basket has {initial:d} cucumbers", dict(d=int)s=dict(d=int)))
# def basket():
#     return CucumberBasket(initial_count=2)


# @when("{some} cucumbers are added to basket")
# @when(parsers.cfparse("{some:d} cucumbers are added to basket",  dict(d=int)s=dict(d=int)))
# def add_cucumbers(basket):
#     basket.add(4)


# @then("the basket contains {total} cucumbers")
# @then(parsers.cfparse("the basket contains {total:d} cucumbers",  dict(d=int)s=dict(d=int)))
# def basket_has_total(basket):
#     assert basket.count == 6
