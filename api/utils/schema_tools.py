"""Ferramentas de validação do corpo da requisição."""

from datetime import datetime
from typing import Any, Union

DATE_FORMAT_PG = "%Y-%m-%d %H:%M:%S"


def check_empty_required_fields(fields: tuple, body: dict) -> tuple:
    """Verifica se os campos requeridos estão no dicionário informado.

    Args:
        fields (tuple): tupla com os nomes dos campos requerido
        body (dict): dicionário onde iremos verificar se os campos foram enviados

    Returns:
        bool, list: lista dos campos obrigatorios ausentes do "body" (corpo).
    """
    result: list = list(filter(lambda x: body.get(x, False), fields))
    return (len(result) == len(fields)), (set(fields) - set(result))


def empty_message(field: str):
    """Mensagem padrão quando o campo é vazio ou não foi enviado."""
    return f"O campo {field} é vazio ou não foi enviado"


def empty_fields_message(fields: Any, field) -> dict:
    """Gera mensagem de erro dos campos vazios."""
    return {x: empty_message(x) for x in fields}


def never_empty(value: Any, field) -> str:
    """Se o valor e vazio gera um exceção ValueError."""
    if not value:
        raise ValueError(empty_message(field))
    return value


def serialize_datetime(value: Union[datetime, str], str_format: str = DATE_FORMAT_PG) -> str:
    """Converterá datetime para string conforme formato informado."""
    if isinstance(value, datetime):
        return value.strftime(str_format)

    return value
