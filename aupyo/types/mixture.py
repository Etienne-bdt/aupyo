from .track import Track
from typing import Dict

class Mixture:
    """
    A class representing a mixture of audio signals.
    
    Attributes:
        signals (list): A list of audio signals in the mixture.
    """
    
    def __init__(self, signals=None):
        """
        Initializes the Mixture with a Dict of audio signals.
        
        Args:
            signals (dict): A dict of audio signals to be included in the mixture.
        """
        if signals is None:
            signals = {}
        if not isinstance(signals, dict):
            raise TypeError("Signals must be a dictionary with instrument names as keys and Track objects as values.")
        self.signals: Dict[Track] = signals

    def __repr__(self):
        """
        Returns a string representation of the Mixture object.
        
        Returns:
            str: A string representation of the Mixture object.
        """
        return f"Mixture(signals={self.signals.keys()})"
    
    def add_signal(self, instrument:str, track: Track):
        """
        Adds a new audio signal to the mixture.
        
        Args:
            track (Track): The audio signal to be added to the mixture.
        """
        self.signals[instrument] = track

    def remove_signal(self, instrument: str):
        """
        Removes an audio signal from the mixture.
        
        Args:
            instrument (str): The name of the instrument to be removed from the mixture.
        """
        if instrument in self.signals:
            del self.signals[instrument]
        else:
            raise KeyError(f"Instrument '{instrument}' not found in the mixture.")
        
    def get_signal(self, instrument: str) -> Track:
        """
        Retrieves an audio signal from the mixture.
        
        Args:
            instrument (str): The name of the instrument to retrieve.
        
        Returns:
            Track: The audio signal associated with the specified instrument.
        """
        if instrument in self.signals:
            return self.signals[instrument]
        else:
            raise KeyError(f"Instrument '{instrument}' not found in the mixture.")
        
    def __getitem__(self, instrument: str) -> Track:
        """
        Allows access to audio signals using the instrument name as a key.
        
        Args:
            instrument (str): The name of the instrument to retrieve.
        
        Returns:
            Track: The audio signal associated with the specified instrument.
        """
        return self.get_signal(instrument)
    
    def __setitem__(self, instrument: str, track: Track):
        """
        Allows setting an audio signal using the instrument name as a key.
        Args:
            instrument (str): The name of the instrument to set.
            track (Track): The audio signal to be associated with the specified instrument.
        """
        if not isinstance(track, Track):
            raise TypeError("The value must be a Track object.")
        self.add_signal(instrument, track)
    
    def __delitem__(self, instrument: str):
        """
        Allows deletion of an audio signal using the instrument name as a key.
        Args:
            instrument (str): The name of the instrument to be removed.
        """
        self.remove_signal(instrument)

    def __contains__(self, instrument: str) -> bool:
        """
        Checks if an audio signal exists in the mixture using the instrument name.
        
        Args:
            instrument (str): The name of the instrument to check.
        
        Returns:
            bool: True if the instrument exists in the mixture, False otherwise.
        """
        return instrument in self.signals
    
    def __len__(self) -> int:
        """
        Returns the number of audio signals in the mixture.
        Returns:
            int: The number of audio signals in the mixture.
        """
        return len(self.signals)
    def __iter__(self):
        """
        Allows iteration over the instruments in the mixture.
        Returns:
            Iterator: An iterator over the instruments in the mixture.
        """
        return iter(self.signals.items())
