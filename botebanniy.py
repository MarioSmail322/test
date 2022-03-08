import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id


def main():
    """ Пример создания клавиатуры для отправки ботом """

    vk_session = vk_api.VkApi(token='402a2b58ec3d27507ff3d0ead04dfaf0fad19152552a130402fdb3b0645538a65e204d8b709447e1a3a0d')
    vk = vk_session.get_api()

    keyboard = VkKeyboard(one_time=None)

    keyboard.add_button('/find', color=VkKeyboardColor.SECONDARY)
    keyboard.add_button('/wanted', color=VkKeyboardColor.POSITIVE)
    keyboard.add_button('/scr', color=VkKeyboardColor.POSITIVE)
    

    vk.messages.send(
        peer_id=2000000001,
        random_id=get_random_id(),
        keyboard=keyboard.get_keyboard(),
        message='Клавиатура работает'
    )


if __name__ == '__main__':
    main()