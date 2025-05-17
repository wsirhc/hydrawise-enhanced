from .set_valve import set_valve_state

"""Hydrawise Enhanced custom component for Home Assistant."""

DOMAIN = "hydrawise_enhanced"


async def async_setup(hass, config):
    """Set up the Hydrawise Enhanced component."""
    # Initialization code here
    return True

async def async_set_valve(hass, username, password, valve_id, state):
    """Set the state of a valve using set_valve.py."""
    result = await hass.async_add_executor_job(
        set_valve_state, username, password, valve_id, state
    )
    return result