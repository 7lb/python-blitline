#autogenerated on 2015-09-01 12:11:16.873595
from blitline import Function

class Annotate(Function):
    """
    Adds text to an image
    """
    function_name = "annotate"


class Append(Function):
    """
    Appends images together either vertically or horizontally
    """
    function_name = "append"


class AutoLevel(Function):
    """
    Automatically adjusts the levels the color channels of an image
    """
    function_name = "auto_level"


class AutoGamma(Function):
    """
    Automatically adjusts the brightness levels of the channels of an image
    """
    function_name = "auto_gamma"


class AutoEnhance(Function):
    """
    Automatically 'enhances' (magic wand) an image.
    """
    function_name = "auto_enhance"


class Blur(Function):
    """
    Blurs an image
    """
    function_name = "blur"


class BackgroundColor(Function):
    """
    Sets a transparent background color to be a solid (useful when converting pngs to jpgs)
    """
    function_name = "background_color"


class Composite(Function):
    """
    Composites one image onto another
    """
    function_name = "composite"


class Contrast(Function):
    """
    Adjusts contrasts within the image.
    """
    function_name = "contrast"


class Caption(Function):
    """
    Annotates an image with text autowrap feature.
    """
    function_name = "caption"


class ContrastStretchChannel(Function):
    """
    Adjusts contrasts within the image.
    """
    function_name = "contrast_stretch_channel"


class ConvertCommand(Function):
    """
    Advanced function with direct access to IM's convert command.
    """
    function_name = "convert_command"


class Crop(Function):
    """
    Crop an image to a specific size.
    """
    function_name = "crop"


class CropToSquare(Function):
    """
    Crop an image to a sqaure, based on height vs width. Square side length will be the smaller of the 2.
    """
    function_name = "crop_to_square"


class DeleteProfile(Function):
    """
    Deletes color profile information.
    """
    function_name = "delete_profile"


class Deskew(Function):
    """
    Tries to relalign a slightly distorted image. (Typically used in scanning and OCR)
    """
    function_name = "deskew"


class Density(Function):
    """
    Sets the DPI of an image
    """
    function_name = "density"


class Despeckle(Function):
    """
    Reduces the speckle noise while preserving the edges
    """
    function_name = "despeckle"


class Dissolve(Function):
    """
    Composites with transparency
    """
    function_name = "dissolve"


class Ellipse(Function):
    """
    Draws an ellipse
    """
    function_name = "ellipse"


class Enhance(Function):
    """
    Reduces noise in the image
    """
    function_name = "enhance"


class Equalize(Function):
    """
    Equalizes an image (Auto-adjust image).
    """
    function_name = "equalize"


class GammaChannel(Function):
    """
    Adjusts contrasts within the image.
    """
    function_name = "gamma_channel"


class GrayColorspace(Function):
    """
    Turns image into grayscale.
    """
    function_name = "gray_colorspace"


class ImaggaSmartCrop(Function):
    """
    Uses Imagga image analysis tools to determine the best crop for you photo. This requires a Blitline+Imagga subscription.
    """
    function_name = "imagga_smart_crop"


class Line(Function):
    """
    Draws a linear line between two points.
    """
    function_name = "line"


class Level(Function):
    """
    Levels channels of image
    """
    function_name = "level"


class Level(Function):
    """
    Inverse of 'level'
    """
    function_name = "level"


class LiquidRescale(Function):
    """
    Uses seam carving to reduce image size
    """
    function_name = "liquid_rescale"


class MedianFilter(Function):
    """
    Applies a digital filter that improves the quality of a noisy image. Each pixel is replaced by the median in a set of neighboring pixels as defined by radius.
    """
    function_name = "median_filter"


class Modulate(Function):
    """
    Changes the brightness, saturation, and hue.
    """
    function_name = "modulate"


class NoOp(Function):
    """
    Simple noop(no operation). No function performed on image.
    """
    function_name = "no_op"


