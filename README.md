# Python Dialpad API Client

A python wrapper around the Dialpad REST API

## Installation

For now, this package is private and unpublished, but it's still reasonably easy to install on your
machine:

```bash
git clone git@github.com:jakedialpad/python-dialpad.git
cd python-dialpad
python ./setup.py install
```

## Usage

I'll be adding more to this repo here and there, but for now here's a quick snippet to demonstrate
how to use this library to make it less painful to test new endpoints. I have this little snippet
in a python script that I just modify and run when I want to test things:

```python
import dialpad

DP_ENV = 'jake'

if DP_ENV == 'jake':
  client = dialpad.DialpadClient(base_url='https://jake-dot-uv-beta.appspot.com', token='O_o')
else:
  client = dialpad.DialpadClient(beta=True, token=':O')


try:
  print client.transcripts.get(
    call_id='6435876717723648',
  )
except Exception as e:
  print e
```

[Learn More](https://www.dialpad.com/developers/docs/)
