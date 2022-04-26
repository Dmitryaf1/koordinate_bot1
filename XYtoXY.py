from telegram import ReplyKeyboardRemove, ParseMode, ReplyKeyboardMarkup
from telegram.ext import ConversationHandler
from Pereschet_XY_to_BL import pereschet_XY_to_BL
from Pereschet_BL_to_XY import pereschet_BL_to_XY
from functions import angle

def anketa3_start(update, context):
    update.message.reply_text('Введите координату х:', reply_markup=ReplyKeyboardRemove())
    return 'x'

def koord_X2(update, context):
    global x
    x = float(update.message.text)
    context.user_data['anketa'] = {'x': x}
    update.message.reply_text('Введите координату y:')
    return 'y'

def koord_Y2(update, context):
    global y
    y = float(update.message.text)
    context.user_data['anketa'] = {'y': y}
    update.message.reply_text('Введите зону N:')
    return 'N'

def zona_N3(update, context):
    global n, x, y
    n = int(update.message.text)
    context.user_data['anketa'] = {'N': n}

    Xstart = x
    Ystart = y

    B, L = pereschet_XY_to_BL(x, y, n)
    if n == 60:
        n2 = 1
    else:
        n2 = n+1
    B = angle(B)
    L = angle(L)
    x, y = pereschet_BL_to_XY(B, L, n2)

    if B>0  and L>0  and n>0 and n<=60:
        user_text = f"""
            <b>Прямоугольные координаты</b>
            <b>Координата х</b>: {Xstart}
            <b>Координата y</b>: {Ystart}
            <b>Зона </b>: {n}
            ------------------------
            <b>Пересчитанные координаты</b>
            <b>Зона </b>: {n2}
            <b>Координата х</b>: {x}
            <b>Координата y</b>: {y}
        """
    else:
        user_text = 'Возможна ошибка в исходных данных'

    keyboard = ReplyKeyboardMarkup([['/start']], resize_keyboard=True)
    update.message.reply_text(user_text, reply_markup=keyboard, parse_mode=ParseMode.HTML)
    return ConversationHandler.END

