class MixturesEncoderDecoder():
    """Class for operations on data strings"""
    def __init__(self):
        """Default MixturesEncoderDecoder constructor"""

    def decodeString(self, inputText):
        """Decodes a string to data readable by the model"""
        # Splitting inputText into parts
        twoPart = inputText.split(' ')
        # Beginning = ratios
        ratioString = twoPart[0]
        # End = labels
        labelString = twoPart[-1]
        # Split labels and ratios on a set character
        recentRatios = ratioString.split(':')
        recentLabels = labelString.split('/')

        # Type conversion str -> int
        recentRatios = list(map(int,recentRatios))

        # Calculating total mass
        totalMass = sum(recentRatios)
        recentRatios = [totalMass] + recentRatios

        return [recentRatios, recentLabels]

    def encodeData(self, ratios, labels):
        """Encodes data to a single string"""
        ratioString = ':'.join(map(str, ratios))
        labelString = '/'.join(labels)

        # Formatting for a better visualisation
        ratioString = '{:<20}'.format(ratioString)

        # Putting strings together
        return ratioString + labelString
