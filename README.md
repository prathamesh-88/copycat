# CopyCat

Transfers and appends the stdin data to a given output file. Provides you with added features such as sorting the file alphabetically, removing duplicates, etc.


## Usage

 > `copycat [-h] [-u] [-a] [-s] [-r] output_filename`


#### Positional arguments:

|  Argument  |  Use  |
|---|---|
|  output_filename  |  Specify the file name to output the result  |


#### Optional Arguments

| Flags | Function  |
|---|---|
|-h, --help | Show this help message and exit  |
|  -u, --unique | Removes duplicate lines |
|  -a, --append | Appends to the file without overwriting previous content  ||
|  -s, --sort | Sort the file alphabetically |
|  -r, --remove-duplicates  | Removes all duplicates from the file |

