Module 02_homework.classes.market
=================================

Classes
-------

`Market()`
:   Класс, представляющий магазин.
    
    :attr :
        queue (List[Buyer]): Очередь покупателей.
    
    Methods:
        accept_to_market(buyer: Buyer) -> None:
            Принимает покупателя в магазин.
        take_in_queue(buyer: Buyer) -> None:
            Принимает покупателя в очередь.
        release_from_market(buyers: List[Buyer]) -> None:
            Освобождает покупателей из магазина.
        give_order() -> None:
            Выполняет выдачу заказов покупателям.
        release_from_queue() -> None:
            Освобождает покупателей из очереди.
        take_order() -> None:
            Обрабатывает заказы покупателей.
        update() -> None:
            Обновляет состояние магазина.
        handle_promo(promo_buyer: Buyer) -> None:
            Обрабатывает заказы для клиентов в акции.
    
    Инициализирует объект Market.

    ### Ancestors (in MRO)

    * interfaces.i_market_behaviour.IMarketBehaviour
    * interfaces.i_queue_behaviour.IQueueBehaviour
    * abc.ABC

    ### Methods

    `accept_to_market(self, buyer: classes.buyer.Buyer) ‑> None`
    :   Принимает покупателя на магазин.
        
        :arg :
            buyer (Buyer): Покупатель.
        
        :return :
            None

    `give_order(self) ‑> None`
    :   Выполняет выдачу заказов/возврат покупателям.
        
        :return :
            None

    `handle_promo(self, promo_buyer: classes.buyer.Buyer) ‑> None`
    :   Обрабатывает заказы для клиентов в акции.
        
        :arg :
            promo_buyer (Buyer): Покупатель в акции.
        
        :return :
            None

    `release_from_market(self, buyers: List[classes.buyer.Buyer]) ‑> None`
    :   Освобождает покупателей из магазина.
        
        :arg :
            buyers (List[Buyer]): Список покупателей.
        
        :return :
            None

    `release_from_queue(self) ‑> None`
    :   Освобождает покупателей из очереди.
        
        :return :
            None

    `take_in_queue(self, buyer: classes.buyer.Buyer) ‑> None`
    :   Принимает покупателя в очередь.
        
        :arg :
            buyer (Buyer): Покупатель.
        
        :return :
            None

    `take_order(self) ‑> None`
    :   Обрабатывает заказы покупателей (в том числе возврат).
        
        :return :
            None

    `update(self) ‑> None`
    :   Обновляет состояние магазина.
        
        :return :
            None

Module 02_homework.classes.buyer
================================

Classes
-------

`Buyer(name: str)`
:   Абстрактный класс, представляющий покупателя.
    
    :attr :
        name (str): Имя покупателя.
        is_take_order (bool): Флаг - получил ли покупатель заказ.
        is_make_order (bool): Флаг - сделал ли покупатель заказ.
        is_make_return (bool): Флаг - возвращает ли покупатель товар.
        is_have_returned (bool): Флаг - вернул ли покупатель товар.
    
    Methods:
        get_name() -> str:
            Возвращает имя покупателя.
    
    Инициализирует объект Buyer.
    
    :param :
        name (str): Имя покупателя.

    ### Ancestors (in MRO)

    * interfaces.i_return_order.IReturnOrder
    * interfaces.i_buyer_behaviour.IBuyerBehaviour
    * abc.ABC

    ### Methods

    `get_name(self) ‑> str`
    :   Возвращает имя покупателя.
        
        :return :
            (str): Имя покупателя.

Module 02_homework.classes.ordinary_client
==========================================

Classes
-------

