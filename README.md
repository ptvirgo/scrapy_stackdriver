# Scrapy Stackdriver (unofficial)

This [Scrapy]("http://scrapy.org") extension adds [Google
StackDriver]("https://cloud.google.com/stackdriver/") logging to the Scrapy
spiders.  It simply attaches the Google handler to the spider's built-in
logger, so you don't have to change your spider's code.

Logs will appear on the StackDriver log page for your project, under the name
`scraper.<spider name>`.

## Configuration

```bash
$ pip install [...]
```

Add to your `settings.py`

```python

STACKDRIVER_ENABLED = True
STACKDRIVER_PROJECT_ID = '<your google cloud project>'

EXTENSIONS = {
    'scrapy_stackdriver.StackDriverLogger': 500
}

```
### Settings

- `STACKDRIVER_ENABLED` controls whether the extension is active
- `STACKDRIVER_PROJECT_ID` should be your [Google project
  id](https://support.google.com/cloud/answer/6158840?hl=en)

As per other Google Cloud projects, you will also need to [appropriately
set the
`GOOGLE_APPLICATION_CREDENTIALS`](https://cloud.google.com/docs/authentication/production)
variable for your environment.
