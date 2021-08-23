def nape(audio, sr, mono = False, nfft = 2048, hop = 512, norm = True):
    
    """
    
    Normalised aggregated power envelope (nape).
    
    The normalised aggregated power envelope is a representation of an audio signal
    calculated by summing the columns of the short-time Fourier transform (STFT).
    
    This function uses librosa for audio processing: https://librosa.org/doc/latest/index.html
    
    Parameters
    ----------
    audio : an audio file, loaded using librosa.load().
    
    sr : the sampling rate of the audio file in Hz.
    
    mono : is the audio file mono or stereo - if false, stereo files will be converted to mono using librosa.to_mono().
    
    nfft : the number of samples within a window, which should be a power of 2  - passed to librosa.stft() as n_fft.
    
    hop : the number of audio samples betwen adjacent spectra in the STFT - passed to librosa.stft() as hop_length.
    
    norm : the default is to aggregated power envelope is normalised to a unit area. If False the envelope is not normalised.
    

    Returns
    -------
    a data frame with two columns:
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
    
    import librosa
    import numpy as np
    import pandas as pd
    
    # load audio file and convert to mono
    y, sr = librosa.load(audio, sr, mono = mono)
    if mono == False:
        y = librosa.to_mono(y)
    else:
        y = y
    
    # calculate the short-time Fourier transform
    D = np.abs(librosa.stft(y, n_fft = nfft, hop_length = hop))
    
    # Sum the columns of the STFT and normalise if requried
    nape = np.sum(D, axis = 0) 
    if norm == True:
        nape = nape/sum(nape)
    else:
        nape = nape
    
    # set times of spectra
    times = [x / (len(nape) / (len(y) / sr)) for x in list(range(0, len(nape)))]
    
    # collect and return as a data frame
    return pd.DataFrame(data = {'time': times, 'nape': nape})