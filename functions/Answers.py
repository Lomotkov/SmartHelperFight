from functions.GenerateResp import *
from utils.CorrectAnswer import correct_name_end


def dima(event):
    return generate_response_text("Погодите а вот его трогать не стоит",
                                  event
                                  )


def shot(event):
    return generate_response_with_tts("Перестрелка",
                                      "",
                                      "<speaker audio=\"dialogs-upload"
                                      "/7fc0f449-e743-4b28-8d13-c7b678bb59d7/096d56e9-deee-46c1"
                                      "-b5d1-2e573b79e933.opus\">",
                                      event
                                      )


def enemy(event):
    return generate_response_with_tts("Враги в доме",
                                      "Разойдись, свинопасы, или госпожа "
                                      "голосовой помощник вам таких люлей отвесят, вовек не забудете",
                                      "<speaker audio=\"dialogs-upload/7fc0f449-e743-4b28-8d13-c7b678bb59d7"
                                      "/6fe441de-2550-412d"
                                      "-b1ae-e3432ae7dfb4.opus\">",
                                      event
                                      )


def fight(text, event):
    if 'бой' in text:
        if ' с ' in text:
            name = text[text.find(' с ') + 3:]
        else:
            name = text[text.find('бой') + 3:]
        name = correct_name_end(name)
        return generate_response_with_tts("НАЧАТЬ БОЙ",
                                          name + ", приготовь свою жопу",
                                          "<speaker audio=\"dialogs-upload/7fc0f449-e743-4b28-8d13-c7b678bb59d7"
                                          "/7869c646-c0ea-4b42-b594-488131bad5e4.opus\">",
                                          event
                                          )

