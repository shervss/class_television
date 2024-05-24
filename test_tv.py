# Pseudocode

from tv_class import TV

def main():
    # Create two TV objects
    tv1 = TV()
    tv2 = TV()
    # Turn on the TVs
    tv1.turn_on()
    tv2.turn_on()
    # Set channels and volumes for tv1
    tv1.set_channel(30)
    tv1.set_volume(3)
    # Set channels and volumes for tv2
    tv2.set_channel(3)
    tv2.set_volume(2)
    # Print the results
    print(f"tv1's channel is {tv1.get_channel()} and volume level is {tv1.get_volume()}")
    print(f"tv2's channel is {tv2.get_channel()} and volume level is {tv2.get_volume()}")

main()