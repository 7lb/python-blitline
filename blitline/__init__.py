# -*- coding: utf-8 -*-
import json
import random
import requests
from urlparse import urlsplit

class Function(object):
    function_name = None
    def __init__(self, **kw):
        self.functions = kw.pop('functions', [])
        self.save = kw.pop('save', None) or Save()
        self.params = kw

    def __str__(self):
        params = []
        for i in self.params.items():
            params.append('='.join(map(str, i)))
        return '{0}({1}) -> {2}'.format(self.function_name, ','.join(params), str(self.save))

    def serialize(self, ctx):
        doc = {
            'name': self.function_name,
            'params': self.params,
        }
        save = self.save.serialize(ctx)
        if save:
            doc['save'] = save
        if self.functions:
            jf = []
            for f in self.functions:
                jf.append(f.serialize(ctx))
            doc['functions'] = jf
        return doc

class Save(object):
    def __init__(self, image_identifier=None, quality=None, save_metadata=None):
        self.image_identifier = image_identifier or self._random_id()
        self.quality = quality
        self.save_metadata = save_metadata

    def __str__(self):
        params = ['image_identifier=%s' % self.image_identifier]
        if self.quality is not None:
            params.append('quality=%s' % self.quality)
        if self.save_metadata is not None:
            params.append('save_metadata=%s' % self.save_metadata)
        return 'Save(%s)' % ','.join(params)

    def _random_id(self):
        return 'img%s-{name}' % (random.random(),)

    def serialize(self, ctx):
        doc = {
            'image_identifier': self.image_identifier.format(**ctx),
        }
        if self.quality is not None:
            doc['quality'] = self.quality
        if self.save_metadata is not None:
            doc['save_metadata'] = self.save_metadata
        return doc

class S3Destination(Save):
    def __init__(self, bucket, key, headers=None, *args, **kw):
        super(S3Destination, self).__init__(*args, **kw)
        self.bucket = bucket
        self.key = key
        self.headers = headers

    def serialize(self, ctx):
        doc = super(S3Destination, self).serialize(ctx)
        doc['s3_destination'] = {
            'bucket': self.bucket.format(**ctx),
            'key': self.key.format(**ctx),
        }
        if self.headers is not None:
            h = dict((k, v.format(**ctx)) for k,v in self.headers.items())
            doc['s3_destination']['headers'] = h
        return doc

class NoSave(object):
    def serialize(self, ctx):
        return {}

class JobError(Exception):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message

    def __str__(self):
        return 'JobError(%s) - %s' % (self.status_code, self.message)

class Job(object):
    def __init__(self, *functions):
        self.functions = functions

    def __call__(self, application_id, src, **ctx):
        ctx.update({
            'application_id': application_id,
            'src': src,
        })
        if 'name' not in ctx:
            ctx['name'] = urlsplit(src).path.rsplit('/', 1)[1]
        doc = self.serialize(ctx=ctx)
        r = requests.post(
            "http://api.blitline.com/job",
            data={'json': json.dumps(doc)},
            timeout=5)
        results = r.json['results']
        if r.status_code != 200 or 'error' in results:
            raise JobError(r.status_code, r.content)
        return JobResult.build_from_response(results)

    def serialize(self, ctx):
        doc = {
            'application_id': ctx['application_id'],
            'src': ctx['src'],
            'functions': [ f.serialize(ctx) for f in self.functions ],
        }
        try:
            doc['postback_url'] = ctx['postback_url']
        except KeyError:
            pass
        return doc

class JobResult(object):
    def __init__(self):
        self.job_id = None
        self.error = None
        self.images = None

    @classmethod
    def build_from_response(cls, response):
        r = cls()
        r.job_id = response['job_id']
        r.error = response.get('error')
        images = {}
        for x in response['images']:
            images[x['image_identifier']] = x['s3_url']
        r.images = images
        return r

    @classmethod
    def poll_job(cls, job_id):
        url = "http://cache.blitline.com/listen/{job_id}".format(job_id=job_id)
        r = requests.get(url, timeout=5)
        output = r.json
        if isinstance(output['results'], basestring):
            output['results'] = json.loads(output['results'])
        return output

    def wait(self):
        r = self.poll_job(self.job_id)['results']
        output = {
            'original_meta': r['original_meta'],
        }
        for i in r['images']:
            iid = i.pop('image_identifier')
            output[iid] = i
        return output

    def open(self, image_identifier, stream=True):
        remote = self.images[image_identifier]
        if not stream:
            return requests.get(remote)
        else:
            return requests.get(remote, stream=True)

    def download(self, image_identifier, output, chunk=10*1024):
        try:
            r = self.open(image_identifier, stream=True)
        except TypeError:
            r = self.open(image_identifier, stream=False)
            output.write(r.content)
        else:
            while True:
                buff = r.raw.read(chunk)
                print 'read', image_identifier, len(buff)
                if not buff:
                    break
                output.write(buff)

    def download_all(self, destination):
        import os.path
        for iid in self.images:
            self.download(iid, file(os.path.join(destination, iid), 'w'))

from blitline.functions import *
