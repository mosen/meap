"""
Hand crafted EAP8021X Metadata, with love
"""


cftypes = [
    ('EAPOLClientConfigurationRef', b'^{OpaqueEAPOLClientConfigurationRef=}', 'EAPOLClientConfigurationGetTypeID', None),
    ('EAPOLClientProfileRef', b'^{OpaqueEAPOLClientProfileRef=}', 'EAPOLClientProfileGetTypeID', None),
    ('EAPOLClientItemIDRef', b'^{OpaqueEAPOLClientItemIDRef=}', 'EAPOLClientItemIDGetTypeID', None),
]

functions = {
    'EAPOLClientConfigurationGetTypeID': (b'Q',),
    'EAPOLClientProfileGetTypeID': (b'Q',),
    'EAPOLClientItemIDGetTypeID': (b'Q',),
    'EAPOLClientConfigurationCreate': ('^{OpaqueEAPOLClientConfigurationRef=}^{__CFAllocator=}',),
    'EAPOLClientConfigurationCopyProfiles': ('^{__CFArray=}^{OpaqueEAPOLClientConfigurationRef=}',),
}
