Assignment: Great Number Game
Create a site that when a user loads it creates a random number between 1-100 and stores the number in session. Allow the user to guess at the number and tell them when they are too high or too low. If they guess the correct number tell them and offer to play again.

In order to generate a random number you can use the "random" python module:

import random # import the random module
# The random module has many useful functions. This is one that gives a random number in a range
random.randrange(0, 101) # random number between 0-100
In order to remove something from the session, you must "pop" it off of the session dictionary.

# Set session like so:
session['someKey'] = 50
# Remove something from session like so:
session.pop('someKey')

![alt tag](https://user-images.githubusercontent.com/32435667/37870476-47e8553e-2fa5-11e8-80e5-0b62bd32da18.png)
![alt tag](https://user-images.githubusercontent.com/32435667/37870491-89040a5e-2fa5-11e8-9206-55f8637c0421.png)
![alt tag](https://user-images.githubusercontent.com/32435667/37870498-a4bdc85c-2fa5-11e8-9992-3aa6ef350dce.png)

