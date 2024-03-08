# Playing with Words

Collection of combinatorial problems with words and text generation

## Setup

Pre-requisites

- Python > 3.7
- pipenv

Install dependencies using:

```
pipenv install --dev
```

## Running test suite

Tests are run with pytest withing the pipenv environment. A simple shortcut:

```
./test.sh
```

## Problem: Band Name in Lyrics

Provided a name of a band and the lyrics from one of their songs, return a portion of the lyrics so that the name of the band can be read vertically.

For example:

*   Band name: Sun
*   Lyrics: "...plays under the moon..."

Should return something like:

```
plays
    under the
 moon
```

The idea is that the letters "s", "u" and "n" from the band name can be read vertically when the words position themselves in such a manner.

This could also be another possible combination:

```
   plays
       under
the moon
```

A more comprehensive example using the band _Metallica_ and the lyrics from "Disposable Heroes":

```
Barking of machine gun fire, does nothing to me now
Sounding of the clock that ticks, get used to it somehow
More a man, more stripes you bare, glory seeker trends
Bodies fill the fields I see
The slaughter never ends

Soldier boy, made of clay
Now an empty shell
Twenty one, only son
But he served us well
Bred to kill, not to care
Do just as we say
Finished here, greetings death
He's yours to take away

Back to the front
You will do what I say, when I say
Back to the front
You will die when I say, you must die
Back to the front
You coward
You servant
You blind man
```

Should produce something like:

```
   machine gun
fire, does
 nothing to me now Sounding of the clock
 that ticks, get used to it somehow More a man, more stripes you bare,
  glory seeker trends Bodies
 fill the
  fields I see The slaughter never ends Soldier boy, made of
   clay Now
   an
```

Where the word "metallica" can be read from the 4th column of characters.

If no such combination exists, should return nothing.
