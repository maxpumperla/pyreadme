#!/usr/bin python
# -*- coding: utf-8 -*-
################################################################################
# Copyright (c) 2015-2018 Skymind, Inc.
#
# This program and the accompanying materials are made available under the
# terms of the Apache License, Version 2.0 which is available at
# https://www.apache.org/licenses/LICENSE-2.0.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# SPDX-License-Identifier: Apache-2.0
################################################################################

import argparse
import json
import os
import sys
import pkg_resources
import argcomplete
import traceback
import subprocess
import click
from click.exceptions import ClickException
from dateutil import parser


if sys.version_info[0] == 2:
    input = raw_input


def to_bool(string):
    if type(string) is bool:
        return string
    return True if string[0] in ["Y", "y"] else False


class CLI(object):

    def __init__(self):
        self.var_args = None
        self.command = None

    def command_dispatcher(self, args=None):
        desc = ('pyreadme,  is an interface for the readme.io HTTP API.\n')
        parser = argparse.ArgumentParser(description=desc)
        parser.add_argument(
            '-v', '--version', action='version',
            version=pkg_resources.get_distribution("pydl4j").version,
            help='Print pyreadme version'
        )

        subparsers = parser.add_subparsers(title='subcommands', dest='command')
        subparsers.add_parser('init', help='Initialize pyreadme')

        argcomplete.autocomplete(parser)
        args = parser.parse_args(args)
        self.var_args = vars(args)

        if not args.command:
            parser.print_help()
            return

        self.command = args.command

        if self.command == 'init':
            self.init()
            return


    def init(self):

        click.echo(click.style(u"""\n██████╗ ██╗   ██╗██████╗ ███████╗ █████╗ ██████╗ ███╗   ███╗███████╗
██╔══██╗╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗██╔══██╗████╗ ████║██╔════╝
██████╔╝ ╚████╔╝ ██████╔╝█████╗  ███████║██║  ██║██╔████╔██║█████╗  
██╔═══╝   ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██║██║  ██║██║╚██╔╝██║██╔══╝  
██║        ██║   ██║  ██║███████╗██║  ██║██████╔╝██║ ╚═╝ ██║███████╗
╚═╝        ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚══════╝\n""", fg='blue', bold=True))

        click.echo(click.style("pyreadme", bold=True) +
                   " is an interface for the readme.io HTTP API!\n")


def handle():
    try:
        cli = CLI()
        sys.exit(cli.command_dispatcher())
    except KeyboardInterrupt:
        sys.exit()
    except Exception as e:
        click.echo(click.style("Error: ", fg='red', bold=True))
        traceback.print_exc()
        sys.exit()


if __name__ == '__main__':
    handle()
