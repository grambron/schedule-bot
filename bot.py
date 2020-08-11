import telebot
import keyboards
from keyboards import new_keyboard
from state_manager import StateManager
from node_manager import NodeManager

bot = telebot.TeleBot("1395352900:AAF-V0aHMRuBGUJSF1VmwN0ieesnTSHdvEM")
commands = {
    'привет': 'Привет',
    'пока': 'не уходи из 34:('
}
state_manager = StateManager()
node_manager = NodeManager()


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет", reply_markup=keyboards.start)


@bot.message_handler(content_types=['text'])
def send_text(message):
    state = state_manager.get_state(message.chat.id)
    node = node_manager.get_node(state)
    keyboard = new_keyboard(node.buttons)
    bot.send_message(message.chat.id, node.text, reply_markup=keyboard)
    # text = commands.get(message.text.lower(), 'О чем ты вообще?')
    # bot.send_message(message.chat.id, text)


if __name__ == '__main__':
    bot.polling()
