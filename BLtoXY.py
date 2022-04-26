from telegram import ReplyKeyboardRemove, ParseMode
from Pereschet_BL_to_XY import pereschet_BL_to_XY, answe
from telegram.ext import ConversationHandler
from functions import keyboard, kontrol
from Message_File import message_B, message_L

def anketa2_start(update, context):
    update.message.reply_text(message_B, reply_markup=ReplyKeyboardRemove(), parse_mode=ParseMode.HTML)
    return 'B'

def koord_B(update, context):
    global B
    B = kontrol(update, update.message.text)
    context.user_data['anketa2'] = {'B': B}
    update.message.reply_text(message_L, reply_markup=ReplyKeyboardRemove(), parse_mode=ParseMode.HTML)
    return 'L'

def koord_L(update, context):
    global L
    L = kontrol(update, update.message.text)
    context.user_data['anketa2'] = {'L': L}
    update.message.reply_text('Введите зону N:')
    return 'N'

def zona_N2(update, context):
    global n, B, L, x, y
    n = int(kontrol(update, update.message.text))
    context.user_data['anketa2'] = {'N': n}
    x, y = pereschet_BL_to_XY(B, L, n)

    if B>0 and B<360 and L>0 and L<360 and n>0 and n<=60:

        user_text = answe(B, L, x, y, n)
    else:
        user_text = 'Возможна ошибка в исходных данных'

    update.message.reply_text(user_text, reply_markup=keyboard, parse_mode=ParseMode.HTML)
    return ConversationHandler.END



