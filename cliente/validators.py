import re
from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _

error_messages = {
    'invalid': _("Numero de CPF/CNPJ inválido"),
    'digits_only': _("Este campo aceita apenas números"),
    'max_digits': _("Este campo deve ter 11 (CPF) ou 14 (CNPJ) dígitos"),
}


def DV_maker(v):
    if v >= 2:
        return 11 - v
    return 0


def validate_CPF_CNPJ(value):
    if value in EMPTY_VALUES:
        return u''

    if not value.isdigit():
        raise ValidationError(error_messages['digits_only'])

    if len(value) == 11:
        return validate_CPF(value)
    else:
        return validate_CNPJ(value)


def validate_CPF(value):
    """
    Value can be either a string in the format XXX.XXX.XXX-XX or an
    11-digit number.
    """

    if value in EMPTY_VALUES:
        return u''
    if not value.isdigit():
        value = re.sub("[-\.]", "", value)  # noqa: W605
    orig_value = value[:]
    try:
        int(value)
    except ValueError:
        raise ValidationError(error_messages['digits_only'])
    if len(value) != 11:
        raise ValidationError(error_messages['max_digits'])
    orig_dv = value[-2:]

    new_1dv = sum([i * int(value[idx]) for idx, i in enumerate(range(10, 1, -1))])
    new_1dv = DV_maker(new_1dv % 11)
    value = value[:-2] + str(new_1dv) + value[-1]
    new_2dv = sum([i * int(value[idx]) for idx, i in enumerate(range(11, 1, -1))])
    new_2dv = DV_maker(new_2dv % 11)
    value = value[:-1] + str(new_2dv)
    if value[-2:] != orig_dv:
        raise ValidationError(error_messages['invalid'])

    return orig_value


def validate_CNPJ(value):
    """
    Value can be either a string in the format XX.XXX.XXX/XXXX-XX or a
    group of 14 characters.
    :type value: object
    """
    value = str(value)
    if value in EMPTY_VALUES:
        return u''
    if not value.isdigit():
        value = re.sub("[-/\.]", "", value)  # noqa: W605
    orig_value = value[:]
    try:
        int(value)
    except ValueError:
        raise ValidationError(error_messages['digits_only'])
    if len(value) != 14:
        raise ValidationError(error_messages['max_digits'])
    orig_dv = value[-2:]

    new_1dv = sum([i * int(value[idx]) for idx, i in enumerate(list(range(5, 1, -1)) + list(range(9, 1, -1)))])
    new_1dv = DV_maker(new_1dv % 11)
    value = value[:-2] + str(new_1dv) + value[-1]
    new_2dv = sum([i * int(value[idx]) for idx, i in enumerate(list(range(6, 1, -1)) + list(range(9, 1, -1)))])
    new_2dv = DV_maker(new_2dv % 11)
    value = value[:-1] + str(new_2dv)
    if value[-2:] != orig_dv:
        raise ValidationError(error_messages['invalid'])

    return orig_value