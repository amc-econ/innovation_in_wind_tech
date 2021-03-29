#!/usr/bin/env python

"""Tests for `innovation_in_wind_tech` package."""


import unittest
from click.testing import CliRunner

from innovation_in_wind_tech import innovation_in_wind_tech
from innovation_in_wind_tech import cli


class TestInnovation_in_wind_tech(unittest.TestCase):
    """Tests for `innovation_in_wind_tech` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'innovation_in_wind_tech.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
