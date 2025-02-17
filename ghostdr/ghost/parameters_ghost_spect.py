# This parameter file contains the parameters related to the primitives located
# in the primitives_ghost_spect.py file, in alphabetical order.

from gempy.library import config

from geminidr.core import parameters_ccd, parameters_visualize, parameters_preprocess

from astrodata import AstroData as ad

def arcs_valueCheck(value):
    """Validate applyFlatBPMConfig.arcs"""
    return len(value) == 2 and isinstance(
        value[0], str) and isinstance(
        value[1], str)


class addWavelengthSolutionConfig(config.Config):
    suffix = config.Field("Filename suffix", str, "_wavelengthAdded",
                          optional=True)
    arcs = config.ListField("Before & after arcs for each input",
                            tuple, None, optional=True, single=False)


class applyFlatBPMConfig(config.Config):
    suffix = config.Field("Filename suffix", str, "_flatBPMApplied",
                          optional=True)
    flat = config.ListField("Flat field to use", (str, ad), None,
                            optional=True, single=True)
    flat_stream = config.Field("Stream to obtain flat field from", str, None,
                               optional=True)
    write_result = config.Field("Write primitive output to disk?", bool, True,
                                optional=True)


class barycentricCorrectConfig(config.Config):
    suffix = config.Field("Filename suffix", str, "_barycentricCorrected",
                          optional=True)
    correction_factor = config.Field("Barycentric correction factor", float,
                                     None, optional=True)


class clipSigmaBPMConfig(config.Config):
    suffix = config.Field("Filename suffix", str, "_sigmaBPMClipped",
                          optional=True)
    sigma = config.Field("Sigma value for clipping", float, 3.0)
    iters = config.Field("Number of clipping iterations", int, None,
                         optional=True)
    bpm_value = config.Field("BPM value to give to clipped pixels", int, 1)


class darkCorrectConfig(parameters_preprocess.darkCorrectConfig):
    def setDefaults(self):
        self.suffix = "_darkCorrected"
        self.dark = None
        self.do_cal = "skip"


class extractProfileConfig(config.Config):
    suffix = config.Field("Filename suffix", str, "_extractedProfile",
                          optional=True)
    slit = config.ListField("Slit viewer exposure", (str, ad), None,
                            optional=True, single=True)
    slitflat = config.ListField("Slit viewer flat field", (str, ad), None,
                                optional=True, single=True)
    flat = config.ListField("Flat field", (str, ad), None,
                            optional=True, single=True)
    sky_correct = config.Field("Correct for sky?", bool, True,
                               optional=True)
    smooth_flat_spatially = config.Field(
        "Smooth the flat field image before applying?", bool, False,
        optional=True
    )
    flat_precorrect = config.Field("Pre-correct by the flat field?", bool, True,
                                   optional=True)
    write_result = config.Field("Write primitive output to disk?", bool, False,
                                optional=True)


class interpolateAndCombineConfig(config.Config):
    suffix = config.Field("Filename suffix", str, "_interpdAndCombined",
                          optional=True)
    scale = config.ChoiceField("Output wavelength scale", str, {
        'linear': 'Linear wavelength scale',
        'loglinear': 'Log-linear wavelength scale'
    }, default='loglinear')
    skip = config.Field("No-op this primitive?", bool, False, optional=True)
    oversample = config.Field("(Approx.) oversampling of output wavelength "
                              "scale", float, 2.0)


class findAperturesConfig(config.Config):
    suffix = config.Field("Filename suffix", str, "_findAper",
                          optional=True)
    slitflat = config.Field("Slit viewer flat field",
                            (str, ad),
                            None, optional=True)
    flat = config.ListField("Flat field", (str, ad), None,
                            optional=True, single=True)
    skip_pixel_model = config.Field('Skip adding a pixel model to the '
                                    'flat field?', bool, False)


class fitWavelengthConfig(config.Config):
    suffix = config.Field("Filename suffix", str, "_fitWavl",
                          optional=True)
    flat = config.ListField("Flat field", (str, ad), None,
                            optional=True, single=True)
    # inspect_fit = config.Field("Use matplotlib to inspect fit quality?", bool,
    #                            False, optional=True)
    plot_fit = config.Field("Use matplotlib to inspect fit quality?", bool,
                            False, optional=True)


class flatCorrectConfig(config.Config):
    skip = config.Field("No-op this primitive?", bool, False, optional=True)
    suffix = config.Field("Filename suffix", str, "_flatCorrected",
                          optional=True)
    slit = config.Field("Slit viewer exposure", (str, ad), None, optional=True)
    slitflat = config.ListField("Slit viewer flat field", (str, ad), None,
                                optional=True, single=True)
    flat = config.ListField("Processed flat field exposure", (str, ad), None,
                            optional=True, single=True)
    write_result = config.Field("Write primitive output to disk?", bool, True,
                                optional=True)


class formatOutputConfig(config.Config):
    suffix = config.Field("Filename suffix", str, "_formattedOutput",
                          optional=True)
    detail = config.ChoiceField("Level of detail", str, {
        'default': 'Default output',
        'processed_image': 'Include processed CCD image',
        'flat_profile': 'Include flat profile',
        'sensitivity_curve': 'Include computed sensitivity curve',
    }, default='default')


class overscanCorrectConfig(parameters_ccd.overscanCorrectConfig):
    def setDefaults(self):
        self.suffix = '_overscanCorrect'
        self.niterate = 2
        self.high_reject = 3.0
        self.low_reject = 3.0
        self.function = 'poly'
        self.nbiascontam = 4
        self.order = 0


class rejectCosmicRaysConfig(config.Config):
    suffix = config.Field("Filename suffix", str, "_cosmicRaysRejected",
                          optional=True)
    subsampling = config.Field("Subsampling factor", int, 2)
    sigma_lim = config.Field("Sigma clipping value", float, 15.0)
    f_lim = config.Field("lacosmicx f_lim value", float, 5.0)
    n_steps = config.Field("Number of iterations", int, 1)


class responseCorrectConfig(config.Config):
    suffix = config.Field("Filename suffix", str, "_responseCorrected",
                          optional=True)
    skip = config.Field("No-op this primitive?", bool, False, optional=True)
    std = config.Field("Standard star (observed)", (str, ad), None,
                       optional=True)
    std_spec = config.Field("Standard star reference spectrum", (str, ad), None,
                            optional=True)
    write_result = config.Field("Write primitive output to disk?", bool, True,
                                optional=True)


class tileArraysConfig(parameters_visualize.tileArraysConfig):
    def setDefaults(self):
        self.suffix = "_arraysTiled"
