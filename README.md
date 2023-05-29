# name
- DebugNodeVbs

## Overview
- Arbitrary nodes implemented in VBScript (e.g., customized WinActor nodes) can be easily tested in Python.

## Requirement
- Windows 10 Pro or above
- Python 3.11.0
- VBScript 5.812

## Usage
- Register keywords to be excluded from processing in the VBS program, line by line.
- Register the corresponding variables to set variables in the VBS program. The delimiter is ",".
- The command line to execute is as follows.
```
python DebugNodeVbs.py (Target VBS) (! Keywords enclosed in ! and their values are set with the delimiter character =. Multiple values can be set.)
```
- example
```
python DebugNodeVbs.py .\sample.vbs 開始セル="A9" 終了セル="AE9"
```

## Features
- Referring to exclusive.data and concat.data and options, this program reconstructs a VBS program that can be executed on the command line.
- This program executes the reconfigured VBS program.

## Reference
- None

## Author
- superbunnbun

## Licence
[MIT](https://github.com/superbunnbun/DebugNodeVbs/blob/main/LICENSE)