`OrdinaryClient(name: str)`
:   Класс, представляющий обычного клиента.
    
    Attributes:
        name (str): Имя клиента.
        is_take_order (bool): Флаг - получил ли клиент заказ.
        is_make_order (bool): Флаг - сделал ли клиент заказ.
        is_make_return (bool): Флаг - возвращает ли клиент товар.
        is_have_returned (bool): Флаг - вернул ли клиент товар.
    
    Methods:
        get_name() -> str:
            Возвращает имя клиента.
        is_take_order() -> bool:
            Проверяет, получил ли клиент заказ.
        is_make_order() -> bool:
            Проверяет, сделал ли клиент заказ.
        set_take_order(take_order: bool) -> None:
            Устанавливает значение флага получения заказа.
        set_make_order(make_order: bool) -> None:
            Устанавливает значение флага совершения заказа.
        get_buyer():
            Возвращает самого клиента.
        is_make_return() -> bool:
            Проверяет, возвращает ли клиент товар.
        set_make_return(is_make_return: bool) -> None:
            Устанавливает значение флага возврата товара.
        is_have_returned() -> bool:
            Проверяет, вернул ли клиент товар.
        set_have_returned(is_have_returned: bool) -> None:
            Устанавливает значение флага возвращения товара.
    
    Инициализирует объект OrdinaryClient.
    
    :arg :
        name (str): Имя клиента.

    ### Ancestors (in MRO)

    * classes.buyer.Buyer
    * interfaces.i_return_order.IReturnOrder
    * interfaces.i_buyer_behaviour.IBuyerBehaviour
    * abc.ABC

    ### Methods

    `get_buyer(self)`
    :   Возвращает самого клиента.

    `get_name(self) ‑> str`
    :   Возвращает имя клиента.
        
        :return :
            str: Имя клиента.

    `is_have_returned(self) ‑> bool`
    :   Проверяет, вернул ли клиент товар.
        
        :return :
            bool: Флаг возвращения товара.

    `is_make_order(self) ‑> bool`
    :   Проверяет, сделал ли клиент заказ.
        
        :return :
            bool: Флаг совершения заказа.

    `is_make_return(self) ‑> bool`
    :   Проверяет, возвращает ли клиент товар.
        
        :return :
            bool: Флаг возврата товара.

    `is_take_order(self) ‑> bool`
    :   Проверяет, получил ли клиент заказ.
        
        :return :
            bool: Флаг получения заказа.

    `set_have_returned(self, is_have_returned: bool) ‑> None`
    :   Устанавливает значение флага возвращения товара.
        
        :arg :
            is_have_returned (bool): Значение флага возвращения товара.

    `set_make_order(self, make_order: bool) ‑> None`
    :   Устанавливает значение флага совершения заказа.
        
        :arg :
            make_order (bool): Значение флага совершения заказа.

    `set_make_return(self, is_make_return: bool) ‑> None`
    :   Устанавливает значение флага возврата товара.
        
        :arg :
            is_make_return (bool): Значение флага возврата товара.

    `set_take_order(self, take_order: bool) ‑> None`
    :   Устанавливает значение флага получения заказа.
        
        :arg :
            take_order (bool): Значение флага получения заказа.

Module 02_homework.classes.pensioner_client
===========================================

Classes
-------

