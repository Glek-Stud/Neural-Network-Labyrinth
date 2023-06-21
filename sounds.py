from pygame import mixer, time


class Sounds:
    def end_game_sound(self):
        # load mp3
        sound = mixer.music.load("end_game.mp3")
        # play
        mixer.music.play()


    def step_sound(self):
        mixer.music.load("step.mp3")

        mixer.music.play(-1)

    def train_sound(self):
        mixer.music.load("training.mp3")

        mixer.music.play()

    def start_noiral_sound(self):
        pass

    def stop(self):

        mixer.music.stop()
