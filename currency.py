# !/usr/bin/env python3
"""
currency.py: Changing one kind of currency the user has to the currency the user wants to exchange to.
             (Make sure your computer is online)

__date__   = "2018.12.3"
__author__ = "Wang Yanze"
__pkuid__  = "1800011721"
__email__  = "1800011721@pku.edu.cn"
"""


def before_space(astr):
    """Returns: Substring of s; up to, but not including, the first space

       Parameter s: the string to slice
       Precondition: s has at least one space in it"""
    if astr.count(' ') == 0:
        return None
    else:
        if astr.find(' ') == 0:
            return ''
        else:
            w = astr.find(' ')
            return astr[:w]


def test_before_space():
    """test before_space() function"""
    assert (before_space('0.8963 Euros') == '0.8963')
    assert (before_space('0.8963Euros ') == '0.8963Euros')
    assert (before_space('0.8963 Euros ') == '0.8963')
    assert (before_space('0.004 British Pounds Sterling') == '0.004')
    assert (before_space('0.8963Euros') is None)
    assert (before_space(' 0.8963Euros') == '')
    print('before_space() working correctly')


def first_inside_quotes(astr):
    """
    Returns: The first substring of s between two (double) quote characters
    :parameter astr : the string needed convert
    :precondition : astr must have at least one space
    """
    if type(astr) != str:
        return None
    elif astr.count('"') <= 1:
        return None
    else:
        alist = astr.split('"')
        return alist[1]


def test_first_inside_quotes():
    """test first_inside_quotes() function"""
    assert (first_inside_quotes('A "B C" D "E F" G') == 'B C')
    assert (first_inside_quotes('A "B C" D "E F G') == 'B C')
    assert (first_inside_quotes('A"" "B C" D "E F" G') == '')
    assert (first_inside_quotes('A "B C D E F G') is None)
    print('first_inside_quotes() is working correctly')


def get_to(json):
    """
    Returns: The TO value in the response to a currency query.
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """
    place = json.index('"to"')
    new_str = json[place + len('"to"'):]
    return first_inside_quotes(new_str)


def test_get_to():
    """test get_to() function"""
    assert (get_to(
        '{ "from" : "2.5 United States Dollars", "to" : "2.1589225 Euros", "success" : true, "error" : "" }')
               == '2.1589225 Euros')
    assert (get_to('{ "from" : "", "to" : "", "success" : false, "error" : "Source currency code is invalid." }')
               == '')
    print('get_to() working correctly')


def has_error(json):
    """
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    Returns: True if the query has an error; False otherwise
    """
    if 'true' in json:
        return True
    else:
        return False


def test_has_error():
    """test has_error() function"""
    assert (has_error('{ "from" : "2.5 Cuban Pesos", "to" : "0.08466362745098 Euros", "success" : true, "error" : "" }')
            is True)
    assert (has_error('{ "from" : "", "to" : "", "success" : false, "error" : "Source currency code is invalid." }')
            is False)
    print('has_error() working correctly')


def currency_response(currency_from, currency_to, amount_from):
    """Returns: a JSON string that is a response to a currency query.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float
    """
    from urllib.request import urlopen
    doc = urlopen("http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=%s&to=%s&amt=%f"
                  % (currency_from, currency_to, amount_from))
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    return jstr


def test_currency_response():
    """test currency_response() function"""
    assert (
            '{ "from" : "2.5 Cuban Pesos", "to" : "0.08466362745098 Euros", "success" : true, "error" : "" }'
            == currency_response('CUP', 'EUR', 2.5)
    )
    assert (
            '{ "from" : "2.5 United States Dollars", "to" : "2.1589225 Euros", "success" : true, "error" : "" }'
            == currency_response('USD', 'EUR', 2.5)
    )
    assert (
            '{ "from" : "", "to" : "", "success" : false, "error" : "Source currency code is invalid." }'
            == currency_response('123', 'EUR', 2.5)
    )
    assert (
            '{ "from" : "", "to" : "", "success" : false, "error" : "Source currency code is invalid." }'
            == currency_response('', '', float())
    )
    print('currency_response() working correctly')


def iscurrency(currency):
    """
    Returns: True if currency is a valid (3 letter code for a) currency.
             It returns False otherwise.

    Parameter currency: the currency code to verify
    Precondition: currency is a string.
    """
    if has_error(currency_response(currency, 'USD', 1)) is True:
        return True
    else:
        return False


def test_iscurrency():
    """test iscurrency() function"""
    assert (iscurrency('USD') is True)
    assert (iscurrency('') is False)
    assert (iscurrency(123) is False)
    print('iscurrency() working correctly')


def exchange(currency_from, currency_to, amount_from):
    """
    Returns: amount of currency received in the given exchange.
             The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float
    """
    response = currency_response(currency_from, currency_to, amount_from)
    outcome = get_to(response)
    amount_to = before_space(outcome)
    return float(amount_to)


def test_exchange():
    """test exchange() function"""
    assert (exchange('USD', 'EUR', 2.5) == 2.1589225)
    assert (exchange('CLP', 'GBP', 3.65) == 0.0041012051559792)
    assert (exchange('JPY', 'ILS', 0) == 0)
    print('exchange() working correctly')


def isnum(amount_from):
    """
    returns: judge if the input is a valid number;
             if it is, return True ; else return False
    parameter amount_from : the str needed be judged
    """
    if '.' in amount_from:
        s = amount_from.split('.')
        if s[0].isdigit() and s[-1].isdigit():
            return True
        else:
            return False
    elif amount_from.isdigit() is True:
        return True
    else:
        return False


def test_isnum():
    """test isnum() function"""
    assert (isnum('3.5') is True)
    assert (isnum('2') is True)
    assert (isnum('k.3') is False)
    print('isnum() working correctly')


def test_all():
    """test all cases"""
    test_currency_response()
    test_before_space()
    test_first_inside_quotes()
    test_get_to()
    test_exchange()
    test_iscurrency()
    test_isnum()


def main():
    """
    the user inputs three parameters: currency_from, currency_to, amount_from
     currency_from: the currency on hand
     currency_to: the currency to convert to
     amount_from: amount of currency to convert

    These parameters should be valid, but if not, there will be a reminder.

    Then, you will get your outcome about the currency exchange, from the currency on hand
    to the currency you want to exchange.

    The program will test all functions by itself finally.

    You must make sure your computer is online to do these!
    """
    currency_from = input('please input the currency you have')
    while iscurrency(currency_from) is False:
        print('please input valid currency abbreviation!')
        currency_from = input('please input the currency you have')

    currency_to = input('please input the currency you want to get')
    while iscurrency(currency_to) is False:
        print('please input valid currency abbreviation!')
        currency_to = input('please input the currency you want to get')

    amount_from = input('please input the amount')
    while isnum(amount_from) is False:
        print('please input valid number!')
        amount_from = input('please input the amount')

    outcome = exchange(currency_from, currency_to, float(amount_from))
    print(outcome)
    test_all()


if __name__ == '__main__':
    main()

