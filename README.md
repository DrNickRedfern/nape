# nape
The normalised aggregated power envelope (nape) is a representation of an audio signal calculated by summing the columns of the short-time Fourier transform (STFT).

The function `nape` uses librosa for digital signal processing an returns a data frame with the times of the short-time spectra and the envelope values.

This approach will work with any audio file, but I have found it to be particularly useful when analysing film soundtracks.

For a detailed discussion of this method see my tutorial of this method at [https://www.academia.edu/43289938/Computational_analysis_of_a_horror_film_trailer_soundtrack_with_Python](https://www.academia.edu/43289938/Computational_analysis_of_a_horror_film_trailer_soundtrack_with_Python).

## How to use `nape`
The function is very easy to use and requires only a handful of arguments:

* audio: an audio file
* sr: the sampling rate of the audio file in Hz
* mono: `nape` requires a mono audio file, so if `mono = False` the file will be converted to mono
* nfft: the number of samples within a window when calcualating the STFT
* hop: the number of audio samples betwen adjacent spectra in the STFT
* norm: the aggregated power envelope is normalised to a unit area by default but the non-normalised envelope can be obtained with `norm = False`

To demonstrate, we can apply nape to Brad Sucks' 'Total Breakdown,' which you can download under a Attribution-ShareAlike 3.0 International License here: [https://freemusicarchive.org/music/Brad_Sucks/Out_Of_It/07\_-\_Brad_Sucks\_-\_Total_Breakdown](https://freemusicarchive.org/music/Brad_Sucks/Out_Of_It/07_-_Brad_Sucks_-_Total_Breakdown).

To calculate the envelope we create a data frame `df` using `nape`:

```Python
df = nape(path/to/audio/file, sr = 44100, mono = False, nfft = 2048, hop = 512, norm = True)
```

|   | time  | nape  |
| :-----: | :-: | :-: |
| 0 | 0.000000 | 7.566067e-07 |
| 1 | 0.011609 | 1.469769e-06 |
| 2 | 0.023219 | 2.246583e-06 |
| 3 | 0.034828 | 3.218146e-06 |
| 4 | 0.046438 | 3.266896e-06 |


The result can then be plotted using

```Python
import matplotlib.pyplot as plt

plt.figure(figsize = (10, 6))
plt.plot(df['time'], df['nape'], color = '#2C115F')
plt.xlabel('Time (s)') 
plt.ylabel('Normalized power')

```

which will return:

![nape demonstration](images/demo_nape.jpg?raw=true)
