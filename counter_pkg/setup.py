from setuptools import find_packages, setup

package_name = 'counter_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='root@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
    'console_scripts': [
        'counter_publisher = counter_pkg.counter_publisher:main',
        'counter_subscriber = counter_pkg.counter_subscriber:main',
        'robot_status_publisher = counter_pkg.robot_status_publisher:main',
        'robot_status_subscriber = counter_pkg.robot_status_subscriber:main',
        'robot_status_subscriberA = counter_pkg.robot_status_subscriberA:main',
        'robot_status_subscriberB = counter_pkg.robot_status_subscriberB:main',

    ],
},
)
