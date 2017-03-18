from moeap.eap8021x import EAPOLClientConfigurationCreate, EAPOLClientConfigurationCopyProfiles


def profiles():
    """Get a list of all defined EAPOLClient Configuration Profiles.

    This can be a mix of different profile types.

    Returns:
        list of EAPOLClientProfileRef
    """
    cfg = EAPOLClientConfigurationCreate(None)
    if cfg is None:
        raise ValueError('Expected config object')

    profiles = EAPOLClientConfigurationCopyProfiles(cfg)
    if profiles is None:
        return None

    return profiles
#
# def loginwindow_profiles(iface=None):
#     """Get a list of profiles configured for LoginWindow mode.
#
#     Args:
#           iface Name of the BSD interface to get a loginwindow profile for eg. 'en0'. If this is absent
#                 then all loginwindow profiles are returned.
#
#     """
#     EAPOLClientConfigurationCopyLoginWindowProfiles()
#
# def profile_for_ssid(ssid):
#     # EAPOLClientConfigurationGetProfileWithWLANSSID
#     return EAPOLClientWifiProfile()

#EAPOLClientConfigurationGetProfileWithWLANDomain

#EAPOLClientConfigurationRemoveProfile

# def create(user_defined_name=None, auth_props=None, ):
#     """Create a new EAPOLClientProfile"""
#     cfg = EAPOLClientConfigurationCreate(None)
#     if cfg is None:
#         raise ValueError('Expected config object')
#
#     p = EAPOLClientProfileCreate(cfg)
    

#
# class EAPOLClientProfile(object):
#     """This class is a wrapper for the EAP8021X EAPOLClientProfileRef struct."""
#
#     def __init__(self, ref=None, id=None):
#         # if id
#         # EAPOLClientConfigurationGetProfileWithID
#         self._ref = ref
#
#     @property
#     def id(self):
#         """Get the EAPOLClient Profile Identifier"""
#         # EAPOLClientProfileGetID
#         return 1
#
#     @property
#     def auth_props(self):
#         # EAPOLClientProfileGetAuthenticationProperties
#
#     @property
#     def name(self):
#         # EAPOLClientProfileGetUserDefinedName
#
#
#     def export(self):
#         # EAPOLClientProfileCreatePropertyList
#         # write plist
#
#     def save(self):
#         # EAPOLClientConfigurationSave
#
# class EAPOLClientWifiProfile(EAPOLClientProfile):
#     """Wrapper for EAP Profiles that specifically are tied to WLAN interfaces"""
#     @property
#     def ssid(self):
#     # EAPOLClientProfileGetWLANSSIDAndSecurityType
#
#     @property
#     def domain(self):
#         # EAPOLClientProfileGetWLANDomain