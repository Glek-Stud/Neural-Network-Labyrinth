from pygame import mixer, time


class Sounds:
    @staticmethod
    def end_game_sound():
        mixer.music.load("sound/end_game.mp3")
        mixer.music.play()

    @staticmethod
    def step_sound():
        mixer.music.load("sound/step.mp3")
        mixer.music.play(-1)

    @staticmethod
    def button_train_sound():
        mixer.music.load("sound/training.mp3")
        mixer.music.play()

    @staticmethod
    def button_switch_sound(switch):
        if switch:
            mixer.music.load("sound/turn_off.mp3")
        else:
            mixer.music.load("sound/turn_on.mp3")
        mixer.music.play()
        time.wait(170)

    @staticmethod
    def stop():
        mixer.music.stop()
