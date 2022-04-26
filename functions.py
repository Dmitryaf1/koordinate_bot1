from telegram import ReplyKeyboardMarkup
from telegram.ext import ConversationHandler

def zone(n):
    L0 = 6*n-3
    return L0

def func(grm):
    grad = int(grm / 3600)

    min = int((grm / 3600 - grad) * 60)
    sec = round(((grm / 3600 - grad) * 60 - min) * 60, 3)
    return grad, min, sec

def angle(B):
    B = int(B / 3600) + int((B / 3600 - int(B / 3600)) * 60) / 100 + round(((B / 3600 - int(B / 3600))
     * 60 - int((B / 3600 - int(B / 3600)) * 60)) * 60, 3) / 10000
    return B

def grad(B):
    B = int(B) + int((B - int(B)) * 100) / 60 + ((B - int(B)) * 100 - int((B - int(B)) * 100)) * 100 / 3600
    return B

def kontrol(update, var):
    try:
        for update.message.text in var:
            var = float(var)
            print(type(var))
            return var
    except ValueError:
        update.message.reply_text('Введены некорректные данные', reply_markup=keyboard)
        return ConversationHandler.END


keyboard = ReplyKeyboardMarkup([['/start']], resize_keyboard=True)
keyboard_start = ReplyKeyboardMarkup([['Переход от прямоугольных координат к геодезическим'],
                                    ['Переход от геодезических координат к прямоугольным'],
                                    ['Пересчет прямоугольных координат из зоны в зону']], resize_keyboard=True)
def anketa_end(update, context):
    update.message.reply_text('Завершение работы')
    return ConversationHandler.END