# Echo module

Simply module providing one primary command for `echo(**kwargs)`, which can be used for debugging and testing Dareplane setups.

## Example usecase

While implementing the `callback` functionality via the `control_room` module, I implemented triggering a callback via another module, passing it to the control_room, with specified destination `dp-echo`, which would then log that a function was indeed called in this `dp-echo` module.
