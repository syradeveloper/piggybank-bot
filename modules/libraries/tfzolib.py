import random

class generators():
    def motivation_gen():
        motivation_list = [
            'Каждая копейка имеет значение',
            'Твои сбережения растут с каждым днем',
            'Продолжай откладывать, и скоро ты достигнешь своей цели',
            'Маленькие шаги ведут к большим результатам',
            'С каждым вкладом ты становишься ближе к мечте',
            'Твоя копилка становится тяжелее каждый день',
            'Твои усилия принесут плоды',
            'Накопление денег – это инвестиция в твое будущее',
            'Ты на правильном пути к финансовой независимости',
            'Экономия сегодня – процветание завтра',
            'Твой упорство поможет тебе накопить нужную сумму',
            'Каждая монетка, отложенная сегодня, работает на твое будущее',
            'Ты становишься все ближе к своей финансовой цели',
            'Твои накопления растут, и это впечатляет',
            'Каждая отложенная сумма приближает тебя к мечте',
            'Ты справляешься с задачей экономии отлично',
            'Твои финансовые цели становятся реальностью',
            'Каждая монета в копилке – шаг к мечте',
            'Ты движешься в правильном направлении',
            'Продолжай в том же духе, и ты добьешься успеха',
            'Накопленные деньги – это твоя свобода',
            'Ты можешь гордиться своими достижениями',
            'Твои усилия в экономии впечатляют',
            'Ты становишься все успешнее в накоплении денег',
            'Каждая копейка имеет значение для достижения твоих целей',
            'Ты движешься к своей финансовой независимости',
            'Твои старания и упорство приведут тебя к успеху',
            'Ты молодец, продолжаешь откладывать',
            'Каждая отложенная сумма приближает тебя к мечте',
            'Ты на правильном пути к финансовому благополучию',
        ]
        return random.choice(motivation_list)