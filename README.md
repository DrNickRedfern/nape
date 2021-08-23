# nape
The normalised aggregated power envelope (nape) is a representation of an audio signal calculated by summing the columns of the short-time Fourier transform (STFT).

For a detailed discussion of this method see my tutorial at [https://www.academia.edu/43289938/Computational_analysis_of_a_horror_film_trailer_soundtrack_with_Python](https://www.academia.edu/43289938/Computational_analysis_of_a_horror_film_trailer_soundtrack_with_Python).

## How to use the function
The function is very easy to use and requires only a handful of arguments:

The result can then be plotted using:

```Python
import matplotlib.pyplot as plt

plt.figure(figsize = (10, 6))
plt.plot(res['time'], res['nape'], color = '#2C115F')
plt.xlabel('Time (s)') 
plt.ylabel('Normalized power')

```

Which will return:


