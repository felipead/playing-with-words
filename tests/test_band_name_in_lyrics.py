from words.band_name_in_lyrics import display_vertically


def test_band_name_in_lyrics_display_vertically_exact_fit():
    name = 'Sun'
    lyrics = 'plays under the moon'

    output = display_vertically(name, lyrics)

    expected = '''\
plays
    under the
 moon\
'''

    assert output == expected


def test_band_name_in_lyrics_display_vertically_surrounded_with_words():
    name = 'Sun'
    lyrics = 'foo bar ... plays under the moon ... foo bar'

    output = display_vertically(name, lyrics)

    expected = '''\
plays
    under the
 moon\
'''

    assert output == expected


def test_band_name_in_lyrics_display_vertically_case_insensitive():
    name = 'Sun'
    lyrics = 'foo bar ... plays Under the MOON ... foo bar'

    output = display_vertically(name, lyrics)

    expected = '''\
plays
    Under the
 MOON\
'''

    assert output == expected


def test_band_name_in_lyrics_display_vertically_extra_white_space():
    name = 'Sun'
    lyrics = 'foo bar  ... plays under    the\n  moon  ... foo  bar'

    output = display_vertically(name, lyrics)

    expected = '''\
plays
    under the
 moon\
'''

    assert output == expected


def test_band_name_in_lyrics_display_vertically_when_the_name_has_repeated_words():
    name = 'Sunn'
    lyrics = 'foo bar  ... plays under    the\n  moon but navigates the sea ... foo  bar'

    output = display_vertically(name, lyrics)

    expected = '''\
plays
    under the
 moon but
    navigates\
'''

    assert output == expected


def test_band_name_in_lyrics_display_vertically_sample_2():
    name = 'Metallica'
    lyrics = '''\
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
'''
    output = display_vertically(name, lyrics)

    expected = '''\
   machine gun
fire, does
 nothing to me now Sounding of the clock
 that ticks, get used to it somehow More a man, more stripes you bare,
  glory seeker trends Bodies
 fill the
  fields I see The slaughter never ends Soldier boy, made of
   clay Now
   an\
'''

    assert output == expected


def test_band_name_in_lyrics_display_vertically_sample_3():
    name = 'Everything'
    lyrics = '''\
I step off the train
I'm walking down your street again
And past your door
But you don't live there anymore
It's years since you've been there
Now you've disappeared somewhere
Like outer space
You've found some better place
And I miss you
Like the deserts miss the rain
Could you be dead?
You always were two steps ahead
Of everyone
We'd walk behind while you would run
I look up at your house
And I can almost hear you shout
Down to me
Where I always used to be
And I miss you -
Like the deserts miss the rain
Back on the train
I ask why did I come again
Can I confess
I've been hanging around your old address?
And the years have proved
To offer nothing since you moved
You're long gone
But I can't move on
And I miss you
Like the deserts miss the rain
I step off the train
I'm walking down your street again
And past your door
I guess you don't live there anymore
It's years since you've been there
Now you've disappeared somewhere
Like outer space
You've found some better place
And I miss you
Like the deserts miss the rain
And I miss you
Like the deserts miss the rain
(Deserts miss the rain)
'''

    output = display_vertically(name, lyrics)

    expected = '''\
   step off the train I'm walking down your street again And past your door But you don't
   live
   there
anymore It's
     years since you've been
     there Now you've disappeared
somewhere
    Like outer space You've
  found some better place And I miss you Like the deserts miss the rain Could you be dead? You always were two steps ahead Of everyone We'd walk behind while you would run I look up at your house And I can almost hear you shout Down to me Where I always used to be And I miss you - Like the deserts miss the rain Back on the train I ask why did I come
    again\
'''

    assert output == expected


def test_band_name_in_lyrics_display_vertically_not_found_lyrics_too_short_1():
    name = 'Sun'
    lyrics = 'plays the moon'

    output = display_vertically(name, lyrics)

    assert output is None


def test_band_name_in_lyrics_display_vertically_not_found_lyrics_too_short_2():
    name = 'Sun'
    lyrics = 'under the moon'

    output = display_vertically(name, lyrics)

    assert output is None


def test_band_name_in_lyrics_display_vertically_not_found_lyrics_too_short_3():
    name = 'Sun'
    lyrics = 'plays under'

    output = display_vertically(name, lyrics)

    assert output is None


def test_band_name_in_lyrics_display_vertically_not_found_1():
    name = 'Cobra'
    lyrics = 'my old man told me this story about a witch and a rat'

    output = display_vertically(name, lyrics)

    assert output is None


def test_band_name_in_lyrics_display_vertically_not_found_2():
    name = 'ABBA'
    lyrics = '... the quick brown fox jumps over the lazy dog ...'

    output = display_vertically(name, lyrics)

    assert output is None


def test_band_name_in_lyrics_display_vertically_not_found_3():
    name = 'Metallica'
    lyrics = '''\
Barking of machinegun fire,
does nothing to me now Sounding of the clock that ticks,
get used to it somehow More a man, more stripes you wear,
glory seeker trends,
Bodies fill the fields I see, the slaughter never ends\
'''

    output = display_vertically(name, lyrics)
    assert output is None


def test_band_name_in_lyrics_display_vertically_empty_name():
    name = ''
    lyrics = '... the quick brown fox jumps over the lazy dog ...'

    output = display_vertically(name, lyrics)

    assert output is None


def test_band_name_in_lyrics_display_vertically_empty_lyrics():
    name = 'Metallica'
    lyrics = ''

    output = display_vertically(name, lyrics)

    assert output is None
