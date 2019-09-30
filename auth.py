import tweepy


def keys():
    auth = tweepy.OAuthHandler("NML5Rsg1sxEh5eeGuSPtcpfVd",
                'S4097EtaPD0HhVTOIyXWedOswdd5q4CRvWZWyggv6nXRtVDiBZ')

    auth.set_access_token('1138909666321281031-M49ZNNPumNAnevcwzoifpWwKhdJzw1',
                      'HmKWJdynLp7rFZ6r65NSnWobjj2fWQ1I2GvoPaYxcMA2N')

    return auth
