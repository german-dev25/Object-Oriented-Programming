Module 02_homework.interfaces.i_buyer_behaviour
===============================================

Classes
-------

`IBuyerBehaviour()`
:   Интерфейс для определения поведения покупателя.
    
    Methods:
        is_take_order() -> bool:
            Проверяет, получил ли покупатель заказ.
    
        is_make_order() -> bool:
            Проверяет, сделал ли покупатель заказ.
    
        set_take_order(take_order: bool) -> None:
            Устанавливает флаг получения заказа для покупателя.
    
        set_make_order(make_order: bool) -> None:
            Устанавливает флаг сделанного заказа для покупателя.
    
        get_buyer():
            Возвращает объект покупателя.

    ### Ancestors (in MRO)

    * abc.ABC

    ### Methods

    `get_buyer(self)`
    :   Возвращает объект покупателя.

    `is_make_order(self) ‑> bool`
    :   Проверяет, сделал ли покупатель заказ.
        
        :return :
            bool: Флаг, указывающий сделал ли покупатель заказ.

    `is_take_order(self) ‑> bool`
    :   Проверяет, получил ли покупатель заказ.
        
        :return :
            bool: Флаг, указывающий получил ли покупатель заказ.

    `set_make_order(self, make_order: bool) ‑> None`
    :   Устанавливает флаг сделанного заказа для покупателя.
        
        :arg :
            make_order (bool): Флаг, указывающий сделал ли покупатель заказ.

    `set_take_order(self, take_order: bool) ‑> None`
    :   Устанавливает флаг получения заказа для покупателя.
        
        :arg :
            take_order (bool): Флаг, указывающий получил ли покупатель заказ.

Module 02_homework.interfaces.i_market_behaviour
================================================

Classes
-------

`IMarketBehaviour()`
:   Интерфейс для определения поведения магазина.
    
    Methods:
        accept_to_market(buyer: Buyer) -> None:
            Принимает покупателя в магазин.
    
        release_from_market(buyers: List[Buyer]) -> None:
            Освобождает покупателей из магазина.
    
        update() -> None:
            Обновляет состояние магазина.

    ### Ancestors (in MRO)

    * abc.ABC

    ### Methods

    `accept_to_market(self, buyer: classes.buyer.Buyer) ‑> None`
    :   Принимает покупателя в магазин.
        
        :arg:
            buyer (Buyer): Покупатель.
        
        :return :
            None

    `release_from_market(self, buyers: List[classes.buyer.Buyer]) ‑> None`
    :   Освобождает покупателей из магазина.
        
        :arg:
            buyers (List[Buyer]): Список покупателей.
        
        :return :
            None

    `update(self) ‑> None`
    :   Обновляет состояние магазина.
        
        :return :
            None

Module 02_homework.interfaces.i_queue_behaviour
===============================================

Classes
-------

`IQueueBehaviour()`
:   Интерфейс, представляющий поведение очереди магазина.
    
    Methods:
        take_in_queue(buyer: Buyer) -> None:
            Помещает покупателя в очередь.
    
        release_from_queue() -> None:
            Удаляет покупателя из очереди.
    
        take_order() -> None:
            Обрабатывает получение заказа покупателем.
    
        give_order() -> None:
            Обрабатывает выдачу заказа покупателю.

    ### Ancestors (in MRO)

    * abc.ABC

    ### Methods

    `give_order(self) ‑> None`
    :   Обрабатывает выдачу заказа покупателю.
        
        :return :
            None

    `release_from_queue(self) ‑> None`
    :   Удаляет покупателя из очереди.
        
        :return :
            None

    `take_in_queue(self, buyer: classes.buyer.Buyer) ‑> None`
    :   Помещает покупателя в очередь.
        
        :arg :
            buyer (Buyer): Покупатель.
        
        :return :
            None

    `take_order(self) ‑> None`
    :   Обрабатывает получение заказа покупателем.
        
        :return :
            None

Module 02_homework.interfaces.i_return_order
============================================

Classes
-------

`IReturnOrder()`
:   Интерфейс, представляющий возврат товара в магазине.
    
    Methods:
        is_make_return() -> bool:
            Проверяет, возвращает ли покупатель товар.
    
        set_make_return(is_make_return: bool) -> None:
            Устанавливает флаг возврата товара для покупателя.
    
        is_have_returned() -> bool:
            Проверяет, вернул ли покупатель товар.
    
        set_have_returned(is_have_returned: bool) -> None:
            Устанавливает флаг успешного возврата товара для покупателя.

    ### Ancestors (in MRO)

    * abc.ABC

    ### Methods

    `is_have_returned(self) ‑> bool`
    :   Проверяет, вернул ли покупатель товар.
        
        :return :
            bool: Флаг, указывающий вернул ли покупатель товар.

    `is_make_return(self) ‑> bool`
    :   Проверяет, возвращает ли покупатель товар.
        
        :return :
            bool: Флаг, указывающий возвращает ли покупатель товар.

    `set_have_returned(self, is_have_returned: bool) ‑> None`
    :   Устанавливает флаг успешного возврата товара для покупателя.
        
        :arg :
            is_have_returned (bool): Флаг, указывающий вернул ли покупатель товар.
        
        :return :
            None

    `set_make_return(self, is_make_return: bool) ‑> None`
    :   Устанавливает флаг возврата товара для покупателя.
        
        :arg :
            is_make_return (bool): Флаг, указывающий возвращает ли покупатель товар.
        
        :return :
            None