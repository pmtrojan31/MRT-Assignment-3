from setuptools import find_packages, setup
from glob import glob

package_name = 'my_diff_drive'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pranav',
    maintainer_email='24b1286@iitb.ac.in',
    description='TODO: Package description',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ["velocity_publisher = my_diff_drive.velocity_publisher:main"
        ],
    },
)