`PensionerClient(name: str, pens_id: int)`
:   Класс, представляющий клиента-пенсионера.
    
    Attributes:
        name (str): Имя клиента.
        pens_id (int): Идентификатор пенсионера.
        is_take_order (bool): Флаг -  получил ли клиент заказ.
        is_make_order (bool): Флаг -  сделал ли клиент заказ.
        is_make_return (bool): Флаг -  возвращает ли клиент товар.
        is_have_returned (bool): Флаг -  вернул ли клиент товар.
    
    Methods:
        get_name() -> str:
            Возвращает имя клиента.
        is_take_order() -> bool:
            Проверяет, получил ли клиент заказ.
        is_make_order() -> bool:
            Проверяет, сделал ли клиент заказ.
        set_take_order(take_order: bool) -> None:
            Устанавливает значение флага получения заказа.
        set_make_order(make_order: bool) -> None:
            Устанавливает значение флага совершения заказа.
        get_buyer():
            Возвращает самого клиента.
        is_make_return() -> bool:
            Проверяет, возвращает ли клиент товар.
        set_make_return(is_make_return: bool) -> None:
            Устанавливает значение флага возврата товара.
        is_have_returned() -> bool:
            Проверяет, вернул ли клиент товар.
        set_have_returned(is_have_returned: bool) -> None:
            Устанавливает значение флага возвращения товара.
    
    Инициализирует объект PensionerClient.
    
    :arg :
        name (str): Имя клиента.
        pens_id (int): Идентификатор пенсионера.

    ### Ancestors (in MRO)

    * classes.buyer.Buyer
    * interfaces.i_return_order.IReturnOrder
    * interfaces.i_buyer_behaviour.IBuyerBehaviour
    * abc.ABC

    ### Methods

    `get_buyer(self)`
    :   Возвращает самого клиента.

    `get_name(self) ‑> str`
    :   Возвращает имя клиента.
        
        :return :
            str: Имя клиента.

    `is_have_returned(self) ‑> bool`
    :   Проверяет, вернул ли клиент товар.
        
        :return :
            bool: Флаг возвращения товара.

    `is_make_order(self) ‑> bool`
    :   Проверяет, сделал ли клиент заказ.
        
        :return :
            bool: Флаг совершения заказа.

    `is_make_return(self) ‑> bool`
    :   Проверяет, возвращает ли клиент товар.
        
        :return :
            bool: Флаг возврата товара.

    `is_take_order(self) ‑> bool`
    :   Проверяет, получил ли клиент заказ.
        
        :return :
            bool: Флаг получения заказа.

    `set_have_returned(self, is_have_returned: bool) ‑> None`
    :   Устанавливает значение флага возвращения товара.
        
        :arg :
            is_have_returned (bool): Значение флага возвращения товара.

    `set_make_order(self, make_order: bool) ‑> None`
    :   Устанавливает значение флага совершения заказа.
        
        :arg :
            make_order (bool): Значение флага совершения заказа.

    `set_make_return(self, is_make_return: bool) ‑> None`
    :   Устанавливает значение флага возврата товара.
        
        :arg :
            is_make_return (bool): Значение флага возврата товара.

    `set_take_order(self, take_order: bool) ‑> None`
    :   Устанавливает значение флага получения заказа.
        
        :arg :
            take_order (bool): Значение флага получения заказа.

Module 02_homework.classes.promotional_client
=============================================

Classes
-------

`PromoClient(name: str, promo_name: str, promo_cl_id: int)`
:   Класс PromoClient представляет клиента-участника акции.
    
    Attributes:
        promo_participants (dict): Словарь, содержащий количество
        участников для каждой акции.
        promo_name (str): Название акции.
        promo_cl_id (int): Идентификатор клиента-участника.
    
    Methods:
        get_name(self) -> str:
            Возвращает имя клиента.
        get_promo_participants(self) -> dict:
            Возвращает словарь с количеством участников для каждой акции.
        get_promo_num(self) -> int:
            Возвращает количество участников для текущей акции.
        is_take_order(self) -> bool:
            Возвращает флаг, указывающий, получил ли клиент заказ.
        is_make_order(self) -> bool:
            Возвращает флаг, указывающий, сделал ли клиент заказ.
        set_take_order(self, take_order: bool) -> None:
            Устанавливает флаг получения заказа.
        set_make_order(self, make_order: bool) -> None:
            Устанавливает флаг совершения заказа.
        get_buyer(self) -> Buyer:
            Возвращает объект Buyer, представляющий клиента.
         is_make_return() -> bool:
             Проверяет, возвращает ли клиент товар.
         set_make_return(is_make_return: bool) -> None:
             Устанавливает значение флага возврата товара.
         is_have_returned() -> bool:
             Проверяет, вернул ли клиент товар.
         set_have_returned(is_have_returned: bool) -> None:
             Устанавливает значение флага возвращения товара.
    
    Инициализирует объект PromoClient.
    
    Args:
        name (str): Имя клиента.
        promo_name (str): Название акции.
        promo_cl_id (int): Идентификатор клиента-участника.

    ### Ancestors (in MRO)

    * classes.buyer.Buyer
    * interfaces.i_return_order.IReturnOrder
    * interfaces.i_buyer_behaviour.IBuyerBehaviour
    * abc.ABC

    ### Class variables

    `promo_participants: dict`
    :

    ### Methods

    `get_buyer(self)`
    :   Возвращает самого клиента.

    `get_name(self) ‑> str`
    :   Возвращает имя клиента.
        
        :return :
            str: Имя клиента.

    `get_promo_num(self) ‑> int`
    :   Возвращает количество участников для текущей акции.
        
        :return :
            int: Количество участников.

    `get_promo_participants(self) ‑> dict`
    :   Возвращает словарь с количеством участников для каждой акции.
        
        :return :
            dict: Словарь акции и количества участников.

    `is_have_returned(self) ‑> bool`
    :   Проверяет, вернул ли клиент товар.
        
        :return :
            bool: Флаг возвращения товара.

    `is_make_order(self) ‑> bool`
    :   Проверяет, сделал ли клиент заказ.
        
        :return :
            bool: Флаг совершения заказа.

    `is_make_return(self) ‑> bool`
    :   Проверяет, возвращает ли клиент товар.
        
        :return :
            bool: Флаг возврата товара.

    `is_take_order(self) ‑> bool`
    :   Проверяет, получил ли клиент заказ.
        
        :return :
            bool: Флаг получения заказа.

    `set_have_returned(self, is_have_returned: bool) ‑> None`
    :   Устанавливает значение флага возвращения товара.
        
        :arg :
            is_have_returned (bool): Значение флага возвращения товара.

    `set_make_order(self, make_order: bool) ‑> None`
    :   Устанавливает значение флага совершения заказа.
        
        :arg :
            make_order (bool): Значение флага совершения заказа.

    `set_make_return(self, is_make_return: bool) ‑> None`
    :   Устанавливает значение флага возврата товара.
        
        :arg :
            is_make_return (bool): Значение флага возврата товара.

    `set_take_order(self, take_order: bool) ‑> None`
    :   Устанавливает значение флага получения заказа.
        
        :arg :
            take_order (bool): Значение флага получения заказа.

