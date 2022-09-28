# -*- coding: utf-8 -*-
import json
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import cm, mm
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import win32print
import win32api
from os.path import isfile
from os import remove as osrem
import glob
import time
from sys import exit
from typing import List

class Till(object):
    """
    класс наших касс для размещения на pdf
    """
    # def __init__(self, i_till: dict = {}):
    #     """
    #     param x: int координата х начала нашего объекта
    #     param y: int кордината y начала нашего объекта
    #     param org: str строка с организацией
    #     param i_font: int шрифт текста в нашем объекте
    #     param i_width:int ширина объекта
    #     param i_date: str дата в текстовом виде, строка
    #     param i_till: dict словарь с остальными строками объекта
    #     объект кассы будет инициализироваться
    #     координатами и строками с данными
    #     """
    #     # x: int = 0, y: int = 0, i_font: int = 12, i_width: int = 55,
    #     # self.x = x  #кордината x начала нашего объекта
    #     # self.y = y  #кордината y начала нашего объекта
    #     # self.i_font = i_font  #шрифт
    #     # self.column_width = i_width  #ширина
    #
    #     self.org = i_till.get('organization', ' ')  #строка с организацией
    #     self.shop = i_till.get('shop', ' ')  #строка с названием магазина
    #     self.date = i_till.get('date', ' ')  #строка с датой
    #     self.number = i_till.get('number', ' ')  # строка с датой
    #     self.sales_items = i_till.get('sales_items', 0)  #продажа товаров
    #     self.revenue = i_till.get('revenue', 0)  #выручка
    #     self.sales_gift_certificate = i_till.get('sales_gift_certificate', 0)  #продажа подарочных сертификатов
    #     self.pay_cashless = i_till.get('pay_cashless', 0)  #оплата безналом
    #     self.pay_cash = i_till.get('pay_cash', 0)  #оплата налом
    #     self.pay_other_form = i_till.get('refund_other_form', 0)  #сумма обмена, та сумма товара что покупателю отдали мы
    #     self.pay_sbp = i_till.get('pay_sbp', 0)  #сумма оплаты по СБП
    #     self.pay_gift_certificate = i_till.get('pay_gift_certificate', 0)  #оплата подарочными сертификатами
    #     self.refund_cash = i_till.get('refund_cash', 0)  #сумма возврат наличных
    #     self.refund_cashless = i_till.get('refund_cashless', 0)  #сумма возврат безнала
    #     self.refund_other_form = i_till.get('refund_other_form', 0)  #сумма обмена, та сумма товара что покупатель принес нам
    #     self.refund_sbp = i_till.get('refund_sbp', 0)  #возврат по СБП
    #     #следующие строки будут выводится пустыми, для заполнения вручную кассирами
    #     self.zp = i_till.get('zp', ' ')  #зарплата
    #     self.other_expenses = i_till.get('other_expenses', ' ')  #прочий расход
    #     self.other_parish = i_till.get('other_parish', ' ')  #прочий приход
    #     self.encashment = i_till.get('encashment', ' ')  #инкассация
    #     self.remaining_money = i_till.get('remaining_money', ' ')  #остаток денег в кассе
    #     self.cashier = i_till.get('cashier', ' ')  #кассир
    def __init__(self):
        """
        param x: int координата х начала нашего объекта
        param y: int кордината y начала нашего объекта
        param org: str строка с организацией
        param i_font: int шрифт текста в нашем объекте
        param i_width:int ширина объекта
        param i_date: str дата в текстовом виде, строка
        param i_till: dict словарь с остальными строками объекта
        объект кассы будет инициализироваться
        координатами и строками с данными
        """
        # x: int = 0, y: int = 0, i_font: int = 12, i_width: int = 55,
        # self.x = x  #кордината x начала нашего объекта
        # self.y = y  #кордината y начала нашего объекта
        # self.i_font = i_font  #шрифт
        # self.column_width = i_width  #ширина

        self.org = []
        self.shop = []
        self.date = []
        self.number = []
        self.sales_items = []
        self.sales_gift_certificate = []
        self.revenue = []
        self.pay_cashless = []
        self.pay_cash = []
        self.pay_other_form = []
        self.pay_sbp = []
        self.pay_gift_certificate = []
        self.refund_cash = []
        self.refund_cashless = []
        self.refund_sbp = []
        self.refund_other_form = []
        #следующие строки будут выводится пустыми, для заполнения вручную кассирами
        self.zp = []
        self.other_expenses = []
        self.other_parish = []
        self.encashment = []
        self.remaining_money = []
        self.cashier = []

    def make_list_table_row(self, i_till: dict = {}):
        self.org.append(i_till.get('organization', ' '))  #строка с организацией
        self.shop.append(i_till.get('shop', ' '))  #строка с названием магазина
        self.date.append(i_till.get('date', ' '))  #строка с датой
        self.number.append(i_till.get('number', ' '))  # строка с датой
        self.sales_items.append(i_till.get('sales_items', 0))  #продажа товаров
        self.sales_gift_certificate.append(i_till.get('sales_gift_certificate', 0))  #продажа подарочных сертификатов
        self.revenue.append(i_till.get('revenue', 0))  # выручка
        self.pay_cashless.append(i_till.get('pay_cashless', 0))  #оплата безналом
        self.pay_cash.append(i_till.get('pay_cash', 0))  #оплата налом
        self.pay_other_form.append(i_till.get('change_other_form', 0))  #сумма обмена, та сумма товара что покупателю отдали мы
        self.pay_sbp.append(i_till.get('pay_sbp', 0))  #сумма оплаты по СБП
        self.pay_gift_certificate.append(i_till.get('pay_gift_certificate', 0))  #оплата подарочными сертификатами
        self.refund_cash.append(i_till.get('refund_cash', 0))  #сумма возврат наличных
        self.refund_cashless.append(i_till.get('refund_cashless', 0))  #сумма возврат безнала
        self.refund_other_form.append(i_till.get('refund_other_form', 0))  #сумма обмена, та сумма товара что покупатель принес нам
        self.refund_sbp.append(i_till.get('refund_sbp', 0))  #возврат по СБП
        #следующие строки будут выводится пустыми, для заполнения вручную кассирами
        self.zp.append(i_till.get('zp', ' '))  #зарплата
        self.other_expenses.append(i_till.get('other_expenses', ' '))  #прочий расход
        self.other_parish.append(i_till.get('other_parish', ' '))  #прочий приход
        self.encashment.append(i_till.get('encashment', ' '))  #инкассация
        self.remaining_money.append(i_till.get('remaining_money', ' '))  #остаток денег в кассе
        self.cashier.append(i_till.get('cashier', ' '))  #кассир

    def make_data_for_table(self, i_style):
        """
        метода составления данных для объекта таблица в репортлаб
        :param i_style:
        :return:
        """
        o_data = []
        for attr in self.__dir__():
            table_row = []
            if attr.startswith('__') is False:
                if isinstance(getattr(self, attr), list):
                    i_list = getattr(self, attr)
                    print(i_list)
                    for i_str in i_list:
                        table_row.append(Paragraph(str(i_str), i_style))
                    if len(table_row) > 0:
                        o_data.append(table_row)
        return o_data


