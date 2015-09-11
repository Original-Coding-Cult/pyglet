from __future__ import absolute_import
from .test_image_saving import ImageSavingTestCase

from pyglet.gl import *
from pyglet import image

class BufferCopyTestCase(ImageSavingTestCase):
    """Test colour buffer copy to texture.

    A scene consisting of a single coloured triangle will be rendered.  The
    colour buffer will then be saved to a stream and loaded as a texture.

    You will see the original scene first for up to several seconds before the
    buffer image appears (because retrieving and saving the image is a slow
    operation).  Messages will be printed to stdout indicating what stage is
    occuring.
    """
    alpha = False
    show_checkerboard = False

    def draw_original(self):
        glBegin(GL_TRIANGLES)
        glColor4f(1, 0, 0, 1)
        glVertex3f(0, 0, -1)
        glColor4f(0, 1, 0, 1)
        glVertex3f(200, 0, 0)
        glColor4f(0, 0, 1, 1)
        glVertex3f(0, 200, 1)
        glEnd()

        glColor4f(1, 1, 1, 1)

        if not self.saved_texture:
            self.saved_texture = \
                image.get_buffer_manager().get_color_buffer().texture


BufferCopyTestCase.create_test_case(
        name='test_copy_buffer',
        question='Do you see two equal coloured triangles?'
        )