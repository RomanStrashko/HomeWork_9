from bot import bot


async def start_game(message):
    await bot.send_message(message.from_user.id, f'Привет {message.from_user.first_name}, давай сыграем в игру "конфеты!\n'
                                                 f'На столе лежит 150 конфет, нам с тобой нужно по очереди'
                                                 f'брать от 1 до 28 конфет за ход, кто последний заберет конфеты со стола,'
                                                 f'тот и выграл.')



async def player_take(message):
    await bot.send_message(message.from_user.id, f'Возьми от 1 до 28 конфет')


async def table_info(message, name1, take, total_count, name2):
    await bot.send_message(message.from_user.id, f'{name1} взял {take} конфет, \n'
                           f'на столе осталось {total_count} конфет \n'
                           f'ход {name2}')
async def win(message, name, take, total_count):
    await bot.send_message(message.from_user.id, f'{name} взял {take} конфет, \n'
                                                 f'на столе осталось {total_count} конфет \n'
                                                 f'{name} победил!')

async def wrong_take(message):
    await bot.send_message(message.from_user.id, f'Ты взял слишком много конфет, попробуй снова!')
