# hoznuzhdi
проект создания pdf странички с кассовым отчетом из программы СБИС++ 1.9, сбис будут формировать json файл и отправлять его скрипту а скрипт будет делать pdf и печатать его на принтер по умолчанию

формат json { "till": [ { "organization": "Юрлицо", "shop": "Магазин", "date": "Дата", "number": "Поряд. N", "refund_other_form": "Возврат иная ФО", "change_other_form": "Оплата иная ФО", "pay_cash": "Оплата нал", "pay_cashless": "Оплата безнал", "pay_sbp": "Оплата СБП", "refund_cash": "Возврат нал", "refund_cashless": "Возврат безнал", "refund_sbp": "Возврат СБП", "pay_gift_certificate": "Оплата серт.", "sales_gift_certificate": "Продажи серт.", "sales_items": "Продажи товар", "revenue": "Выручка", "zp": "З/П, соц", "other_expenses": "Прочий расход", "other_parish": "Прочий приход", "encashment": "Инкассация", "remaining_money": "Остаток денег в кассе", "cashier": "Кассир" } , { "organization": "ООО Клевер", "shop": "м-н Макси Детство", "date": "22.09.22", "number": "", "refund_other_form": 1529, "change_other_form": 1529, "pay_cash": 4050, "pay_cashless": 18996, "pay_sbp": 857, "refund_cash": 2000, "refund_cashless": 0, "refund_sbp": 658, "pay_gift_certificate": 500, "sales_gift_certificate": 1499, "sales_items": 24433, "revenue": 25932, "zp": " ", "other_expenses": " ", "other_parish": " ", "encashment": " ", "remaining_money": " ", "cashier": " " } , { "organization": "ООО Клевер", "shop": "м-н Макси Детство", "date": "22.09.22", "number": "", "refund_other_form": 0, "change_other_form": 0, "pay_cash": 0, "pay_cashless": 0, "pay_sbp": 0, "refund_cash": 0, "refund_cashless": 0, "refund_sbp": 0, "pay_gift_certificate": 0, "sales_gift_certificate": 0, "sales_items": 0, "revenue": 0, "zp": " ", "other_expenses": " ", "other_parish": " ", "encashment": " ", "remaining_money": " ", "cashier": " " } , { "organization": "ООО Клевер", "shop": "м-н Макси Детство", "date": "22.09.22", "number": "", "refund_other_form": 0, "change_other_form": 0, "pay_cash": 0, "pay_cashless": 0, "pay_sbp": 0, "refund_cash": 0, "refund_cashless": 0, "refund_sbp": 0, "pay_gift_certificate": 0, "sales_gift_certificate": 0, "sales_items": 0, "revenue": 0, "zp": " ", "other_expenses": " ", "other_parish": " ", "encashment": " ", "remaining_money": " ", "cashier": " " } , { "organization": "ООО Клевер", "shop": "м-н Макси Детство", "date": "22.09.22", "number": "", "refund_other_form": 0, "change_other_form": 0, "pay_cash": 0, "pay_cashless": 0, "pay_sbp": 0, "refund_cash": 0, "refund_cashless": 0, "refund_sbp": 0, "pay_gift_certificate": 0, "sales_gift_certificate": 0, "sales_items": 0, "revenue": 0, "zp": " ", "other_expenses": " ", "other_parish": " ", "encashment": " ", "remaining_money": " ", "cashier": " " } , { "organization": "ООО Клевер", "shop": "м-н Макси Детство", "date": "22.09.22", "number": "", "refund_other_form": 0, "change_other_form": 0, "pay_cash": 0, "pay_cashless": 0, "pay_sbp": 0, "refund_cash": 0, "refund_cashless": 0, "refund_sbp": 0, "pay_gift_certificate": 0, "sales_gift_certificate": 0, "sales_items": 0, "revenue": 0, "zp": " ", "other_expenses": " ", "other_parish": " ", "encashment": " ", "remaining_money": " ", "cashier": " " } ] }