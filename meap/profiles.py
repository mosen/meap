from meap.eap8021x import EAPOLClientConfigurationCreate, EAPOLClientConfigurationCopyProfiles, \
    EAPOLClientProfileGetID, EAPOLClientProfileGetAuthenticationProperties, EAPOLClientProfileGetUserDefinedName, \
    EAPOLClientProfileCreatePropertyList, EAPOLClientConfigurationGetProfileWithID, EAPOLClientProfileGetInformation, \
    EAPOLClientConfigurationGetSystemProfile, EAPOLClientConfigurationSetSystemProfile, \
    EAPOLClientConfigurationCopyLoginWindowProfiles


def profile_with_uuid(uuid):
    """Get an EAPOLClient Profile by its UUID

    Raises:
        ValueError if EAPOL configuration cannot be accessed.

    Returns:
        EAPOLClientProfile instance or None if not found
    """
    cfg = EAPOLClientConfigurationCreate(None)
    if cfg is None:
        raise ValueError('Expected config object')

    ref = EAPOLClientConfigurationGetProfileWithID(cfg, uuid)
    if ref is None:
        return ref

    return EAPOLClientProfile(ref)


def profile_with_iface(iface):
    """Get the EAPOLClient System Profile associated with the specified BSD interface name."""
    cfg = EAPOLClientConfigurationCreate(None)
    if cfg is None:
        raise ValueError('Expected config object')

    ref = EAPOLClientConfigurationGetSystemProfile(cfg, iface)
    if ref is None:
        return ref

    return EAPOLClientProfile(ref)


def assign_interface(profile_uuid, if_name='en0', loginwindow=False):
    """Assign this profile with an interface."""
    cfg = EAPOLClientConfigurationCreate(None)
    if cfg is None:
        raise ValueError('Expected config object')

    p = profile_with_uuid(profile_uuid)
    if p is None:
        raise ValueError('Cannot find profile with that UUID')

    if not loginwindow:
        success = EAPOLClientConfigurationSetSystemProfile(
            cfg,
            if_name,
            p,
        )

        return success

    return False


#

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

    return [EAPOLClientProfile(ref=ref) for ref in profiles]

def loginwindow_profiles(iface):
    """Get a list of profiles configured for LoginWindow mode.

    Args:
          iface Name of the BSD interface to get a loginwindow profile for eg. 'en0'. If this is absent
                then all loginwindow profiles are returned.

    """
    cfg = EAPOLClientConfigurationCreate(None)
    if cfg is None:
        raise ValueError('Expected config object')

    profiles = EAPOLClientConfigurationCopyLoginWindowProfiles(cfg, iface)
    if profiles is None:
        return None

    return [EAPOLClientProfile(ref=ref) for ref in profiles]
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
    


class EAPOLClientProfile(object):
    """This class is a wrapper for the EAP8021X EAPOLClientProfileRef struct."""

    def __init__(self, ref):
        self._ref = ref

    def __plist__(self):
        """Get this EAPOLClient Profile in a serialized property list format.

        Returns:
            An instance of CFPropertyList which you can serialize to either binary or xml plist format.
        """
        return EAPOLClientProfileCreatePropertyList(self._ref)


    @property
    def uuid(self):
        """Get the EAPOLClient Profile Identifier

        Returns:
            The UUID of the EAPOLClient profile
        """
        return EAPOLClientProfileGetID(self._ref)

    @property
    def auth_props(self):
        """Get the EAP client authentication properties for the profile.

        Returns:
            A dict which can contain different keys depending on which EAP type has been selected.
        """
        return EAPOLClientProfileGetAuthenticationProperties(self._ref)

    @property
    def user_defined_name(self):
        return EAPOLClientProfileGetUserDefinedName(self._ref)

    def information(self, application_id='com.apple.mcx.configurationprofiles.8021X'):
        """Get the associated information for the profile.

        Any application can store information with the EAP profile but we are mostly interested in the Configuration
        Profile which has an application id of ``com.apple.mcx.configurationprofiles.8021X``.

        The configuration profile dict contains a key of ``PayloadUUID`` which refers to the original payload that
        generated the EAP configuration.

        Returns:
            A dict which can contain any extra information.
        """
        return EAPOLClientProfileGetInformation(self._ref, application_id)


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