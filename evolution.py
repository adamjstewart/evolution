#!/usr/bin/env python

# Hello World program written using evolutionary computation

# Requires Python 2.7+ and NumPy

import numpy
import random
import string
import sys
import time


POP_SIZE = 1000
END_GOAL = list('Hello World!')
RATE_OF_INSERTION    = 0.1
RATE_OF_DELETION     = 0.1
RATE_OF_SUBSTITUTION = 0.1
RATE_OF_DUPLICATION  = 0.1


def mutate(sequence):
    '''Returns: a random mutation of sequence.

    Preconditions: sequence must be a list.'''

    assert(isinstance(sequence, list))

    sequence = insertion(sequence)
    sequence = deletion(sequence)
    sequence = substitution(sequence)
    sequence = duplication(sequence)

    return sequence


def insertion(sequence):
    '''Returns: sequence with random characters added.

    Preconditions: sequence must be a list.'''

    assert(isinstance(sequence, list))

    i = 0
    while i <= len(sequence):
        if random.random() < RATE_OF_INSERTION:
            newChar = random.choice(string.printable)
            sequence.insert(i, newChar)
            i += 1
        i += 1

    return sequence


def deletion(sequence):
    '''Returns: sequence with random characters removed.

    Preconditions: sequence must be a list.'''

    assert(isinstance(sequence, list))

    i = 0
    while i < len(sequence):
        if random.random() < RATE_OF_DELETION:
            sequence.pop(i)
        else:
            i += 1

    return sequence


def substitution(sequence):
    '''Returns: sequence with random characters either capitalized or lowercased.

    Preconditions: sequence must be a list.'''

    assert(isinstance(sequence, list))

    for i in range(len(sequence)):
        if random.random() < RATE_OF_SUBSTITUTION:
            if sequence[i].isupper():
                sequence[i] = sequence[i].lower()
            elif sequence[i].islower():
                sequence[i] = sequence[i].upper()

    return sequence


def duplication(sequence):
    '''Returns: sequence with random characters duplicated.

    Preconditions: sequence must be a list.'''

    assert(isinstance(sequence, list))

    i = 0
    while i < len(sequence):
        if random.random() < RATE_OF_DUPLICATION:
            sequence.insert(i, sequence[i])
            i += 1
        i += 1

    return sequence


def fitness(source, target):
    '''Returns: the evolutionary fitness of source.

    Calculates the Levenshtein Distance between source and target.

    Algorithm and implementation are modified from:
    http://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance

    Preconditions: source and target must be lists.'''

    assert(isinstance(source, list))
    assert(isinstance(target, list))

    if len(source) < len(target):
        return fitness(target, source)

    # Now len(source) >= len(target)
    if len(target) == 0:
        return len(source)

    # Cast lists to arrays
    source = numpy.asarray(source)
    target = numpy.asarray(target)

    # Use dynamic programming algorithm, but with the added optimization
    # that we only need the last two rows of the matrix.
    previousRow = numpy.arange(target.size + 1)
    for s in source:
        # Insertion (target grows longer than source):
        currentRow = previousRow + 1

        # Substitution or matching:
        # Target and source items are aligned, and either
        # are different (cost of 1), or are the same (cost of 0).
        currentRow[1:] = numpy.minimum(
                currentRow[1:],
                numpy.add(previousRow[:-1], target != s))

        # Deletion (target grows shorter than source):
        currentRow[1:] = numpy.minimum(
                currentRow[1:],
                currentRow[:-1] + 1)

        previousRow = currentRow

    return previousRow[-1]


if __name__ == '__main__':

    # Retrieve input string
    sequence = []
    if len(sys.argv) > 1:
        sequence = list(' '.join(sys.argv[1:]))

    # Warning: there is no guarantee that an evolutionary program will converge
    while sequence != END_GOAL:
        print('Score: {:2d}, String: {}'.format(fitness(sequence, END_GOAL), ''.join(sequence)))

        # Asexual reproduction
        generation = []
        for i in range(POP_SIZE):
            generation.append(sequence[:])

        generation = list(map(mutate, generation))

        # Find most fit
        for newSequence in generation:
            if fitness(newSequence, END_GOAL) <= fitness(sequence, END_GOAL):
                sequence = newSequence

    print('Score: {:2d}, String: {}'.format(fitness(sequence, END_GOAL), ''.join(sequence)))
