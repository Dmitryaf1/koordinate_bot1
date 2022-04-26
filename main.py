from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from XYtoBL import anketa_start, koord_X, koord_Y, zona_N
from BLtoXY import anketa2_start, koord_B, koord_L, zona_N2
from XYtoXY import anketa3_start, koord_X2, koord_Y2, zona_N3
from functions import keyboard_start, anketa_end
import settings
def greet_user(update, context):
    print('вызов функции')
    update.message.reply_text('Привет пользователь! Выбери задачу', reply_markup=keyboard_start)

def main():
    global text
    mybot2 = Updater(settings.API_KEY, use_context=True)
    dp = mybot2.dispatcher
    command_end = CommandHandler('start', anketa_end)

    anketa = ConversationHandler(
        entry_points=[
            MessageHandler(Filters.regex('^(Переход от прямоугольных координат к геодезическим)$'), anketa_start)],
        states={
            'x': [MessageHandler(Filters.text, koord_X), command_end],
            'y': [MessageHandler(Filters.text, koord_Y), command_end],
            'N': [MessageHandler(Filters.text, zona_N), command_end],
        },
        fallbacks=[]
    )
    anketa2 = ConversationHandler(
        entry_points=[
            MessageHandler(Filters.regex('^(Переход от геодезических координат к прямоугольным)$'), anketa2_start)],
        states={
            'B': [MessageHandler(Filters.text, koord_B), command_end],
            'L': [MessageHandler(Filters.text, koord_L), command_end],
            'N': [MessageHandler(Filters.text, zona_N2), command_end],
        },
        fallbacks=[]
    )
    anketa3 = ConversationHandler(
        entry_points=[
            MessageHandler(Filters.regex('^(Пересчет прямоугольных координат из зоны в зону)$'), anketa3_start)],
        states={
            'x': [MessageHandler(Filters.text, koord_X2), command_end],
            'y': [MessageHandler(Filters.text, koord_Y2), command_end],
            'N': [MessageHandler(Filters.text, zona_N3), command_end],
        },
        fallbacks=[]
    )
    dp.add_handler(CommandHandler('start', greet_user))

    dp.add_handler(anketa)
    dp.add_handler(anketa2)
    dp.add_handler(anketa3)

    mybot2.start_polling()
    mybot2.idle()

if __name__ =='__main__':
    main()

