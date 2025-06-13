"""
File to define the Track class, which represents a track in a project.
"""
import numpy as np
import librosa

class Track:
    def __init__(self, path: str, to_mono: bool = False):
        """
        Initialize a Track object with the given path.

        :param path: The path to the track file.
        """
        self.path = path
        self.mono = False
        if to_mono:
            self.mono= True
        self.data, self.sample_rate = librosa.load(path, sr=None, mono=self.mono)
        #Check if the track is mono or stereo
        self.duration = self.duration  # Calculate duration based on the loaded data

    def __repr__(self):
        """
        Return a string representation of the Track object.

        :return: A string representation of the Track object.
        """
        return f"Track(path={self.path}, sample_rate={self.sample_rate}, duration={self.duration:.2f} seconds)"
        
    @property
    def is_mono(self):
        """
        Check if the track is mono.

        :return: True if the track is mono, False otherwise.
        """
        return np.squeeze(self.data).ndim == 1
        

    @property
    def duration(self):
        """
        Calculate the duration of the track in seconds.

        :return: The duration of the track in seconds.
        """
        return len(self.data) / self.sample_rate
    
    def to_mono(self):
        """
        Convert the track to mono if it is not already.

        :return: The mono version of the track.
        """
        if self.mono:
            return self.data
        else:
            data = librosa.to_mono(self.data)
            self.mono = True
            return data

    


        