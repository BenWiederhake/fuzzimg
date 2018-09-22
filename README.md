# fuzzimg

> Shuffle and sort pixels of an image

So you have an image and want to poke the pixels, and combine operations in a silly way.

`fuzzimg` does that.  In an incredibly stupid, simple, but fun way.

## Table of Contents

- [Background](#background)
- [Usage](#usage)
- [Examples](#examples)
- [TODOs](#todos)
- [Contribute](#contribute)

## Background

"What if you sort the pixels of an image, but not sort-sort, rather only sort them a little bit?"

Well, now you know.

## Usage

There's not much to it.

```
$ ./fuzzimg.py 
USAGE: ./fuzzimg.py <INPUT_FILENAME>…
$ echo $?
1
$ ./fuzzimg.py examples/green.jpg
For examples/green.jpg (sorted);
    Reading …
    Columns …
    Rows …
    Reassemble …
    Write out …
For examples/green.jpg (shuffled);
    Reading …
    Columns …
    Rows …
    Reassemble …
    Write out …
Done!
$
```

## Examples

### `wecker`

One day my alarm clock had a bitflip or whatever.

![](/examples/wecker.jpg)

If you shuffle the pixels (mostly), you get this mess:

![](/examples/wecker.jpg_shuffled.png)

Sorted (mostly), you get this weird thing:

![](/examples/wecker.jpg_sorted.png)

### `green`

Here's a nice photo I took while walking home

![](/examples/green.jpg)

If you shuffle the pixels (mostly), you get this mess:

![](/examples/green.jpg_shuffled.png)

Sorted (mostly), you get this weird thing:

![](/examples/green.jpg_sorted.png)

## TODOs

* More silly operations

## Contribute

Feel free to dive in! [Open an issue](https://github.com/BenWiederhake/fuzzimg/issues/new) or submit PRs.

## License

Code is under MIT license.
If you want to use the images (both source and derivates), please ask me beforehand.
I'll probably MIT them, too, but am curious why you would ever need them.
