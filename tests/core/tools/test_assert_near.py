
import numpy as np

from openfisca_core.tools import assert_near


def test_enum(tax_benefit_system):
    possible_values = tax_benefit_system.variables['housing_occupancy_status'].possible_values
    value = possible_values.encode(np.array(['tenant']))
    expected_value = 'tenant'
    assert_near(value, expected_value)


def test_enum_2(tax_benefit_system):
    possible_values = tax_benefit_system.variables['housing_occupancy_status'].possible_values
    value = possible_values.encode(np.array(['tenant', 'owner']))
    expected_value = ['tenant', 'owner']
    assert_near(value, expected_value)
