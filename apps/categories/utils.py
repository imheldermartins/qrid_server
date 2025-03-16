from .models import Category


def is_credit(type):
    return type == Category.INCOME


def is_debit(type):
    return type == Category.EXPENSE
