import argparse
from moeap.profiles import profiles


def list_command(args):
    """List EAPClientProfiles Command."""
    p = profiles()
    print(p)


def show_command(args):
    """Show EAPClientProfile Command."""

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

    args = parser.parse_args()
    args.func(args)

