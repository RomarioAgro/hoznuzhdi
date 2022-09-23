# -*- coding: utf-8 -*-
import json
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import cm, mm
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
    def __init__(self, org: str = '', shop: str = '', i_date: str = '01.01.2022', i_till: dict = {}):
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

        self.org = org  #строка с организацией
        self.shop = shop  #строка с названием магазина
        self.date = i_date  #строка с датой
        self.sales_items = i_till.get('sales_items', 0)  #продажа вещей
        self.revenue = i_till.get('revenue', 0)  #выручка
        self.sales_gift_certificate = i_till.get('sales_gift_certificate', 0)  #продажа подарочных сертификатов
        self.pay_cashless = i_till.get('pay_cashless', 0)  #оплата безналом
        self.pay_cash = i_till.get('pay_cash', 0)  #оплата налом
        self.pay_other_form = i_till.get('change_sum', 0)  #сумма обмена, та сумма товара что покупателю отдали мы
        self.pay_sbp = i_till.get('pay_sbp', 0)  #сумма оплаты по СБП
        self.pay_gift_certificate = i_till.get('pay_gift_certificate', 0)  #оплата подарочными сертификатами
        self.refund_cash = i_till.get('refund_cash', 0)  #сумма возврат наличных
        self.refund_cashless = i_till.get('refund_cashless', 0)  #сумма возврат безнала
        self.refund_other_form = i_till.get('change_sum', 0)  #сумма обмена, та сумма товара что покупатель принес нам
        self.refund_sbp = i_till.get('refund_sbp', 0)  #возврат по СБП
        #следующие строки будут выводится пустыми, для заполнения вручную кассирами
        self.zp = i_till.get('zp', ' ')  #зарплата
        self.other_expenses = i_till.get('other_expenses', ' ')  #прочий расход
        self.other_parish = i_till.get('other_parish', ' ')  #прочий приход
        self.encashment = i_till.get('encashment', ' ')  #инкассация
        self.remaining_money = i_till.get('remaining_money', ' ')  #остаток денег в кассе
        self.cashier = i_till.get('cashier', ' ')  #кассир

def make_pdf_page(c):
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
        vtext = 'Юрлицо'
        ytext = text_on_page(c, vtext=vtext, vtext_font_size=vtext_font_size, xstart=pole, ystart=c_height - pole,
                             xfinish=pole + 55 * mm)
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



def text_on_page(canvs, vtext: str = 'Test', vtext_font_size: int = 10, xstart: int = 0, ystart: int = 0,
                 xfinish: int = 170, cross_out:bool = False):
    """
    функция размещения текста на нашем объекте pdf
    :param canvs: obj сам объект pdf
    :param vtext: str текст который будем размещать
    если текст не входит в одну строку, то будем делать переносы,
    поэтому по выходу надо знать на какой высоте объект уже занят
    :param vtext_font_size: int размер шрифта
    :param xstart: int стартовая координата X
    :param ystart: int стартовая координата Y
    :param xfinish: int финишная координата X
    :return: int финишная координата Y, на какой высоте остановились
    """
    from reportlab.pdfbase.pdfmetrics import stringWidth

    # xstart, ystart start coordinates our text string
    vtext_result = ''
    for char in vtext:
        x_text_print = xstart + stringWidth(vtext_result, 'Arial', vtext_font_size)
        if x_text_print < xfinish:
            vtext_result = vtext_result + char
        else:
            canvs.drawString(xstart, ystart, vtext_result)
            if cross_out is True:
                cross_out_y = ystart + vtext_font_size // 3
                canvs.line(xstart, cross_out_y, xstart + stringWidth(vtext_result, 'Arial', vtext_font_size), cross_out_y)
            if char != " ":
                vtext_result = char
            else:
                vtext_result = ""
            ystart = ystart - vtext_font_size
    else:
        canvs.drawString(xstart, ystart, vtext_result)
        if cross_out is True:
            cross_out_y = ystart + vtext_font_size // 3
            canvs.line(xstart, cross_out_y, xstart + stringWidth(vtext_result, 'Arial', vtext_font_size), cross_out_y)
    return ystart


# def make_pdf_page(c, qr_data: str = '99999', vtext: str = 'zaglushka', vtext_price: str = '000000',
#                   shop: str = 'not shop', sale='00000'):
def make_list_of_till(i_path: str = 'r:\\', i_fname: str = 'hoznuzhdi.json') -> List[Till]:
    o_list = []
    with open(i_path+i_fname) as json_file:
        data = json.load(json_file)
    print(data)
    for elem in data['till']:
        if elem['sales_items'] != 0 and elem['change_sum'] != 0:
            o_list.append(Till(org=data['organization'], shop=data['shop'], i_date=data['date'], i_till=elem))
    return o_list



def main():
    i_path = 'r:\\'
    i_name = 'hoznuzhdi.json'
    del_pdf_in_folder(i_path)
    list_shop = make_list_of_till(i_path=i_path, i_fname=i_name)
    print(list_shop)
    pdf_canvas = canvas.Canvas('r:\\hoznuzhdi.pdf', pagesize=landscape(A4))
    make_pdf_page(pdf_canvas)
    # pdf_canvas = canvas.Canvas('r:\\hoznuzhdi.pdf', pagesize=landscape(A4))
    # pdf_canvas.drawString(100, 100, 'jkjkjkj')
    # pdf_canvas.save()


error = main()
exit(error)
