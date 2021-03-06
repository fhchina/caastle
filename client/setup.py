#!/usr/bin/env python

PROJECT = 'cld'

VERSION = '0.0.1'

from setuptools import setup, find_packages

try:
    long_description = open('README.rst', 'rt').read()
except IOError:
    long_description = ''

setup(
    name=PROJECT,
    version=VERSION,

    description='CloudARK command-line tool',
    long_description=long_description,

    author='Devdatta Kulkarni',
    author_email='kulkarni.devdatta@gmail.com',

    url='',
    download_url='',

    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: Apache Software License',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Intended Audience :: Developers',
                 'Environment :: Console',
                 ],

    platforms=['Any'],

    scripts=[],

    provides=[],
    install_requires=['cliff'],

    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'cld = fmcmds.main:main'
        ],
        'cld.cmds': [
            'container create = fmcmds.container_create:ContainerCreate',
            'container delete = fmcmds.container_delete:ContainerDelete',
            'container show = fmcmds.container_show:ContainerShow',
            'container list = fmcmds.container_list:ContainerList',
            'app delete = fmcmds.app_delete:AppDelete',
            'app deploy = fmcmds.app_deploy:AppDeploy',
            #'app redeploy = fmcmds.app_redeploy:AppRedeploy',
            'app list = fmcmds.app_list:AppList',
            'app show = fmcmds.app_show:AppShow',
            'app logs = fmcmds.app_logs:AppLogs',
            'resource show = fmcmds.resource_show:ResourceShow',
            'resource list = fmcmds.resource_list:ResourceList',
            'env create = fmcmds.environment_create:EnvironmentCreate',
            'env delete = fmcmds.environment_delete:EnvironmentDelete',
            'env show = fmcmds.environment_show:EnvironmentShow',
            'env list = fmcmds.environment_list:EnvironmentList',
            'env exec = fmcmds.env_exec:EnvironmentExec',
            'env shell = fmcmds.env_shell:EnvironmentShell',
            'setup aws = fmcmds.setup_aws:AWSSetup',
            'setup gcloud = fmcmds.setup_gcloud:GCloudSetup',
        ],
    },

    zip_safe=False,
)
