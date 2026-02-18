# Bad Apple on RARS (RISC-V Emulator)
This is a simple toy project which plays the entirety of Bad Apple on the 256x256 bitmap display of RARS. `converter.py` converts the original .mp4 video in a binary file, where the value of each byte indicates how many pixels are white (or black) in each row of each frame. The project already plays the whole video as is with the supplied `bad_apple.dat`. The bitmap display is mapped on the heap, starting at address 0x10040000.

Here's a short gif showing the final result:

<p align="center">
  <img src="https://github.com/Ancom05/BadAppleRars/blob/master/example.gif" alt="animated" />
</p>