from classes.market import Market
from classes.ordinary_client import OrdinaryClient
from classes.pensioner_client import PensionerClient
from classes.promotional_client import PromoClient
from classes.special_client import SpecialClient


def run():
    """
    Функция для запуска симуляции работы магазина.

    Создает экземпляры клиентов различных типов,
    добавляет их в магазин и запускает обновление состояния магазина.
    """
    magnit: Market = Market()

    # Создание экземпляров клиентов различных типов
    ord_cl_1 = OrdinaryClient(name='Об_кл_1')
    ord_cl_2 = OrdinaryClient(name='Об_кл_2')
    ord_cl_3 = OrdinaryClient(name='Об_кл_3')

    sp_cl_1 = SpecialClient(name='Киркоров', vip_id=555555)
    sp_cl_2 = SpecialClient(name='Басков', vip_id=100500)

    pensioner_1 = PensionerClient(name='Петрович', pens_id=101)
    pensioner_2 = PensionerClient(name='Иваныч', pens_id=102)

    promo_1 = PromoClient(name='Пр_Кл_1', promo_name='Лето 2023',
                          promo_cl_id=202)
    promo_2 = PromoClient(name='Пр_Кл_2', promo_name='Лето 2023',
                          promo_cl_id=203)
    promo_3 = PromoClient(name='Пр_Кл_3', promo_name='Лето 2023',
                          promo_cl_id=204)
    promo_4 = PromoClient(name='Пр_Кл_4', promo_name='Лето 2023',
                          promo_cl_id=205)
    promo_5 = PromoClient(name='Пр_Кл_5', promo_name='Жаркая распродажа',
                          promo_cl_id=302)
    promo_6 = PromoClient(name='Пр_Кл_6', promo_name='Жаркая распродажа',
                          promo_cl_id=303)
    promo_7 = PromoClient(name='Пр_Кл_7', promo_name='Жаркая распродажа',
                          promo_cl_id=304)

    # Установка флага возврата для некоторых клиентов
    ord_cl_2.set_make_return(True)
    sp_cl_2.set_make_return(True)
    pensioner_2.set_make_return(True)

    # Добавление клиентов в магазин
    magnit.accept_to_market(ord_cl_1)
    magnit.accept_to_market(ord_cl_2)
    magnit.accept_to_market(ord_cl_3)
    magnit.accept_to_market(sp_cl_1)
    magnit.accept_to_market(sp_cl_2)
    magnit.accept_to_market(pensioner_1)
    magnit.accept_to_market(pensioner_2)
    magnit.accept_to_market(promo_1)
    magnit.accept_to_market(promo_2)
    magnit.accept_to_market(promo_3)
    magnit.accept_to_market(promo_4)
    magnit.accept_to_market(promo_5)
    magnit.accept_to_market(promo_6)
    magnit.accept_to_market(promo_7)

    # Обновление состояния магазина
    magnit.update()


if __name__ == '__main__':
    run()
