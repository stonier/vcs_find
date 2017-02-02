#
# License: BSD
#    https://raw.githubusercontent.com/stonier/vcs_extras/devel/LICENSE
#
##############################################################################
# Documentation
##############################################################################

"""
Arg parse construction.
"""
##############################################################################
# Imports
##############################################################################

import argparse
import vcs_extras
import vcs_extras.console as console

from . import find
from . import config
from . import index_contents

##############################################################################
# Methods
##############################################################################


def version_string():
    return console.cyan + "Version" + console.reset + " : " + console.yellow + vcs_extras.__version__ + console.reset


def get_parser():
    # Create a top level parser
    parser = argparse.ArgumentParser(
        description="version control index handling",
        epilog="And his noodly appendage reached forth to tickle the blessed...\n",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-v', '--version', action='version', version=version_string())
    subparsers = parser.add_subparsers(title='commands',
                                       help='valid commands for vci interactions')
    find.add_subparser(subparsers)
    config.add_subparser(subparsers)
    index_contents.add_subparser(subparsers)
    return parser