Module 02_homework.classes.special_client
=========================================

Classes
-------

`SpecialClient(name: str, vip_id: int)`
:   Класс, представляющий особого клиента.
    
    Attributes:
        name (str): Имя клиента.
        vip_id (int): Идентификатор VIP-клиента.
        is_take_order (bool): Флаг, указывающий получил ли клиент заказ.
        is_make_order (bool): Флаг, указывающий сделал ли клиент заказ.
        is_make_return (bool): Флаг, указывающий возвращает ли клиент товар.
        is_have_returned (bool): Флаг, указывающий вернул ли клиент товар.
    
    Methods:
        get_name() -> str:
            Возвращает имя клиента.
        is_take_order() -> bool:
            Проверяет, получил ли клиент заказ.
        is_make_order() -> bool:
            Проверяет, сделал ли клиент заказ.
        set_take_order(take_order: bool) -> None:
            Устанавливает значение флага получения заказа.
        set_make_order(make_order: bool) -> None:
            Устанавливает значение флага совершения заказа.
        get_buyer():
            Возвращает самого клиента.
        is_make_return() -> bool:
            Проверяет, возвращает ли клиент товар.
        set_make_return(is_make_return: bool) -> None:
            Устанавливает значение флага возврата товара.
        is_have_returned() -> bool:
            Проверяет, вернул ли клиент товар.
        set_have_returned(is_have_returned: bool) -> None:
            Устанавливает значение флага возвращения товара.
    
    Инициализирует объект SpecialClient.
    
    :arg :
        name (str): Имя клиента.
        vip_id (int): Идентификатор VIP-клиента.

    ### Ancestors (in MRO)

    * classes.buyer.Buyer
    * interfaces.i_return_order.IReturnOrder
    * interfaces.i_buyer_behaviour.IBuyerBehaviour
    * abc.ABC

    ### Methods

    `get_buyer(self)`
    :   Возвращает самого клиента.

    `get_name(self) ‑> str`
    :   Возвращает имя клиента.
        
        :return :
            str: Имя клиента.

    `is_have_returned(self) ‑> bool`
    :   Проверяет, вернул ли клиент товар.
        
        :return :
            bool: Флаг возвращения товара.

    `is_make_order(self) ‑> bool`
    :   Проверяет, сделал ли клиент заказ.
        
        :return :
            bool: Флаг совершения заказа.

    `is_make_return(self) ‑> bool`
    :   Проверяет, возвращает ли клиент товар.
        
        :return :
            bool: Флаг возврата товара.

    `is_take_order(self) ‑> bool`
    :   Проверяет, получил ли клиент заказ.
        
        :return :
            bool: Флаг получения заказа.

    `set_have_returned(self, is_have_returned: bool) ‑> None`
    :   Устанавливает значение флага возвращения товара.
        
        :arg :
            is_have_returned (bool): Значение флага возвращения товара.

    `set_make_order(self, make_order: bool) ‑> None`
    :   Устанавливает значение флага совершения заказа.
        
        :arg :
            make_order (bool): Значение флага совершения заказа.

    `set_make_return(self, is_make_return: bool) ‑> None`
    :   Устанавливает значение флага возврата товара.
        
        :arg :
            is_make_return (bool): Значение флага возврата товара.

    `set_take_order(self, take_order: bool) ‑> None`
    :   Устанавливает значение флага получения заказа.
        
        :arg :
            take_order (bool): Значение флага получения заказа.


