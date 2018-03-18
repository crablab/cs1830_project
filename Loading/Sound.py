import sched
import time
import copy

class SoundManager:
    def __init__(self, sound_dict):
        self.sound_dict = sound_dict

        self.sound_sched = sched.scheduler(time.time, time.sleep)

        self.active_sound_dict = {}

        self.sound_bg_name = None

        self.test_isPlaying  = False

    def updateSoundDict(self, sound_dict):
        self.sound_dict.update(sound_dict)

    def update(self):
        self.sound_sched.run(False)

    def __removeSound(self, sound_id):
        self.active_sound_dict.pop(sound_id)

    def playSound(self, sound_name):
        if sound_name in self.sound_dict:
            i = 0
            while (i in self.active_sound_dict):
                i +=1
                
            sound = copy.copy(self.sound_dict[sound_name])
            time_delay = self.sound_dict[sound_name]._get_length()
            
            self.sound_sched.enter(time_delay, 2, self.__removeSound, kwargs={"sound_id":i})
            self.active_sound_dict.update({i:sound})

            self.active_sound_dict[i].play()
                        

    def setContinuousBG(self, sound_name):
        if sound_name in self.sound_dict:
            self.sound_bg_name = sound_name
            self.__playBG()

    def __playBG(self):
        if (self.sound_bg_name != None) and (self.sound_bg_name in self.sound_dict):
            self.sound_dict[self.sound_bg_name].rewind()
            self.sound_dict[self.sound_bg_name].play()
            
            time_delay = self.sound_dict[self.sound_bg_name]._get_length()
            self.sound_sched.enter(time_delay, 1, self.__playBG)

"""
s1 = simplegui._load_local_sound(<fileName>)
    create a sound object using relative file name, eg "a.wav"
    .wav's work havent tested others

s1.set_volume(<float>)
    set volume, float from 0 to 1, default 1

s = Sound(<sound dict>)
    dict is of form {<String sound_name>:<sound object>}
    basically name to refer to sound object and the sound object

s.setContinuousBG(<String sound_name>)
    set which sound is going on repeat in background

s.playSound(<String sound_name>)
    set sound that will play till completion and stop,
    can have multiple of same sound_name playing at once
"""
