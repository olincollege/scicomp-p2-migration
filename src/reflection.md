# Kotlin Reflection

I have completed the Kotlin tour and would now like to reflect on my current experience with Kotlin

## What do I like about Kotlin
I would say the main things I like about Kotlin in particular is that the syntax wasn't the most difficult to pick up. I prefer languages that are statically typed rather than dynamically typed as there can be more considerations made about the actual performance of our code. The combination of static typing in addition to the ease of syntax is something I do like about Kotlin. The fact that it is also compiled is something I can also appreciate

## Are there things you were expecting to find that you haven’t?

I would actually say that there wasn't too much if anything at all that I haven't found that I was expecting. If there was a function meant for a specific purpose, then chances were that the function exists, or the function is simple enough to be implemented on your own.

## Questions

I'm mainly curious about the compiler for running code on the JVM. How does the compiler ensure correctness, type safety, and what role does the Abstract Syntax Tree play in this phase of compilation?

# Translation of code from Python

## What I did

You'll notice that I created a seperate branch in this GitHub repo. The purpose of this project was to calculate concentrations of water and carbon dioxide migrating across the surface of Mercury. The code involved alot of kinematic calculations, so for my port of Kotlin, I decided to translate two functions. The first determines the temperature of a molecule which is dependent on the latitude that the molecule is at due to the position of the sun. The second function takes an input temperature as well as the type of molecule and provides an output velocity. The original functions in Python can be seen as the first two functions in the `helpers.py` file. I decided to do unit testing at different types of latitude levels and different expressions for the type of molecule. Here are my thoughts

### The Good

In general, translating the code was really simple for me to do. My code was very mathematically based, so I utilized the math library that Kotlin had. Through looking at the documentation, I was able to find every necessary function needed to redfine the code for calculating the velocity of a particle. One thing I can also appreciate (More about Jetbrains) is that it does help a bit with the stylistic elements of code that I sometimes overlook.

### The Bad

I wasn't quite able to get my unit tests working in the way that I would've liked it to by utilizing the classes and placing my unit tests in an alternative directory. I don't think I've quite figured out how to utilize the tests JUnit, so this is something that I would like to play around with a bit more.

### The Ugly

I honestly don't think there is anything I majorly disliked about my translation experience. I feel that I will need to take a bit of time to adjust to learning Kotlin a bit more and getting more adjusted to it, but I feel relatively comfortable with it for now.