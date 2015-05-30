#!/usr/bin/env python3
import subprocess
import os


class PyCont:

    ''' path - path to container directory or path to empty dir
    '''

    def __init__(self, path, mount=True):
        self.path = path
        if mount:
            result_mount_proc = self._mount(
                'mount', 'proc', self.path + '/proc')
            result_mount_sys = self._mount(
                'mount', 'sysfs', self.path + '/sys')

    def get(self, title='wheezy', url='http://http.debian.net/debian/'):
        """ Get linux image with debootstrap
            https://wiki.debian.org/Debootstrap
            For execute this need sudo permission
            TODO: configuration of the system
            Note: Not ready
        """
        if not os.path.exists(self.path):
            os.mkdir(self.path)

        subprocess.call(['debootstrap', title, self.path, url])

    def _mount(self, command, title, path):
        """ Mount before starting """
        subprocess.Popen(
            [command, title, '{0}'.format(path), '-t', title], stderr=subprocess.STDOUT)

    def umount(self):
        ' umount mounted all mounted parts [/proc, /sys]'
        subprocess.Popen(
            ['umount', self.path + '/proc'], stderr=subprocess.STDOUT)
        subprocess.Popen(
            ['umount', self.path + '/sys'], stderr=subprocess.STDOUT)

    def _exec(self, command, arguments):
        basic = ['chroot', self.path, command]
        if arguments != None:
            basic.extend(arguments)
        subprocess.call(basic)

    def execute(self, command, *args, **kwargs):
        ''' execute command from container
            command - /bin/bash or /bin/ls, for example
            arg - arguments to command execute('/bin/ls', arg=['-la'])
        '''
        arguments = kwargs.get('arg', [])
        self._exec(command, arguments=arguments)