Module 02_homework.classes.tax_service
======================================

Classes
-------

`TaxService()`
:   Класс, представляющий службу.
    
    Attributes:
        name (str): Имя службы.
        is_take_order (bool): Флаг, указывающий получила ли служба заказ.
        is_make_order (bool): Флаг, указывающий сделала ли служба заказ.
    
    Methods:
        get_name() -> str:
            Возвращает имя службы.
        is_take_order() -> bool:
            Возвращает флаг, указывающий получила ли служба заказ.
        is_make_order() -> bool:
            Возвращает флаг, указывающий сделала ли служба заказ.
        set_take_order(take_order: bool) -> None:
            Устанавливает флаг, указывающий получила ли служба заказ.
        set_make_order(make_order: bool) -> None:
            Устанавливает флаг, указывающий сделала ли служба заказ.
        get_buyer() -> Buyer:
            Возвращает экземпляр, представляющий службу.
        is_make_return() -> bool:
            Проверяет, возвращает ли служба товар.
        set_make_return(is_make_return: bool) -> None:
            Устанавливает значение флага возврата товара.
        is_have_returned() -> bool:
            Проверяет, вернула ли служба товар.
        set_have_returned(is_have_returned: bool) -> None:
            Устанавливает значение флага возвращения товара.
    
    Инициализирует объект TaxService.

    ### Ancestors (in MRO)

    * classes.buyer.Buyer
    * interfaces.i_return_order.IReturnOrder
    * interfaces.i_buyer_behaviour.IBuyerBehaviour
    * abc.ABC

    ### Methods

    `get_buyer(self)`
    :   Возвращает самого клиента.

    `get_name(self) ‑> str`
    :   Возвращает имя клиента.
        
        :return :
            str: Имя клиента.

    `is_have_returned(self) ‑> bool`
    :   Проверяет, вернула ли служба товар.
        
        :return :
            bool: Флаг возвращения товара.

    `is_make_order(self) ‑> bool`
    :   Проверяет, сделала ли служба заказ.
        
        :return :
            bool: Флаг совершения заказа.

    `is_make_return(self) ‑> bool`
    :   Проверяет, возвращает ли служба товар.
        
        :return :
            bool: Флаг возврата товара.

    `is_take_order(self) ‑> bool`
    :   Проверяет, получила ли служба заказ.
        
        :return :
            bool: Флаг получения заказа.

    `set_have_returned(self, is_have_returned: bool) ‑> None`
    :   Устанавливает значение флага возвращения товара.
        
        :arg :
            is_have_returned (bool): Значение флага возвращения товара.

    `set_make_order(self, make_order: bool) ‑> None`
    :   Устанавливает значение флага совершения заказа.
        
        :arg :
            make_order (bool): Значение флага совершения заказа.

    `set_make_return(self, is_make_return: bool) ‑> None`
    :   Устанавливает значение флага возврата товара.
        
        :arg :
            is_make_return (bool): Значение флага возврата товара.

    `set_take_order(self, take_order: bool) ‑> None`
    :   Устанавливает значение флага получения заказа.
        
        :arg :
            take_order (bool): Значение флага получения заказа.

