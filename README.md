# evolution
:seedling: A repository of evolutionary programming scripts

At the moment I only have one script in this repository, `evolution.py`. This script is basically a "Hello World!" program designed to demonstrate the capabilities of an evolutionary programming script.

Any good evolutionary system must satisfy Darwin's tenets of Natural Selection:

1. Individuals within a population are variable
2. These variations are heritable from one generation to the next
3. More individuals are born than will survive to reproduce
4. The individuals with the most favorable variations are naturally selected

If these 4 tenets are met, Darwin reasoned that evolution of a population would occur.

## Population

For our purposes, we define a population of strings. Initially, these strings are all identical, and are initialized to the value given to the `evolution.py` script, or the empty string if no arguments are provided.

## Mutation

A population could not evolve without mutation, and the `mutate()` function is designed to do just that. It calls various subfunctions to introduce mutation through insertion, deletion, substitution, and duplication.

## Reproduction

During every generation, each individual has a chance of undergoing a mutation. These mutations are heritable, as the next generation is based on the characters of the first.

## Selection

In order to create a selective pressure, we define a `fitness()` function, which dictates the evolutionary fitness of a particular individual. Fitness is defined as similarity to the ideal string, in this case "Hello World!", and is calculated using the [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance). After being sorted by Levenshtein distance, the single most fit individual is preserved and the rest of the herd is culled. This new individual becomes the start of the next generation and is copied and mutated to a full population.

## Result

The result of these conditions is that over time, each generation gets successively closer to the end goal, printing the string "Hello World!".

```
$ ./evolution.py goodybe universe
Score: 15, String: goodybe universe
Score: 11, String: oybe unvere
Score: 10, String: oye  Ere
Score:  9, String: ye@    Ere:
Score:  8, String: ye    Eorre:
Score:  8, String: ye@@  Eorre:
Score:  8, String: ye@@  eor:
Score:  7, String: yeh@@  or:d
...
Score:  1, String: Hello orld!
Score:  1, String: Helllo World!
Score:  0, String: Hello World!
```