class Normalize(Function):
    """
    Changes the contrast of a color image by adjusting the pixel color to span the entire range of colors available.
    """
    function_name = "normalize"


class Pad(Function):
    """
    Add empty space to one side or all sides of image (Useful for centering an image on a new canvas color)
    """
    function_name = "pad"


class PadResizeToFit(Function):
    """
    Resize to fit, but will pad to keep the aspect ratio. So for example, if you are going from a 3:4 aspect ratio to a 3:2 aspect ratio, this method will assure the result the desired output size, and pad the filled in area with a specified color.
    """
    function_name = "pad_resize_to_fit"


class Photograph(Function):
    """
    Creates an image that has a white border, with a slight curl, that appears like a photograph
    """
    function_name = "photograph"


class Pixelate(Function):
    """
    Pixelates an area on an image
    """
    function_name = "pixelate"


class Quantize(Function):
    """
    Analyzes the colors within a reference image and chooses a fixed number of colors to represent the image
    """
    function_name = "quantize"


class Rectangle(Function):
    """
    Draws a rectangle
    """
    function_name = "rectangle"


class Resample(Function):
    """
    Resample the image to a new resolution
    """
    function_name = "resample"


class Resize(Function):
    """
    Resize the image to a specific height and width.
    """
    function_name = "resize"


class ResizeToFill(Function):
    """
    Resize the image to fit within the specified dimensions while retaining the aspect ratio of the original image. If necessary, crop the image in the larger dimension
    """
    function_name = "resize_to_fill"


class ResizeToFit(Function):
    """
    Resize the image to fit within the specified dimensions while retaining the original aspect ratio. The image may be shorter or narrower than specified in the smaller dimension but will not be larger than the specified values
    """
    function_name = "resize_to_fit"


class Rotate(Function):
    """
    Rotates the image.
    """
    function_name = "rotate"


class Scale(Function):
    """
    Resize the image to a specific height and width.
    """
    function_name = "scale"


class Script(Function):
    """
    Run your own scripts on Blitline cloud servers. Perfect for using your own ImageMagick scripts
    """
    function_name = "script"


class SepiaTone(Function):
    """
    Applies sepia filter
    """
    function_name = "sepia_tone"


class Sharpen(Function):
    """
    Sharpens the image
    """
    function_name = "sharpen"


class Sketch(Function):
    """
    Simulates a pencil sketch.
    """
    function_name = "sketch"


class Stegano(Function):
    """
    Embeds a hidden watermark in the image.
    """
    function_name = "stegano"


class Tile(Function):
    """
    Tiles a src image over the current image.
    """
    function_name = "tile"


class Trim(Function):
    """
    Makes a 'best guess' crop to upper-left and lower-right corners. For example, if you have an image with a bunch of white border around it, and you want it cropped to only where there something other than the border color.
    """
    function_name = "trim"


class UnsharpMask(Function):
    """
    Sharpens an image
    """
    function_name = "unsharp_mask"


class Vignette(Function):
    """
    Gradually shades the edges of the image by transforming the pixels into the background color.
    """
    function_name = "vignette"


class Watermark(Function):
    """
    Adds a text watermark to an image. For more control use 'annotate'
    """
    function_name = "watermark"


class Vintage(Function):
    """
    Vintage Filter
    """
    function_name = "vintage"


class Lomo(Function):
    """
    Lomo Filter
    """
    function_name = "lomo"


class Photograph(Function):
    """
    Photograph Filter
    """
    function_name = "photograph"


class Savannah(Function):
    """
    Savannah Filter
    """
    function_name = "savannah"


class Xpro(Function):
    """
    Xpro Filter
    """
    function_name = "xpro"


class Celsius(Function):
    """
    Celsius Filter
    """
    function_name = "celsius"


class Stackhouse(Function):
    """
    Stackhouse Filter
    """
    function_name = "stackhouse"

