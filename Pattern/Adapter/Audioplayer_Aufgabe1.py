class AudioPlayer:
    def play_mp3(self, file_name):
        return f"Spiele MP3-Datei ab: {file_name}"

class WAVPlayer:
    def play_wav(self, file_name):
        return f"Spiele WAV-Datei ab: {file_name}"

class AudioAdapter:
    def __init__(self, wav_player):
        self.wav_player = wav_player

    def play_mp3(self, file_name):
        return self.wav_player.play_wav(file_name)



audio_player = AudioPlayer()
print(audio_player.play_mp3("song.mp3"))

wav_player = WAVPlayer()
adapter1 = AudioAdapter(wav_player)
print(adapter1.play_mp3("song.wav"))