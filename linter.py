"""This module exports the puppet-lint util."""

from cuda_lint import Linter, util

class PuppetLint(Linter):

    """Provides an interface to puppet-lint"""
    cmd = None
    executable = 'puppet-lint'
    multiline = False
    syntax = ('Puppet')
    regex = (
             r'^(?P<line>\d+):(?P<col>\d+):'
             r'((?P<warning>warning)|(?P<error>error)):'
             r'(?P<message>.+)'
            )
    base_cmd = ('--log-format '
                '%{line}:%{column}:%{kind}:%{message} '
                '*')
    tempfile_suffix = 'rb'
    error_stream = util.STREAM_STDOUT
    word_re = r'^(".*?"|[-\w]+)'


    def split_match(self, match):
        print('plit_match')
        print(match)
   
        """Return the components of the error."""
        split_match = super(PuppetLint, self).split_match(match)

        match, line, col, error, warning, message, near = split_match
        return match, line, 0, '', '', message, ''
        


    def cmd(self):
        print('cmd')
        """Return the command line to execute."""
        result = self.executable + ' ' + self.base_cmd

        return result
