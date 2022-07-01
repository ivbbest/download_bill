import random


MEDSERVICE = {1: 'консультация', 2: 'лечение',
              3: 'стационар', 4: 'диагностика',
              5: 'лаборатория'}


def fraud_detector(row: str) -> float:
    """
    Детектор мошенничества
    На вход принимает str, на выходе float рандомно
    в диапазоне от 0 до 1
    """
    if not isinstance(row, str):
        raise ValueError("Don't string value")

    fraud_score = random.random()

    return fraud_score


def service_classifier(row: str):
    """
    Классификатор услуг
    На вход принимает str, на выходе dict вида
    {service_class: int, ‘service_name’: str}
    Возвращаемый dict формировать путём рандомного
    выбора пары ключ-значение из шаблона словаря
    """
    if not isinstance(row, str):
        raise ValueError("Don't string value")

    service_class = random.choice(list(MEDSERVICE.keys()))
    service_name = MEDSERVICE.get(service_class)

    return {service_class: service_name}
