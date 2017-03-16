# Jinja2 `os.path` Filters

A Jinja2 extension that introduces the filters `basename` and `dirname`.


## Examples

    my_path = "/some/absolute/path/with/file.txt"
    {{ my_path | basename }}

Will fill in `file.txt`.

    my_path = "/some/absolute/path/with/file.txt"
    {{ my_path | dirname }}

Will fill in `/some/absolute/path/with`.

## Copyright and Licensing

* Copyright 2017, [Moritz Emanuel Beber](mailto:midnighter@posteo.net)
* Free software: [3-Clause BSD License](LICENSE)
