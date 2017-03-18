from moeap.eap8021x import EAPOLClientConfigurationCreate, EAPOLClientConfigurationCopyProfiles


def list_profiles():
    """Get a list of EAPOLClient Configuration Profiles.

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


class EAPOLClientProfile(object):
    """This class is a wrapper for the EAP8021X EAPOLClientProfileRef struct."""

    def __init__(self, ref):
        self._ref = ref

