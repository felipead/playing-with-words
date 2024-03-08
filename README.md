# Playing With Words

## Problem: Band Name

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

If no such combination exists, should return nothing.
