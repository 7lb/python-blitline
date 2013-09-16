python-blitline
===============

Python client for blitline service. It is a thin wrapper over the JSON API.

Install with pip:

    $ pip install python-blitline

Documentation
=============
There is no formal documentation, but this is an example:

```python
import blitline as b

# Your Application ID
BLITLINE_ID = "XXXXXXXXXXXXXXXXXXXX"

blitline_avatar = b.Job(
    b.ResizeToFit(
        width=165,
        height=165,
        save=b.S3Destination(
            bucket="my-s3-bucket",
            key='avatars/{username}.jpg',
            headers={
                'Content-Type': 'image/jpg',
            })))

for u in usernames:
    SRC_URL = "http://example.org/pics/{username}.jpg".format(username=u)
    res = blitline_avatar(BLITLINE_ID, SRC_URL, username=u)
    
    # You can do several things with a running job:
    
    # res.wait() -> wait for job end (default timeout: 5s)
    # res.open(DEST_IMAGE) -> open the specified destination image (streamed download)
    # res.download(DEST_IMAGE, output_file) -> download the specified image and write it to the output file
    # res.download_all(DIR) -> download all output images in the specified directory
```


