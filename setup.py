#!/usr/bin/env python3
"""
Setup script for Advanced Online Exam System with AI Proctoring
"""

from setuptools import setup, find_packages
import os

# Read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Read requirements from requirements.txt
with open(os.path.join(this_directory, 'requirements.txt'), encoding='utf-8') as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name="advanced-exam-system",
    version="1.0.0",
    author="Development Team",
    author_email="dev@examsystem.com",
    description="Advanced Online Exam System with AI-Powered Proctoring",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourorg/advanced-exam-system",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Topic :: Education :: Testing",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Framework :: Flask",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.4.2",
            "pytest-cov>=4.1.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
        ],
        "prod": [
            "gunicorn>=21.2.0",
            "redis>=4.5.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "exam-system=run:main",
        ],
    },
    include_package_data=True,
    package_data={
        "app": [
            "templates/**/*.html",
            "static/**/*",
            "static/models/**/*",
        ],
    },
    keywords="exam system proctoring ai education flask mongodb",
    project_urls={
        "Documentation": "https://github.com/yourorg/advanced-exam-system/wiki",
        "Bug Reports": "https://github.com/yourorg/advanced-exam-system/issues",
        "Source": "https://github.com/yourorg/advanced-exam-system",
    },
) 