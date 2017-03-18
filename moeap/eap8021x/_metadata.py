"""
Hand crafted EAP8021X Metadata, with love
"""
import objc

# objc.createStructType('CE_SemanticsInformation', b'{__CE_SemanticsInformation=^{cssm_data=Q^C}^{__CE_GeneralNames=I^{__CE_GeneralName=Ii{cssm_data=Q^C}}}}', ['semanticsIdentifier', 'nameRegistrationAuthorities'])

misc = {}
# misc = {
#     'EAPOLClientConfiguration': objc.createStructType(
#         'EAPOLClientConfiguration',
#         b'{__EAPOLClientConfiguration={CFRuntimeBase=}^{AuthorizationExternalForm=}^{SCPreferencesRef=}^{SCPreferencesRef=}{CFMutableArrayRef}{CFMutableDictionaryRef}{CFMutableDictionaryRef}{CFMutableDictionaryRef}{CFDictionaryRef}Z',
#         ['cf_base', 'auth_ext_p', 'eap_prefs', 'sc_prefs', 'sc_changed_if', 'profiles', 'ssids', 'domains',
#          'def_auth_props', 'def_auth_props_changed']
#     ),
# }

misc.update({
    # EAPClientProperties.h

    # Properties applicable to most protocols
    'kEAPClientPropUserName': b'UserName',
    'kEAPClientPropUserPassword': b'UserPassword',
    'kEAPClientPropUserPasswordKeychainItemID': b'UserPasswordKeychainItemID',
    'kEAPClientPropAcceptEAPTypes': b'AcceptEAPTypes',
    'kEAPClientPropInnerAcceptEAPTypes': b'InnerAcceptEAPTypes',

    # TLS-based auth

    # EAP.h
    # EAPType enumeration

})

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
    'EAPOLClientProfileGetID': ('@^{OpaqueEAPOLClientProfileRef=}',),
    'EAPOLClientProfileGetAuthenticationProperties': ('@^{OpaqueEAPOLClientProfileRef=}',),
    'EAPOLClientProfileGetUserDefinedName': ('@^{OpaqueEAPOLClientProfileRef=}',),
    'EAPOLClientProfileCreatePropertyList': ('@^{OpaqueEAPOLClientProfileRef=}',),
    'EAPOLClientConfigurationGetProfileWithID': ('^{OpaqueEAPOLClientProfileRef=}^{OpaqueEAPOLClientConfigurationRef=}@',),
    'EAPOLClientProfileGetInformation': ('@^{OpaqueEAPOLClientProfileRef=}@',),
    'EAPOLClientConfigurationGetSystemProfile': ('^{OpaqueEAPOLClientProfileRef=}^{OpaqueEAPOLClientConfigurationRef=}@',),
    'EAPOLClientConfigurationSetSystemProfile': ('Z^{OpaqueEAPOLClientConfigurationRef=}@^{OpaqueEAPOLClientProfileRef=}',),
}
