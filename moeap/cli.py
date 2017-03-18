import argparse
from Foundation import NSPropertyListSerialization, NSPropertyListXMLFormat_v1_0
from moeap.profiles import profiles, profile_with_uuid, profile_with_iface, assign_interface
from . import EAP_TYPE_DESCRIPTIONS

def list_command(args):
    """List EAPClientProfiles Command."""
    for p in profiles():
        ap = p.auth_props
        if 'AcceptEAPTypes' in ap:
            eap_descriptions = [EAP_TYPE_DESCRIPTIONS[accepted] for accepted in ap['AcceptEAPTypes']]
        else:
            eap_descriptions = []

        row = "UUID: {}\tName: {}\tEAP Types: {}".format(p.uuid, p.user_defined_name, ','.join(eap_descriptions))
        print(row)



def show_command(args):
    """Show EAPClientProfile Command."""
    if args.uuid:
        p = profile_with_uuid(args.uuid)
    elif args.iface:
        p = profile_with_iface(args.iface)
    else:
        return -1

    print("UUID:\t{}".format(p.uuid))
    print("User Defined Name:\t{}".format(p.user_defined_name))

    ap = p.auth_props
    if 'AcceptEAPTypes' in ap:
        eap_descriptions = [EAP_TYPE_DESCRIPTIONS[accepted] for accepted in ap['AcceptEAPTypes']]
    else:
        eap_descriptions = []
    print("Accepted EAP Types:\t{}".format(','.join(eap_descriptions)))

    mcx_info = p.information()
    if mcx_info is not None:
        print('Associated Configuration Profile Payload UUID:\t{}'.format(mcx_info.get('PayloadUUID', '(None)')))


def export_command(args):
    """Export EAPClientProfile Command."""
    if args.uuid:
        p = profile_with_uuid(args.uuid)
        plist_data = p.__plist__()
        d, err = NSPropertyListSerialization.dataWithPropertyList_format_options_error_(
            plist_data,
            NSPropertyListXMLFormat_v1_0,
            0,
            None,
        )

        print(d)


def associate_command(args):
    """Associate EAPClientProfile with BSD iface"""
    success = assign_interface(args.uuid, args.iface)
    if success:
        print('Successfully assigned profile {} to interface {}'.format(args.uuid, args.iface))
    else:
        print('Could not assign profile {} to interface {}'.format(args.uuid, args.iface))


def main():
    parser = argparse.ArgumentParser(description='moeap EAPOLClient Utility, modeled on eapolcfg')
    parser.add_argument('-v', '--verbose', action='store_true', help='verbose output')
    subparsers = parser.add_subparsers(title='subcommands', help='sub-command help')

    # list command
    parser_list = subparsers.add_parser('list', help='list help')
    parser_list.add_argument('--loginwindow', help='show only loginwindow EAPClientProfiles', action='store_true')
    parser_list.add_argument('--system', help='show only system EAPClientProfiles', action='store_true')
    parser_list.set_defaults(func=list_command)

    # show command
    parser_show = subparsers.add_parser('show', help='show help')
    parser_show.add_argument('--uuid', help='show EAPClientProfile with this UUID')
    parser_show.add_argument('--ssid', help='show EAPClientProfile associated with this WiFi SSID')
    parser_show.add_argument('--wlandomain', help='show EAPClientProfile associated with this WLAN domain')
    parser_show.add_argument('--iface', help='show EAPClientProfile associated with this BSD interface',
                             choices=['en0', 'en1', 'en2'])
    parser_show.set_defaults(func=show_command)

    # export command
    parser_export = subparsers.add_parser('export', help='export help')
    parser_export.add_argument('--uuid', help='Export EAPClientProfile with this UUID')
    parser_export.set_defaults(func=export_command)

    # associate command
    parser_associate = subparsers.add_parser('associate', help='associate help')
    parser_associate.add_argument('--loginwindow', help='associate as a loginwindow profile', action='store_true')
    parser_associate.add_argument('uuid', help='EAPClientProfile UUID')
    parser_associate.add_argument('iface', help='BSD Interface')
    parser_associate.set_defaults(func=associate_command)

    args = parser.parse_args()
    args.func(args)

