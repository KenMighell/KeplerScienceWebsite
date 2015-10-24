Title: K2 technical information
Save_as: k2-photometric-performance.html

[TOC]

## Summary

The K2 mission is described in detail in [Howell et al. (2014)](http://adsabs.harvard.edu/abs/2014PASP..126..398H).  We summarize key aspects of the mission here, relevant for conducting observations with K2.

The Kepler spacecraft hosts a 0.95-m aperture Schmidt telescope in an Earth-trailing heliocentric orbit, which insures a thermally stable 
environment and provides the ability to remain on a single pointing for the
duration of each Campaign. 
Pointing is maintained by a combination of two reaction wheels and thrusters, 
reacting to motion data provided by fine guidance sensors 
(fine-point observing) or star trackers (coarse-point observing). 

With only two remaining reaction wheels, 
these operations are only possible while pointing within 
the orbital plane of the spacecraft, which approximates to the ecliptic. 
Only this specific family of pointings yields operational configurations 
where solar pressure is largely mitigated by spacecraft geometry, 
thereby making viable precision pointing and photometry 
approaching the quality achieved for the Kepler mission. 

Science observations are taken at one of two timing settings: long (30-min) or short (1-min) cadence. When in fine-point observing, [K2 is capable of achieving a benchmark photometric precision](k2-photometric-performance.html#fine-point-photometric-precision) on an m<sub>V</sub> = 12 G2V star of 170 parts-per-million (ppm) in 30 minutes of integration, i.e., one long cadence exposure. 
This corresponds to ~50 ppm over a 6.5-hour transit 
of an Earth-sized body around that star.

While stars brighter than m<sub>V</sub> = 11.5 will saturate some pixels, 
K2 performs well on stars as bright as m<sub>V</sub> = 4, 
provided the scientific benefit justifies the large number of pixels 
needed to capture saturated flux bleeding along CCD columns. 
Kepler also has many faint-target scientific applications 
where m<sub>V</sub> = 20 objects yield a photometric precision 
of 10% over 30 minutes.

The broad photometric bandpass has a half-maximum transmission range 
of 430 to 840 nm. 
The instrument has neither changeable filters, 
dispersing elements, nor a shutter. 
The detector has a pixel scale of 3.98 arcseconds. 
Image quality varies with position in the focal plane, 
with the 95% encircled energy diameter ranging from 3.1 to 7.5 pixels with a median value of 4.2 pixels. 
The percentage of point-source flux concentrated in the center pixel 
is between 20% and 62% with a median value of 45%.

## Data products

Constraints imposed by onboard storage and communications 
dictate that at most 6% of the data from the full focal plane 
are saved and downloaded. 
Instead, data for specific, predetermined targets are saved 
and transmitted as subimages with a typical area of 160 pixels, 
depending on source brightness. 
The brighter a target, the more pixels required to capture it. 
Pixel apertures can be tailored further to accommodate 
extended or very bright, saturated objects. The Kepler Science Center derives pixel masks for those targets 
successfully justified by proposers and uploads these targets 
to the spacecraft before each Campaign. 

It is expected that on the order of 10,000 to 20,000 long cadence targets and 50 to 100 short cadence targets will be available per Campaign.  The number of observed targets in each Campaign varies based on the density of the field and on how many extended or bright objects are observed.  Such objects require larger aperture sizes and decrease the total number of targets available.  These targets must be justified carefully.

Data distribution and archival services are performed 
by the Space Telescope Science Institute’s 
<a href="https://archive.stsci.edu/k2">MAST archive</a>. 
Final data products available to observers 
include original and calibrated pixel values 
and light curves for each individual target (starting in Campaign 3). 
The calibration corrects for bias level, smear, galactic cosmic rays, 
flat fielding, dark current, background, and instrument noise. 
Simple aperture photometry is used to generate long cadence light curves (starting in Campaign 3). 

Data is delivered in Flexible Image Transport System (FITS) format. 
A thorough understanding of the noise sources and systematic errors of K2 
is needed by observers in order to generate their own light curves 
from the original (uncalibrated or calibrated) pixel data 
or interpret structure found in archived light curves.

There is no exclusive use period associated with any K2 data.

A comprehensive list of data products for K2 is given [here](data-releases.html#k2-product-overview).


## Photometric performance

The photometric precision is dependent primarily 
upon motion of the spacecraft boresight on jitter timescales 
shorter than an exposure length 
and solar-induced drift timescales longer than an exposure. 

### Reaction wheel jitter

During engineering tests between Oct-Dec 2013, 
the spacecraft collected data in a coarse-point mode. 
The measured Full-Width Half Maximum of the coarse-point 
K2 Point-Spread Function is a measure of spacecraft jitter 
and is within 5% of the fine-point Kepler Point-Spread Function 
across the entire field-of-view. 

The figure below provides a fit of the Kepler fine-point Point-Spread Function to a K2 coarse-point target close to the spacecraft boresight. 
From top-left to bottom-right: a 30 min observation of a 12th magnitude K2 star, the best-fitting Kepler PSF model, the best-fit model binned over detector pixels, and the fit residual. Spacecraft jitter during two-wheel operation is therefore generally only a few percent larger than the three-wheel Kepler mission and is not a major concern for K2 photometric precision. 

<a href="http://keplerscience.arc.nasa.gov/K2/images/Dec2013PRF.png"><img src="http://keplerscience.arc.nasa.gov/K2/images/Dec2013PRF.png" style="max-width: 640px;"></a>


### Solar pressure-induced drift

Low-frequency motion due to solar pressure and subsequent thruster firings cause targets to drift across detector pixels and is the dominant factor in photometric precision after photon statistics. The frequency of reaction wheel momentum resaturations and thruster-controlled pointing tweaks will be tuned to trade photometric precision with pixel mask size and fuel consumption. During the Dec 2013 test, resaturations occurred on a 48-hour cycle and pointing tweaks every 12 hours. Thruster firings kept targets localized to within three pixels across the duration of the 6-day test run. For the purposes of providing a photometric precision measure that can be compared with the Kepler mission, an uncrowded 12th magnitude target is selected for showcasing and its sensitivity to a 6-hour duration planet transit is measured. After defining a pixel mask to contain the 3-pixel focal-plane drift of the target, motion systematics and stellar astrophysics are removed from the subsequently derived Simple Aperture Photometry time series with a 48-hour Savitzky-Golay filter (a standard method to prepare stellar light curves for transit searches). The subsequent median 6-hr photometric precision of a 12th mag target is 87 ppm (94 &micro;mag). This is within a factor of 4 of the fine-point Kepler mission precision for quiet G dwarfs. The blue shaded regions represent times associated with reaction wheel resaturations and engineering tests. The data collected during these intervals were clipped from the time-series. 

<a href="http://keplerscience.arc.nasa.gov/K2/images/Dec2013SAP.png"><img src="http://keplerscience.arc.nasa.gov/K2/images/Dec2013SAP.png" style="max-width: 640px;"></a>

A major activity during ongoing testing is the measurement of thermal alignment changes between star trackers and boresight throughout a campaign. This calibration will allow more precise pointing control, smaller pixel masks and consequently more targets per Campaign. There remains room for further improvements in photometric precision by optimizing the frequency of pointing resets and acquiring guide stars for fine-guidance tracking. As described in the following section, pointing and guiding optimization has allowed K2 to achieve photometric precisions that rival the Kepler mission.


### Fine-point photometric precision

Fine-point operations were achieved and maintained during the Feb 2014 engineering test. The plot below compares a 12th magnitude target observed during the Dec 2013 coarse-point operations (left) with a 12th magnitude target collected in fine-point (right). The spacecraft pointed in different directions for these two tests and therefore this is not a like-for-like comparison - the nature and intrinsic variability of both targets is unknown. Nevertheless, in this example, fine-point increases the photometric precision relative to coarse-point by a factor of 2. In both plots, the blue curve is 30-min cadence data, the red diamonds are the same data, binned to 6 hours. The dashed line represents the 1-&sigma; standard deviation of the 30-min data. The median 6-hr photometric precision of the 12th magnitude coarse-point target is 82 ppm, while the same measure for the fine-point target is 44 ppm.

<a href="http://keplerscience.arc.nasa.gov/K2/images/Feb2014SAP.png"><img src="http://keplerscience.arc.nasa.gov/K2/images/Feb2014SAP.png" style="max-width: 640px;"></a>

The following plot provides an ensemble comparison of Kepler three-wheel fine-point precision (red), K2 two-wheel coarse-point precision (green) and K2 two-wheel fine-point precision (blue). The red lines are carefully-selected quiet G dwarfs, falling upon arbitrary modules of the Kepler detector. The green points are stars of unknown spectral type and intrinsic variability and therefore the scatter around a power law fit (dashed line) is considerably larger than the Kepler sample. The K2 fine-point ensemble has been extracted from pixels using apertures optimized for signal-to-noise, and systematic, motion-related structure has been calculated and subtracted using singular value deconvolution across the ensemble of light curves. The large scatter demonstrates that the engineering targets display a range of intrinsic astrophysical variability, however, the noise floor suggests that K2 fine-point data is a significant improvement upon coarse-point quality and approaches the photometric precision of the Kepler archive. 

<a href="http://keplerscience.arc.nasa.gov/K2/images/Feb2014Precision.png"><img src="http://keplerscience.arc.nasa.gov/K2/images/Feb2014Precision.png" style="max-width: 640px;"></a>

The series of plots below contain the same 11th magnitude target, observed during the Feb 2014 fine-point observations. In each a Mandel-Agol planet transit model has been injected, assuming the star is solar-size and the planet has an orbital period of 1.5 days. In each curve four transits have therefore been injected over a 9-day time series and folded upon the orbital period. Such Jupiters (top-left), Neptunes (top-right) and Super-Earths (bottom-left) will be readily detected by current planet searching algorithms. The 6-hr 5-&sigma; Earth-like transit depth (bottom-right) will be challenging, just as it is in the Kepler time-series, but will becoming increasingly significant with more recorded transits.

<a href="http://keplerscience.arc.nasa.gov/K2/images/Feb2014Injection.png"><img src="http://keplerscience.arc.nasa.gov/K2/images/Feb2014Injection.png" style="max-width: 640px;"></a>
