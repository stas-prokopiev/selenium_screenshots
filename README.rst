====================
selenium_screenshots
====================


.. image:: https://img.shields.io/github/last-commit/stas-prokopiev/selenium_screenshots
   :target: https://img.shields.io/github/last-commit/stas-prokopiev/selenium_screenshots
   :alt: GitHub last commit

.. image:: https://img.shields.io/github/license/stas-prokopiev/selenium_screenshots
    :target: https://github.com/stas-prokopiev/selenium_screenshots/blob/master/LICENSE.txt
    :alt: GitHub license<space><space>

.. image:: https://readthedocs.org/projects/selenium_screenshots/badge/?version=latest
    :target: https://selenium_screenshots.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://travis-ci.org/stas-prokopiev/selenium_screenshots.svg?branch=master
    :target: https://travis-ci.org/stas-prokopiev/selenium_screenshots

.. image:: https://img.shields.io/pypi/v/selenium_screenshots
   :target: https://img.shields.io/pypi/v/selenium_screenshots
   :alt: PyPI

.. image:: https://img.shields.io/pypi/pyversions/selenium_screenshots
   :target: https://img.shields.io/pypi/pyversions/selenium_screenshots
   :alt: PyPI - Python Version


.. contents:: **Table of Contents**

Short Overview.
=========================
selenium_screenshots is a python package that helps in creating many screenshots for selenium webdrivers.

Example
------------------------------

.. code-block:: python

    from selenium import webdriver
    from selenium_screenshots.main import Screenshots
    # Please define here any webdriver you would like to use
    # E.G. driver = webdriver.Chrome()
    screenshots_handler = Screenshots(driver)
    # When you would want to create a screenshot, just call method
    # As the result you will get a screenshot in the directory: ./screenshots/
    screenshots_handler.create_screenshot()

Installation via pip:
======================

.. code-block:: bash

    pip install selenium_screenshots

Usage examples
=========================

Arguments of the class object initializer: **Screenshots**
--------------------------------------------------------------------------------------------------



Links
=====

    * `PYPI <https://pypi.org/project/selenium_screenshots/>`_
    * `readthedocs <https://selenium_screenshots.readthedocs.io/en/latest/>`_
    * `GitHub <https://github.com/stas-prokopiev/selenium_screenshots>`_

Project local Links
===================

    * `CHANGELOG <https://github.com/stas-prokopiev/selenium_screenshots/blob/master/CHANGELOG.rst>`_.
    * `CONTRIBUTING <https://github.com/stas-prokopiev/selenium_screenshots/blob/master/CONTRIBUTING.rst>`_.

Contacts
========

    * Email: stas.prokopiev@gmail.com
    * `vk.com <https://vk.com/stas.prokopyev>`_
    * `Facebook <https://www.facebook.com/profile.php?id=100009380530321>`_

License
=======

This project is licensed under the MIT License.