def make_pdf_page(c, i_tills):
        """
        функция создания объекта pdf страницы
        :param c: объект pdf
        :param qr_data: str строка c QR кодом
        :param vtext: str строка с текстом на ценнике
        :param vtext_price: str строка с ценой
        :param shop: str строка с названием магазина
        cross_out: bool флаг зачернутый текст будет или нет
        :return: file
        """
        pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))
        pdfmetrics.registerFont(TTFont('ArialBold', 'arialbd.ttf'))
        c_width = c.__dict__['_pagesize'][0]
        c_height = c.__dict__['_pagesize'][1]
        vtext_font_size = 12
        c.setFont('Arial', vtext_font_size)
        pole = 15 * mm
        ytext = c_height - vtext_font_size * 1.5
        xstart = pole
        # the magic is here
        styles = getSampleStyleSheet()  # дефолтовые стили
        styles['Normal'].fontName = 'Arial'
        i_styles = styles['Normal']
        data = i_tills.make_data_for_table(i_styles)
        rowHeights = []
        colWidths = []
        for _ in range(len(data)):
            rowHeights.append(6 * mm)
        for _ in range(len(data[0])):
            colWidths.append(4.5 * cm)
        table = Table(data=data, colWidths=colWidths, rowHeights=rowHeights)
        table.setStyle(TableStyle([('ALIGN', (1, 1), (-2, -2), 'RIGHT'),
                                ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                                ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                                ]))
        table.wrapOn(c, c_width, c_height)
        table.drawOn(c, pole, pole)
        c.save()


def del_pdf_in_folder(i_path_pdf):
    """
    функция очистки папки от использованых pdf
    :param i_path_pdf: str путь до папки в котрой лежaт pdf
    :return:
    """
    file_queue = [f for f in glob.glob(i_path_pdf + "*.pdf") if isfile(f)]
    if len(file_queue) > 0:
        for i in file_queue:
            osrem(i)


def sendtoprinter():
    """
    функция отправки на печать pdf файлов из папки
    :return:
    """
    old_printer = win32print.GetDefaultPrinter()
    new_printer = win32print.SetDefaultPrinter('Honeywell PC42t plus (203 dpi)')
    # file_queue = [f for f in glob.glob("%s\\*.pdf" % source_path) if isfile(f)]
    file_queue = [f for f in glob.glob("d:\\files\\*.pdf") if isfile(f)]
    if len(file_queue) > 0:
        for i in file_queue:
            if i.find('99999999999999999999999999999999') == -1:
                error_level = print_file(i, new_printer)
                print(i)
    time.sleep(15)
    # if len(file_queue) > 0:
    #     for i in file_queue:
    #         osrem(i)
    win32print.SetDefaultPrinter(old_printer)
    return error_level


def print_file(pfile, printer):
    """
    функция отправки на принтер конкретного файла,
    используем винапи
    :param pfile: str полное имя файла
    :param printer: str имя принтера как в винде
    :return:
    """
    error_level = win32api.ShellExecute(
        0,
        "print",
        '%s' % pfile,
        '/d:"%s"' % printer,
        ".",
        0
    )
    return error_level


def make_tills(i_path: str = 'r:\\', i_fname: str = 'hoznuzhdi.json') -> List[Till]:
    """
    получаем список наших обектов-столбцов таблицы
    :param i_path:
    :param i_fname:
    :return:
    """
    with open(i_path+i_fname) as json_file:
        data = json.load(json_file)
    print(data)
    o_tills = Till()
    for elem in data['till']:
        if elem['sales_items'] != 0 and elem['refund_other_form'] != 0:
            o_tills.make_list_table_row(i_till=elem)
    return o_tills


def main():
    i_path = 'r:\\'
    i_name = 'hoznuzhdi.json'
    del_pdf_in_folder(i_path)
    shop_tills = make_tills(i_path=i_path, i_fname=i_name)
    pdf_canvas = canvas.Canvas('r:\\hoznuzhdi.pdf', pagesize=landscape(A4))
    make_pdf_page(pdf_canvas, shop_tills)


error = main()
exit(error)
