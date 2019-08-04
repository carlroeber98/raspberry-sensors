import time
from ircodec.command import CommandSet

controller = CommandSet(name='TEAC-REMOTE', emitter_gpio=14, receiver_gpio=15)

# Add keys
print("NEXT KEY: power")
controller.add('power')
time.sleep(1)
print("NEXT KEY: mute")
controller.add('mute')
time.sleep(1)
print("NEXT KEY: volume_down")
controller.add('volume_down')
time.sleep(1)
print("NEXT KEY: volume_up")
controller.add('volume_up')
time.sleep(1)
print("NEXT KEY: test_tone")
controller.add('test_tone')
time.sleep(1)
print("NEXT KEY: tape")
controller.add('tape')
time.sleep(1)
print("NEXT KEY: aux")
controller.add('aux')
time.sleep(1)
print("NEXT KEY: md-cdr")
controller.add('md-cdr')
time.sleep(1)


# Save to JSON
controller.save_as('teac.json')
