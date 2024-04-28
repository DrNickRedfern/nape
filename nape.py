import librosa
import numpy as np
import pandas as pd

def nape(path: str, sr: int = 22050, mono: bool = True, nfft: int = 2048, hop: int = 512, norm: bool = True) -> pd.Dataframe:
    """
    Normalised aggregated power envelope (nape).
    
    The normalised aggregated power envelope is a representation of an audio signal
    calculated by summing the columns of the short-time Fourier transform (STFT).
    
    This function uses librosa for audio processing: https://librosa.org/doc/latest/index.html
    
    Parameters
    ----------
    path (str): the path to an audio file, loaded using librosa.load().
    
    sr (int, optional): the target sampling rate in Hz. Defaults to 22050 Hz.
    
    mono (bool, optional): is the audio file mono or stereo - if False, stereo files will be converted to mono using librosa.to_mono(). Defaults to True.
    
    nfft (int, optional): the number of samples within a window, which should be a power of 2  - passed to librosa.stft() as n_fft. Defaults to 2048.
    
    hop (int, optional): the number of audio samples betwen adjacent spectra in the STFT - passed to librosa.stft() as hop_length. Defaults to 512.
    
    norm (bool, optional): the default is to aggregated power envelope is normalised to a unit area. If False the envelope is not normalised. Defaults to True.
    
    Returns
    -------
    pandas.DataFrame: a data frame with two columns:
        times: the times of the spectra in the STFT
        nape: the normalised aggregated power envelope

    Examples
    --------
    df = nape(audio, sr = 48000, mono = True, nfft = 2048, hop = 512, norm = False)
    
    References
    ----------
    For a demonstration of this method see 
    https://www.academia.edu/43289938/Computational_analysis_of_a_horror_film_trailer_soundtrack_with_Python 

    """
    # Check inputs are valid
    if not isinstance(sr, (int, np.integer)) or (sr < 0):
        raise ValueError("sr must be a positive integer")
    
    if not isinstance(hop, (int, np.integer)) or (hop < 0):
        raise ValueError("hop must be a positive integer")
    
    if not isinstance(nfft, (int, np.integer)) or (nfft < 0):
        raise ValueError("nfft must be a positive integer")
    
    # Load audio file and convert to mono if necessary
    audio: np.ndarray[np.float32] = librosa.load(path, sr = sr, mono = mono)[0]
    if not mono:
        y = librosa.to_mono(audio)
    
    # Calculate the short-time Fourier transform
    D: np.ndarray[np.float32] = np.abs(librosa.stft(audio, n_fft = nfft, hop_length = hop))
    
    # Sum the columns of the STFT and normalise if requried
    nape: np.ndarray[np.float32] = np.sum(D, axis = 0)
    if norm:
        nape = nape/sum(nape)
    
    # Set times of spectra
    times: list[float] = [x/(len(nape) / (len(y)/sr)) for x in list(range(0, len(nape)))]
    
    # Collect and return as a data frame
    return pd.DataFrame(data = {'time': times, 'nape': nape})