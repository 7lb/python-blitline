# -*- coding: utf-8 -*-
from blitline import Function

class ResizeToFit(Function):
    def __init__(self, *args, **kw):
        super(ResizeToFit, self).__init__('resize_to_fit', *args, **kw)

class NoOp(Function):
    def __init__(self, *args, **kw):
        super(NoOp, self).__init__('no_op', *args, **kw)

class Lomo(Function):
    def __init__(self, *args, **kw):
        super(Lomo, self).__init__('lomo', *args, **kw)

class Resize(Function):
    def __init__(self, *args, **kw):
        super(Resize, self).__init__('resize', *args, **kw)

class Composite(Function):
    def __init__(self, *args, **kw):
        super(Composite, self).__init__('composite', *args, **kw)

class ImaggaSmartCrop(Function):
    def __init__(self, *args, **kw):
        super(ImaggaSmartCrop, self).__init__('imagga_smart_crop', *args, **kw)
