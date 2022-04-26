from telegram import ReplyKeyboardRemove, ParseMode
from telegram.ext import ConversationHandler
from Pereschet_XY_to_BL import pereschet_XY_to_BL, answer
from functions import func, keyboard, kontrol

def anketa_start(update, context):
    update.message.reply_text('Введите координату х:', reply_markup=ReplyKeyboardRemove())
    return 'x'

def koord_X(update, context):
    global x
    x = kontrol(update, update.message.text)
    context.user_data['anketa'] = {'x': x}
    update.message.reply_text('Введите координату y:')
    return 'y'

def koord_Y(update, context):
    global y
    y = kontrol(update, update.message.text)
    context.user_data['anketa'] = {'y': y}
    update.message.reply_text('Введите зону N:')
    return 'N'

def zona_N(update, context):
    global x, y, n, B, L
    n = int(kontrol(update, update.message.text))
    context.user_data['anketa'] = {'N': n}

    B, L = pereschet_XY_to_BL(x, y, n)
    if B>0  and L>0  and n>0 and n<=60:
        user_text = answer(B, L, x, y, n)
    else:
        user_text = 'Возможна ошибка в исходных данных'
    update.message.reply_text(user_text, reply_markup=keyboard, parse_mode=ParseMode.HTML)
    return ConversationHandler.END






