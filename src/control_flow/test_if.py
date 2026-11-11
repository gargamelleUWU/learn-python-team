"""IF statement

@see: https://docs.python.org/3/tutorial/controlflow.html

There can be zero or more elif parts, and the else part is optional. The keyword ‘elif’ is
short for ‘else if’, and is useful to avoid excessive indentation.

An if … elif … elif … sequence is a substitute for the switch or case statements found
in other languages.
"""


def test_if_statement():
    """IF statement"""

    number = 15
    conclusion = ''

    if number < 0:
        conclusion = 'The number is negative (the given number is below zero)'
    elif number == 0:
        conclusion = 'Number equals to zero'
    elif number < 1:
        conclusion = 'Number is greater than zero but less than one'
    else:
        conclusion = 'Number bigger than or equal to one'

    assert conclusion == 'Number bigger than or equal to one'


def test_grade_classification():
    """IF statement with multiple ELIF branches"""

    grade = 85
    result = ''

    if grade >= 90:
        result = 'A'
    elif grade >= 80:
        result = 'B'
    elif grade >= 70:
        result = 'C'
    else:
        result = 'D'

    assert result == 'B'


def test_nested_conditions():
    """Check ticket eligibility with a condition inside another condition."""

    age = 18
    has_ticket = True
    result = ''

    if age >= 18:
        if has_ticket:
            result = 'Entry allowed'
        else:
            result = 'Ticket required'
    else:
        result = 'Must be at least 18'

    assert result == 'Entry allowed'
