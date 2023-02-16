import os
import time

# pip install PyOpenGL PyOpenGL_accelerate
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL.shaders import compileShader, compileProgram

CHECK_MS = 500
WIDTH, HEIGHT = 512, 512
VERTEX_SHADER_FILE = 'shader.vert'
FRAGMENT_SHADER_FILE = 'shader.frag'


def read_shader(filename):
    with open(filename) as f:
        return f.read()


def build_shader():
    vs = read_shader(VERTEX_SHADER_FILE)
    fs = read_shader(FRAGMENT_SHADER_FILE)

    glClearColor(0.0, 0.0, 0.0, 1.0)

    build_shader.program = compileProgram(
        compileShader(vs, GL_VERTEX_SHADER),
        compileShader(fs, GL_FRAGMENT_SHADER))
    glUseProgram(build_shader.program)

    vao = glGenVertexArrays(1)
    vd = [-1.0, -1.0, 0.0, 0.0, 0.0,
           1.0, -1.0, 0.0, 1.0, 0.0,
           1.0,  1.0, 0.0, 1.0, 1.0,
          -1.0,  1.0, 0.0, 0.0, 1.0]
    vd_gl = (GLfloat * len(vd))(*vd)
    glBindVertexArray(vao)
    glBindBuffer(GL_ARRAY_BUFFER, vao)
    glBufferData(GL_ARRAY_BUFFER, len(vd) * 4, vd_gl, GL_STATIC_DRAW)

    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, False, 20, ctypes.c_void_p(0))

    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 2, GL_FLOAT, False, 20, ctypes.c_void_p(12))


def update_check_time(mtime=False):
    check_files.time = time.time()

    if not mtime:
        return

    check_files.vertex_shader_mtime = os.path.getmtime(VERTEX_SHADER_FILE)
    check_files.fragment_shader_mtime = os.path.getmtime(FRAGMENT_SHADER_FILE)


def check_files():
    if time.time() - check_files.time < CHECK_MS * 0.001:
        return

    update_check_time()

    vs_mt = os.path.getmtime(VERTEX_SHADER_FILE)
    fs_mt = os.path.getmtime(FRAGMENT_SHADER_FILE)

    if vs_mt > check_files.vertex_shader_mtime or fs_mt > check_files.fragment_shader_mtime:
        update_check_time(mtime=True)

        print('Recompiling shader program...')
        build_shader()

        glutPostRedisplay()


def display(t, fbo):
    glClear(GL_COLOR_BUFFER_BIT)

    glUseProgram(build_shader.program)

    glBindTexture(GL_TEXTURE_2D, t)
    glBindFramebuffer(GL_FRAMEBUFFER, 0)

    glDrawArrays(GL_QUADS, 0, 4)

    glutSwapBuffers()


def main():
    glutInit()

    glutInitWindowSize(WIDTH, HEIGHT)
    glutCreateWindow('Shader Window')

    build_shader()

    t = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, t)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, WIDTH, HEIGHT, 0, GL_RGB, GL_UNSIGNED_BYTE, None)

    fbo = glGenFramebuffers(1)
    glBindFramebuffer(GL_FRAMEBUFFER, fbo)
    glFramebufferTexture2D(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0, GL_TEXTURE_2D, t, 0)

    assert glCheckFramebufferStatus(GL_FRAMEBUFFER) == GL_FRAMEBUFFER_COMPLETE

    glutDisplayFunc(lambda: display(t, fbo))
    glutIdleFunc(check_files)

    glutMainLoop()


if __name__ in '__main__':
    update_check_time(mtime=True)
    main()

