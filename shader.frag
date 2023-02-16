#version 330 core

in vec2 uv_out;


void main() {
    gl_FragColor = vec4(uv_out.x, uv_out.y, 0.0, 1.0);
}

