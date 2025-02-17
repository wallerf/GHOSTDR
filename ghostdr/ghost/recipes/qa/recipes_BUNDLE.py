"""
Recipes available to data with tags: GHOST, BUNDLE, RAW, UNPREPARED
Default is "makeProcessedBundle".
"""
recipe_tags = set(['GHOST', 'BUNDLE', 'RAW', 'UNPREPARED'])

def makeProcessedBundle(p):
    """
    This recipe processes GHOST observation bundles.

    Parameters
    ----------
    p : Primitives object
        A primitive set matching the recipe_tags.
    """
    p.splitBundle()
    return

_default = makeProcessedBundle
